
// handler para esconder o popup
closer.onclick = function() {
    overlay.setPosition(undefined);
    closer.blur();
    return false;
};


//# Pop-ups com posição fixa #//
$('#legenda').hide()


// volta a visão para que foi utilizada antes de alguma iteração com as pesquisas
if (visao_return){
    visao = visao_return
}

muda_visao(visao)



////# MAPA #////
map = new ol.Map({
    // adicionando os controles básicos e extendendo ao criado
    controls: ol.control.defaults({
        attributionOptions: {collapsible: false}
    })
    // .extend([
    //     new app.Visoes(),
    // ])
    ,
    // vector layer, onde estão as features (geometrias) dos vetores/shapes
    layers: [vl_svpontos, vl_sisvias, vl_titulos, vl_mapas],
    overlays: [overlay], // adicionando o popup "por cima" do mapa (overlayer)
    target: 'map',

    // Configurações da visão
    view: new ol.View({
        center: [-55, -13],
        minResolution: 190 / Math.pow(2, 30),
        zoom: 23,
        minZoom: 23,
        extent: [-62, -18, -50, -6]

    }),
});



//# onClick no mapa #//
map.on('singleclick', function(evt) {

    overlay.setPosition(undefined); // Retirando o Pop-up de apresentação no mapa
    closer.blur();

    var layr_clicked
    // checa e retorna a feature que foi clicada (null caso nenhuma tenha sido)
    var feature = map.forEachFeatureAtPixel(evt.pixel, function(feature, layer) {
        //you can add a condition on layer to restrict the listener
        layr_clicked = layer.get('name')
        return feature;
        });


    // Check se alguma feature (e caso, se aceita) foi clicada
    if (feature) {


        // 0-Mesorregiões; 1-Microrregiões; 2-Províncias; 3-Munícipios
        var cod = -1; // codigo da feature selecionada
        var nome; // nome da feature selecionada
        var resu_html = ''; // variável auxiliar para criar informações no popup
        var p; // texto auxiliar das infos retornadas da base de dados
        var cfem; // texto html do resultado CFEM

        // checa o código e nome da feature de acordo com o tipo de visão

        // Caso não tenha sido feito pesquisa sobre titulos (ou seja, análise dos dados)
        if (!titulos){

            cod = feature.values_.pk
            nome = feature.values_.nome

            if (temporal) {
                google.charts.setOnLoadCallback(drawChart); // callback da função de desenhar o gráfico
                pk_click = feature.values_.pk
                drawChart()
                google.charts.setOnLoadCallback(drawChart_uf);
                drawChart_uf()

            }

            // Checar visão atual == visão da pesquisa
            else if (visao == visao_return){

                if (resultado_analise){ // confirmando analise dos dados

                    resu_html = '<h3>' + nome + '</h3> <br>'

                    // Pegar valor do resultado tah p/ removê-lo do json
                    // ps: arrecadação tah é o único dado não dividido por ano


                    var tah
                    if (resultado_analise[cod]['tah'])
                        tah = Object.assign({}, resultado_analise[cod]['tah'])
                        delete resultado_analise[cod]['tah']

                    // Iniciando código html da tabela resultante
                    resu_html += '\
                        <table class="table">\
                            <thead>\
                                <tr>\
                                    <th scope="col">Ano</th>\
                                    <th scope="col">CFEM</th>\
                                    <th scope="col">' + pesquisado_analise + '</th>\
                                </tr>\
                            </thead>\
                        '

                    // percorrendo os dados por ano
                    for (var anot in resultado_analise[cod]){
                        p = null //variável auxiliar para os dados pesquisados diferentes de CFEM

                        //coluna para resultantes da arrecadação CFEM
                        cfem = '<td>'
                        for (var un in resultado_analise[cod][anot]['cfem']){
                            cfem += '\
                                Quantidade: ' + check_float(resultado_analise[cod][anot]['cfem'][un][0], 4) + un + '<br>\
                                Valor: R$' + check_float(resultado_analise[cod][anot]['cfem'][un][1], 2) + '<br>'
                        }
                        cfem += '</td>'

                        //# Colunas para as tabelas do dado escolhido para "cruzar" (demografico, economico, socioeconomico) #//

                        // gerando coluna para demografico
                        if (resultado_analise[cod][anot]['demografico']){
                            p = '\
                                <td>População urbana: ' + resultado_analise[cod][anot]['demografico'][0] + '<br>\
                                População rural: ' + resultado_analise[cod][anot]['demografico'][1] + '<br>\
                                População total: ' + resultado_analise[cod][anot]['demografico'][2] + '<br>\
                                </td>'
                        }

                        // gerando coluna para economico

                        else if (resultado_analise[cod][anot]['economico']){
                            p = '\
                                <td>PIB per capita: R$ ' + check_float(resultado_analise[cod][anot]['economico'][0][0], 2) + '<br>\
                                Receitas (fonte externa): R$ ' + check_float(resultado_analise[cod][anot]['economico'][1][0], 2) + '<br>\
                                Receitas: R$ ' + check_float(resultado_analise[cod][anot]['economico'][2][0], 2) + '<br>\
                                Despesas: R$ ' + check_float(resultado_analise[cod][anot]['economico'][3][0], 2) + '<br>\
                                População ativa (18 anos +): ' + resultado_analise[cod][anot]['economico'][4][0] + '<br>\
                                Ocupado no setor agropecuario: ' + check_float(resultado_analise[cod][anot]['economico'][5][0], 2) + '%<br>\
                                Ocupado no setor de comércio: ' + check_float(resultado_analise[cod][anot]['economico'][6][0], 2) + '%<br>\
                                Ocupado no setor de construção: ' + check_float(resultado_analise[cod][anot]['economico'][7][0], 2) + '%<br>\
                                Ocupado no setor de mineração: ' + check_float(resultado_analise[cod][anot]['economico'][8][0], 2) + '%<br>\
                                Ocupado no setor de industria de utilidade pública: ' + check_float(resultado_analise[cod][anot]['economico'][9][0], 2) + '%<br>\
                                Ocupado no setor serviços: ' + check_float(resultado_analise[cod][anot]['economico'][10][0], 2) + '%<br>\
                                Ocupado no setor industria de transformação: ' + check_float(resultado_analise[cod][anot]['economico'][11][0], 2) + '%<br>\
                                Ocupado com grau de formação: ' + check_float(resultado_analise[cod][anot]['economico'][12][0], 2) + '%<br>\
                                Ocupado com ensino fundamental: ' + check_float(resultado_analise[cod][anot]['economico'][13][0], 2) + '%<br>\
                                Ocupado com ensino médio  : ' + check_float(resultado_analise[cod][anot]['economico'][14][0], 2) + '%<br>\
                                Ocupado com ensino superior: ' + check_float(resultado_analise[cod][anot]['economico'][15][0], 2) + '%<br>\
                                </td>'
                        }

                        // gerando coluna para socioeconomico
                        else if (resultado_analise[cod][anot]['socioeconomico']) {
                            p = '\
                                <td>População ocupada: ' + check_float(resultado_analise[cod][anot]['socioeconomico'][0][0], 2) + '%<br>\
                                IDHM (média da região): ' + check_float(resultado_analise[cod][anot]['socioeconomico'][1][0], 3) + '<br>\
                                IHDM-Renda (média da região): ' + check_float(resultado_analise[cod][anot]['socioeconomico'][2][0], 3) + '<br>\
                                IDHM-Longevidade (média da região): ' + check_float(resultado_analise[cod][anot]['socioeconomico'][3][0], 3) + '<br>\
                                IDHM-Educação (média da região): ' + check_float(resultado_analise[cod][anot]['socioeconomico'][4][0], 3) + '<br>\
                                Expectativa de vida (média da região): ' + check_float(resultado_analise[cod][anot]['socioeconomico'][5][0], 2) + '<br>\
                                Probabilidade de alcançar 60 anos (média da região): ' + check_float(resultado_analise[cod][anot]['socioeconomico'][6][0], 2) + '%<br>\
                                Expectativa de anos de estudo (média da região): ' + check_float(resultado_analise[cod][anot]['socioeconomico'][7][0], 2) + '<br>\
                                Renda per capita: R$ ' + check_float(resultado_analise[cod][anot]['socioeconomico'][8][0], 2) + '<br>\
                                Salário trabalho formal (média da região): ' + check_float(resultado_analise[cod][anot]['socioeconomico'][9][0], 2) + '<br>\
                                População em extrema pobreza: ' + check_float(resultado_analise[cod][anot]['socioeconomico'][10][0], 2) + '%<br>\
                                População em pobreza: ' + check_float(resultado_analise[cod][anot]['socioeconomico'][11][0], 2) + '%<br>\
                                População em vulnerabilidade a pobreza: ' + check_float(resultado_analise[cod][anot]['socioeconomico'][12][0], 2) + '%<br>\
                                Taxa de analfabetismo com 15 anos ou mais: ' + check_float(resultado_analise[cod][anot]['socioeconomico'][13][0], 2) + '%<br>\
                                IDEB - anos iniciais (média da região): ' + check_float(resultado_analise[cod][anot]['socioeconomico'][14][0], 2) + '<br>\
                                IDEB - anos finais (média da região): ' + check_float(resultado_analise[cod][anot]['socioeconomico'][15][0], 2) + '<br>\
                                População com água encanada: ' + check_float(resultado_analise[cod][anot]['socioeconomico'][16][0], 2) + '%<br>\
                                População com energia elétrica: ' + check_float(resultado_analise[cod][anot]['socioeconomico'][17][0], 2) + '%<br>\
                                População com esgoto sanitário adequado: ' + check_float(resultado_analise[cod][anot]['socioeconomico'][18][0], 2) + '%<br>\
                                População com esgoto sanitário inadequado: ' + check_float(resultado_analise[cod][anot]['socioeconomico'][19][0], 2) + '%<br>\
                                Urbanização nas vias públicas: ' + check_float(resultado_analise[cod][anot]['socioeconomico'][20][0], 2) + '%<br>\
                                </td>'
                        }

                        // Inserindo de fato os dados na tabela
                        resu_html += '<tbody><tr>'
                        resu_html += '<th scope="row"> ' + anot + '</th>'

                        // Inserindo dados CFEM na tabela caso exista p/ respectivo ano
                        if (cfem){
                            resu_html += cfem
                        }

                        // Inserindo dados de "cruzamento" na tabela caso exista p/ respectivo ano
                        if (p){
                            resu_html += p
                        }
                        resu_html += '</tr>'


                    }

                    // Inserindo dados TAH ao fim da tabela caso exista
                    if (tah){
                        resu_html += '\
                            <tr>\
                                <th scope="row">TAH</th>\
                                <td colspan"2">Total recebido: R$' + check_float(tah[0], 2) + '<br>\
                                    Total cobrado: R$' + check_float(tah[1], 2) + '<br>\
                                </td>\
                            </tr>'
                    }

                    // Finalizando código html da tabela
                    resu_html += '</tbody></table>'

                    // Adicionando o código da tabela ao Pop-up
                    content.innerHTML = resu_html
                    content.scrollTop = content.scrollHeight;
                    overlay.setPosition(evt.coordinate); // Posicionando overlay no ponto clicado
                }


                else if(substratos_regiao){ // caso pesquisa feita sobre substratos encontrados na regiao
                    // Iniciando a tabela
                    resu_html = '<h3>' + nome + '</h3> <br>\
                        <table class="table">\
                            <thead>\
                                <tr>\
                                    <th scope="col">Substrato</th>\
                                    <th scope="col">Quantidade</th>\
                                </tr>\
                            </thead>\
                            <tbody>'

                    // Cria e percorre por substrado encontrado na região clicada
                    for (var sub in substratos_regiao[cod]){
                        resu_html += '\
                            <tr>\
                                <td>' + sub + ' </td>\
                                <td>\
                        '
                        // Acrescenta quantidade encontrada do respectivo substrato (possui diferentes unidades de medida (ex: kg e m³))
                        for (var un in substratos_regiao[cod][sub]){
                            resu_html += '' + check_float(substratos_regiao[cod][sub][un], 2) + ' ' + un + '<br>'
                        }
                        resu_html += '</td></tr>'
                    }
                    // finaliza código da tabela
                    resu_html += '</tbody>'

                    // Adicionando o código da tabela ao Pop-up
                    content.innerHTML = resu_html
                    content.scrollTop = content.scrollHeight;
                    overlay.setPosition(evt.coordinate);// posicionando overlay no ponto clicado
                }
            }
        }


        else{ // separando o click do layer de títulos
            // ps: foi organizado dessa forma para evitar erros ao reconhecer o click a este layer
            if (layr_clicked == lTitulos){
                // pegando feature clicada
                var titulo_c = feature.values_

                $.ajax({
                    type: 'POST',
                    url: '',
                    // async: false,
                    data: {'titulo_click': titulo_c['pk']},
                    success: function(response){
                        // adicionando os dados ao Pop-up
                        content.innerHTML =
                        '<h5>' + titulo_c['nome_prop'] + '</h5>\
                        <p>Processo/Ano: ' + titulo_c['numero'] + '/' + titulo_c['ano'] + '<br>\
                        Cidade(s): ' + response.join(', ') + '<br>\
                        Substrato: ' + titulo_c['subs'] + '<br>\
                        Uso: ' + titulo_c['uso'] + '<br>\
                        Fase: ' + titulo_c['fase'] + '<br>\
                        Ultimo evento: ' + titulo_c['ult_evento'] + '<br>\
                        </p>'
                        content.scrollTop = content.scrollHeight;
                        overlay.setPosition(evt.coordinate);// posicionando overlay no ponto clicado
                        $('#loader').hide()
                    },
                    error: function (data) {
                        console.log('erro')
                    }
                })

            }
        }
    }

});


