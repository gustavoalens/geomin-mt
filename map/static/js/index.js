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
                            let quantidade = check_float(resultado_analise[cod][anot]['cfem'][un][0], 4) // + un
                            let valor = check_float(resultado_analise[cod][anot]['cfem'][un][1], 2)
                            if (quantidade)
                                cfem += 'Quantidade: ' + quantidade + un + '<br>' 
                            if (valor)
                                cfem += 'Valor: R$' + valor + '<br>'
                        }
                        cfem += '</td>'

                        //# Colunas para as tabelas do dado escolhido para "cruzar" (demografico, economico, socioeconomico) #//

                        // gerando coluna para demografico
                        if (resultado_analise[cod][anot]['demografico']){
                            let pop_urb = resultado_analise[cod][anot]['demografico'][0]
                            let pop_rur = resultado_analise[cod][anot]['demografico'][1]
                            let pop_tot = resultado_analise[cod][anot]['demografico'][2]
                            
                            p = '<td>'
                            if (pop_urb)
                                p += 'Populacao urbana: ' + pop_urb + '<br>'
                            if (pop_rur)
                                p += 'Populacao rural: ' + pop_rur + '<br>'
                            if (pop_tot)
                                p += 'Populacao total: ' + pop_tot + '<br>'
                            p += '</td>'
                        }

                        // gerando coluna para economico

                        else if (resultado_analise[cod][anot]['economico']){
                            let pib_pc = check_float(resultado_analise[cod][anot]['economico'][0][0], 2)
                            let rec_fext = check_float(resultado_analise[cod][anot]['economico'][1][0], 2)
                            let receitas = check_float(resultado_analise[cod][anot]['economico'][2][0], 2)
                            let despesas = check_float(resultado_analise[cod][anot]['economico'][3][0], 2)
                            let pop_ativa = check_float(resultado_analise[cod][anot]['economico'][4][0], 0)
                            let oc_agrop = check_float(resultado_analise[cod][anot]['economico'][5][0], 2)
                            let oc_comer = check_float(resultado_analise[cod][anot]['economico'][6][0], 2)
                            let oc_const = check_float(resultado_analise[cod][anot]['economico'][7][0], 2)
                            let oc_miner = check_float(resultado_analise[cod][anot]['economico'][8][0], 2)
                            let oc_indup = check_float(resultado_analise[cod][anot]['economico'][9][0], 2)
                            let oc_servi = check_float(resultado_analise[cod][anot]['economico'][10][0], 2)
                            let oc_indtr = check_float(resultado_analise[cod][anot]['economico'][11][0], 2)
                            let oc_gform = check_float(resultado_analise[cod][anot]['economico'][12][0], 2)
                            let oc_enfun = check_float(resultado_analise[cod][anot]['economico'][13][0], 2)
                            let oc_enmed = check_float(resultado_analise[cod][anot]['economico'][14][0], 2)
                            let oc_ensup = check_float(resultado_analise[cod][anot]['economico'][15][0], 2)
                            
                            p = '<td>'
                            if (pib_pc)
                                p += 'PIB per capita: R$ ' + pib_pc + '<br>'
                            if (rec_fext)
                                p += 'Receitas (fonte externa): R$ ' + rec_fext + '<br>'
                            if (receitas)
                                p += 'Receitas: R$ ' + receitas + '<br>'
                            if (despesas)
                                p += 'Despesas: R$ ' + despesas + '<br>'
                            if (pop_ativa)
                                p += 'População ativa (18 anos +): ' + pop_ativa + '<br>'
                            if (oc_agrop)
                                p += 'Ocupado no setor agropecuario: ' + oc_agrop + '%<br>'
                            if (oc_comer)
                                p += 'Ocupado no setor de comércio: ' + oc_comer + '%<br>'
                            if (oc_const)
                                p += 'Ocupado no setor de construção: ' + oc_const + '%<br>'
                            if (oc_miner)
                                p += 'Ocupado no setor de mineração: ' + oc_miner + '%<br>'
                            if (oc_indup)
                                p += 'Ocupado no setor de industria de utilidade pública: ' + oc_indup + '%<br>'
                            if (oc_servi)
                                p += 'Ocupado no setor serviços: ' + oc_servi + '%<br>'
                            if (oc_indtr)
                                p += 'Ocupado no setor industria de transformação: ' + oc_indtr + '%<br>'
                            if (oc_gform)
                                p += 'Ocupado com grau de formalização: ' + oc_gform + '%<br>'
                            if (oc_enfun)
                                p += 'Ocupado com ensino fundamental: ' + oc_enfun + '%<br>'
                            if (oc_enmed)
                                p += 'Ocupado com ensino médio  : ' + oc_enmed + '%<br>'
                            if (oc_ensup)
                                p += 'Ocupado com ensino superior: ' + oc_ensup + '%<br>'
                            p += '</td>'
                            
                        }

                        // gerando coluna para socioeconomico
                        else if (resultado_analise[cod][anot]['socioeconomico']) {
                            let idhm = check_float(resultado_analise[cod][anot]['socioeconomico'][0][0], 3)
                            let idhm_renda = check_float(resultado_analise[cod][anot]['socioeconomico'][1][0], 3)
                            let idhm_longv = check_float(resultado_analise[cod][anot]['socioeconomico'][2][0], 3)
                            let idhm_educa = check_float(resultado_analise[cod][anot]['socioeconomico'][3][0], 3)
                            let expc_vida = check_float(resultado_analise[cod][anot]['socioeconomico'][4][0], 2)
                            let prob_60ans = check_float(resultado_analise[cod][anot]['socioeconomico'][5][0], 2)
                            let exp_anestu = check_float(resultado_analise[cod][anot]['socioeconomico'][6][0], 2)
                            let renda_pc = check_float(resultado_analise[cod][anot]['socioeconomico'][7][0], 2)
                            let sal_tform = check_float(resultado_analise[cod][anot]['socioeconomico'][8][0], 2)
                            let pop_extpob = check_float(resultado_analise[cod][anot]['socioeconomico'][9][0], 2)
                            let pop_pobre = check_float(resultado_analise[cod][anot]['socioeconomico'][10][0], 2)
                            let pop_vulpob = check_float(resultado_analise[cod][anot]['socioeconomico'][11][0], 2)
                            let tx_analfab15 = check_float(resultado_analise[cod][anot]['socioeconomico'][12][0], 2)
                            let ideb_inciais = check_float(resultado_analise[cod][anot]['socioeconomico'][13][0], 1)
                            let ideb_finais = check_float(resultado_analise[cod][anot]['socioeconomico'][14][0], 1)
                            let pop_aguaenc = check_float(resultado_analise[cod][anot]['socioeconomico'][15][0], 2)
                            let pop_energel = check_float(resultado_analise[cod][anot]['socioeconomico'][16][0], 2)
                            let pop_esgadq = check_float(resultado_analise[cod][anot]['socioeconomico'][17][0], 2)
                            let pop_esgindq = check_float(resultado_analise[cod][anot]['socioeconomico'][18][0], 2)
                            let urb_vpubs = check_float(resultado_analise[cod][anot]['socioeconomico'][19][0], 2)

                            p = '<td>'
                            if (idhm) 
                                p += 'IDHM (média da região): ' + idhm + '<br>'
                            if (idhm_renda) 
                                p += 'IDHM-Renda (média da região): ' + idhm_renda + '<br>'
                            if (idhm_longv) 
                                p += 'IDHM-Longevidade (média da região): ' + idhm_longv + '<br>'
                            if (idhm_educa) 
                                p += 'IDHM-Educação (média da região): ' + idhm_educa + '<br>'
                            if (expc_vida) 
                                p += 'Expectativa de vida (média da região): ' + expc_vida + '<br>'
                            if (prob_60ans) 
                                p += 'Probabilidade de alcançar 60 anos (média da região): ' + prob_60ans + '%<br>'
                            if (exp_anestu) 
                                p += 'Expectativa de anos de estudo (média da região): ' + exp_anestu + '<br>'
                            if (renda_pc) 
                                p += 'Renda per capita: R$ ' + renda_pc + '<br>'
                            if (sal_tform) 
                                p += 'Salário trabalho formal (média da região): ' + sal_tform + '<br>'
                            if (pop_extpob) 
                                p += 'População em extrema pobreza: ' + pop_extpob + '%<br>'
                            if (pop_pobre) 
                                p += 'População em pobreza: ' + pop_pobre + '%<br>'
                            if (pop_vulpob) 
                                p += 'População em vulnerabilidade a pobreza: ' + pop_vulpob + '%<br>'
                            if (tx_analfab15) 
                                p += 'Taxa de analfabetismo com 15 anos ou mais: ' + tx_analfab15 + '%<br>'
                            if (ideb_inciais) 
                                p += 'IDEB - anos iniciais (média da região): ' + ideb_inciais + '<br>'
                            if (ideb_finais) 
                                p += 'IDEB - anos finais (média da região): ' + ideb_finais + '<br>'
                            if (pop_aguaenc) 
                                p += 'População com água encanada: ' + pop_aguaenc + '%<br>'
                            if (pop_energel) 
                                p += 'População com energia elétrica: ' + pop_energel + '%<br>'
                            if (pop_esgadq) 
                                p += 'População com esgoto sanitário adequado: ' + pop_esgadq + '%<br>'
                            if (pop_esgindq) 
                                p += 'População com esgoto sanitário inadequado: ' + pop_esgindq + '%<br>'
                            if (urb_vpubs) 
                                p += 'Urbanização nas vias públicas: ' + urb_vpubs + '%<br>'
                            p += '</td>'
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

// inserindo funções nos clicks nas opções do navbar
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
    muda_visao(0) // ToDo: alterar para 2 (provincia)
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