//# Interações visuais/pré-resultado com o mapa #//
var select = null // objeto da interação Select
var selected // objeto que irá conter o vetor com os ids das regiões selecionadas
var i = 0

// função para adicionar interação de select no mapa
function select_poly(name){
    console.log(map.getInteractions())

    if (select != null){
        map.removeInteraction(select);
    }
    select = new ol.interaction.Select({
        layers: function(layer){
            if (layer.get('name') == name) {
                layer.setZIndex(layer.getZIndex() + 2)
                return true
            }
        },
        filter: function(feature, layer) { //filtro para layer correta para efeito
            if (layer.get('name') == name) return true
        },
        style: style_select,
    });
    map.addInteraction(select);
    // if (name == lMapa){
    //     select.on('select', function(e){
    //         selected = e.target.getFeatures().getArray();
    //     });
    // }
}

// let select_mapa
// function refresh_interaction_mapa(){
//     if (select_mapa != null){
//         map.removeInteraction(select_mapa)
//     }
//     select_mapa = new ol.interaction.Select({
//         layers: function(layer){
//             if (layer.get('name') == lMapa || layer.get('name') == lTitulos) {
//                 layer.setZIndex(layer.getZIndex() + 2)
//                 return true
//             }
//         },
//         filter: function(feature, layer) { //filtro para layer correta para efeito
//             if (layer.get('name') == lMapa || layer.get('name') == lTitulos) return true
//         },
//         style: style_select,
//     });
//     map.addInteraction(select_mapa);
//     select_mapa.on('select', function(e){
//         selected = e.target.getFeatures().getArray();
//     })

//     console.log(map.getInteractions())
    
// }
refresh_interaction_mapa()
// select_poly(lMapa); // inserindo a interação no mapa pela primeira vez


function add_titulos(titulos){
    if (titulos == -1){
        //ToDO: Enviar erro a tela de não encontrado
        alert('Nenhum título encontrado')
    }
    else {

        // map.removeInteraction(select);
        let src_titulos = vl_titulos.getSource()
        src_titulos.clear()
        src_titulos.addFeatures((new ol.format.GeoJSON()).readFeatures(titulos))
        // criando um layer para adicionar o shape do titulos retornados

        // map.addLayer(vl_titulos)
        refresh_interaction_mapa()
        // select_poly(lTitulos)
    }
}
////## Caso retorno da pesquisa sobre os títulos (Apresentar no mapa) ##////
if (titulos){
    add_titulos()
}


////## CHECANDO RETORNOS DAS REQUISIÇÕES ##////

// Simulando o click nas abas em caso de retorno de requisição de alguma pesquisa
// #0 - form_dados; 1 - form_titulos; 2 - form_analise# //
if (form_selecionado == 0) {
    $('#btn_dados').trigger('click');
}

else if(form_selecionado == 1) {
    $('#btn_titulos').trigger('click');
}

else if(form_selecionado == 2) {
    $('#btn_analisar').trigger('click');
}

$('#nv-limpar').click(function(){
    limpa_results()
})

$('#nv-vis_mac').click(function(){
    muda_visao(0)
})

$('#nv-vis_mic').click(function(){
    muda_visao(1)
})

$('#nv-vis_pro').click(function(){
    muda_visao(0) // alterar para 2
})

$('#nv-vis_mun').click(function(){
    muda_visao(3)
})

$('#nv-via_rodo').click(function(){
    check_sisviario(0)
})

$('#nv-via_ferro').click(function(){
    check_sisviario(1)
})

$('#nv-via_hidro').click(function(){
    check_sisviario(2)
})

$('#nv-via_aero').click(function(){
    check_sisviario(3)
})

$('#nv-via_limpar').click(function(){
    check_sisviario(null)
})
