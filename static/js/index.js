// let vis_meso = null
// let vis_meso_res = null
// let vis_micro = null
// let vis_micro_res = null
//  let vis_prov = null
// let vis_muni = null
// let vis_muni_res = null

// let nomes_sisvs = ['Rodovias', 'Ferrovias', 'Hidrovias', 'Aerodromos']
// let rodovias = null
// let ferrovias = null
// let hidrovias = null
// let aerodromos = null

// let temporal = null
////## Funções auxiliares dos botões de controle ##////



function limpa_results(){
    dados_apr = null
    resultado_analise = null
    visao_return = null
    pesquisado_analise = null
    titulos = null
    substratos_regiao = null
    form_selecionado = null
    temporal = null
    $('#pop_graf').hide()
    vl_titulos.getSource().clear()
    $('#legenda').hide()
    $('#btn_graf').removeClass('btn-down')
    $('#btn_graf').addClass('btn-up')
    // if (vis_meso) {
    //     vis_meso_res = jsonCopy(vis_meso)
    // }
    // if (vis_micro) {
    //     vis_micro_res = jsonCopy(vis_micro)
    // }
    // // add provincias
    //
    // if (vis_muni) {
    //     vis_muni_res = jsonCopy(vis_muni)
    // }
    muda_visao(visao)



}

function add_shape_lmapa(vis, clickable){
    let map_src = vl_mapas.getSource()
    map_src.clear()
    map_src.addFeatures(vis);

    // limpando seleção de região
    if (select_mapa != null){
        map.removeInteraction(select_mapa);
    }
    // reiniciando a função para reconhecer click
    if (true){
        refresh_interaction_mapa()
        // select_poly(lMapa);
    }

    overlay.setPosition(undefined);
    closer.blur();
}

function organiza_dados_apr(vis) {
    if (dados_apr.max && dados_apr.min){
        $("#legenda_tit")[0].innerHTML = dados_apr.var
        $("#legenda_mx")[0].innerHTML = check_float(dados_apr.max, 3)
        $("#legenda_mn")[0].innerHTML = check_float(dados_apr.min, 3)
        $("#legenda_md")[0].innerHTML = check_float(((dados_apr.max + dados_apr.min) / 2), 3)
        $('#legenda').show() // Adicionando a legenda na tela

        let denom = (dados_apr.max - dados_apr.min)
        for (var i in vis) {
            let cod = vis[i].values_['pk']
            vis[i].values_.data = dados_apr.result[cod]
            if (vis[i] == 'nan'){
                vis[i].values_.data_nm = null
            } else {
                vis[i].values_.data_nm = (dados_apr.result[cod] - dados_apr.min) / denom
            }
        }
    }
    return vis
}

function requisita_visao(opc){

    let clickable = true
    $('#loader').show()
    $.ajax({ //REFAZER MODO DE PESQUISA
        type: 'POST',
        url: '',
        // async: false,
        data: {'visao': opc},
        success: function(response){
            visao = opc;
            let vis
            switch (opc) {
                case 0: // caso selecionado Mesorregião
                    vis_meso = new ol.format.GeoJSON().readFeatures(response)
                    vis_meso_res = new ol.format.GeoJSON().readFeatures(response)
                    vis = vis_meso_res
                    break;
                case 1: // caso selecionado Microrregião
                    vis_micro = new ol.format.GeoJSON().readFeatures(response)
                    vis_micro_res = new ol.format.GeoJSON().readFeatures(response)
                    vis = vis_micro_res
                    break;
                case 2: // caso selecionado Província
                    vis_meso = new ol.format.GeoJSON().readFeatures(response)
                    vis_meso_res = new ol.format.GeoJSON().readFeatures(response)
                    vis = vis_meso_res
                    break;
                case 3: // caso selecionado Municípios
                    vis_muni = new ol.format.GeoJSON().readFeatures(response)
                    vis_muni_res = new ol.format.GeoJSON().readFeatures(response)
                    vis = vis_muni_res
                    break;
                }


            if (dados_apr && visao_return == opc){ // caso haja resultado a ser inserido no shape
                // adicionando o título da pesquisa e os valores máximo, médio e mínimo na legenda
                vis = organiza_dados_apr(vis)

                clickable = false
            }

            // adicionando no layer e liberando o sistema
            add_shape_lmapa(vis, clickable)
            $('#loader').hide()

        },
        // xhrFields: {
        //     onprogress: function (e){ // Função para computador progresso
        //         console.log(e)
        //         // $('#loader').show()
        //         var data = e.currentTarget.response;
        //
        //         if (data.lastIndexOf('|') >= 0) {
        //             var val2 = data.slice((data.lastIndexOf('|') + 1));
        //             var val = val2.split("-");
        //             var numProgressGeral = parseFloat(val[1]);
        //             var numProgressAtual = parseFloat(val[0]);
        //             console.log(numProgressGeral)
        //
        //             // progressBarGeral.width(numProgressGeral + '%').text(numProgressGeral + '%');
        //             // progressBarAtual.width(numProgressAtual + '%').text(numProgressAtual + '%');
        //         }
        //     }
        // },
        error: function (data) {
            console.log('erro')
        }
    })

}

// função que reconhecerá qual foi clicado e alterar a feature que está em tela
function muda_visao(opc){
    let map_src = vl_mapas.getSource()
    map_src.clear() // limpando o vetor do mapa
    let vis = null // variável auxiliar que salvará as features do shape selecionado
    let clickable = true
    visao = opc; // atualizando variavel global de controle de visao
    $('#nv-vis_mac').removeClass('active')
    $('#nv-vis_mic').removeClass('active')
    $('#nv-vis_pro').removeClass('active')
    $('#nv-vis_mun').removeClass('active')


    switch (opc) {
        case 0: // caso selecionado Mesorregião
            // vis = vis_meso
            $('#nv-vis_mac').addClass('active')
            if (vis_meso_res){
                vis = vis_meso_res
            }
            else if (!vis_meso){
                requisita_visao(opc)
            }
            else {
                vis = vis_meso
            }
            break;
        case 1: // caso selecionado Microrregião
            // vis = vis_micro
            $('#nv-vis_mic').addClass('active')
            if (vis_micro_res){
                vis = vis_micro_res
            }
            else if (!vis_micro){
                requisita_visao(opc)
            }
            else {
                vis = vis_micro
            }
            break;
        case 2: // caso selecionado Província
        $('#nv-vis_pro').addClass('active')
            if (vis_meso_res){
                vis = vis_meso_res
            }
            else if (!vis_meso){
                requisita_visao(opc)
            }
            else {
                vis = vis_meso //adicionar shape certo
            }
            break;
        case 3: // caso selecionado Municípios
            $('#nv-vis_mun').addClass('active')
            if (vis_muni_res){
                vis = vis_muni_res
            }
            else if (!vis_muni){
                requisita_visao(opc)
            }
            else {
                vis = vis_muni
            }
            break;
    }
    // adicionando novo shape ao layer de vetor
    if (vis){
        if (dados_apr && visao_return == opc){ // caso haja resultado a ser inserido no shape
            clickable = false
        }
        add_shape_lmapa(vis, clickable)

    }
}

function requisita_shp_via(sisv) {
    let data = null
    switch (sisv) {
        case 0:
            if (!rodovias){
                data = 'rodovias'
            }
            else {
                return rodovias
            }
            break;
        case 1:
            if (!ferrovias){
                data = 'ferrovias'
            }
            else {
                return ferrovias
            }
            break;
        case 2:
            if (!hidrovias){
                data = 'hidrovias'
            }
            else {
                return hidrovias
            }
            break;

        case 3:
            if (!aerodromos){
                data = 'aerodromos'
            }
            else {
                return aerodromos
            }
            break;
        default:
            console.log('ERRO')
    }

    if (data) {
        $('#loader').show()
        $.ajax({
            type: 'POST',
            url: '',
            // async: false,
            data: {sis_viario: data},
            success: function(response){
                if (response) {
                    addmap_via((new ol.format.GeoJSON()).readFeatures(response), sisv)
                }
                else {
                    // apresentar erro
                    console.log('errão')
                }
                $('#loader').hide()
            },
            error: function (data) {
                console.log('erro')
            }
        })
    }

    return null
}


// função para checar se o vetor de rodovias está ativo ou não no mapa
function check_sisviario(sisv) {

    $('#nv-via_rodo').removeClass('active')
    $('#nv-via_ferro').removeClass('active')
    $('#nv-via_hidro').removeClass('active')
    $('#nv-via_aero').removeClass('active')

    let sr_sisvias = vl_sisvias.getSource()
    let legenda_via = $('#legenda_via')
    if (sr_sisvias.getFeatures().length > 0){
        $('#btn_' + nomes_sisvs[sis_viario]).removeClass('selected')
        sr_sisvias.clear()
        legenda_via.hide()
    }

    if (sisv == null || sisv == sis_viario) {
        sis_viario = null
        legenda_via.hide()
    }
    else if (!sis_viario || sisv != sis_viario){
        let shp_viario = requisita_shp_via(sisv)

        if (shp_viario){
            addmap_via(shp_viario, sisv)
        }
        legenda_via.show()
    }

}

function addmap_via(shp, sisv) {
    sis_viario = sisv
    vl_sisvias.getSource().addFeatures(shp)
    $('#btn_' + nomes_sisvs[sisv]).addClass('selected')

    let titulo_leg = $('#legenda_via_tit')
    let div_leg_via = $('#legenda_via_itens')

    div_leg_via.empty()

    function add_linha_legenda(stroke, legenda, is_line) {
        let rep_item = new XMLHttpRequest()
        if (is_line) {
            rep_item.open('GET', 'static/imagens/line2.html', true)
        }
        else {
            rep_item.open('GET', 'static/imagens/point.html', true)
        }
        rep_item.onreadystatechange = function(){
            if (rep_item.status == 200 && rep_item.readyState == 4){
                let svg = rep_item.responseText

                for (let l in legenda){
                    let l_nome = legenda[l]
                    let div_item = document.createElement('div')
                    div_item.id = `leg_rodovia_${l}`
                    div_item.className = 'row leg_via-item'

                    let div_line = document.createElement('div')
                    div_line.className = 'col-md-3'
                    div_line.innerHTML = svg
                        .replace(/__prefix__/g, l)
                        .replace(/__fill__/g, stroke[l_nome])

                    let div_nome = document.createElement('div')
                    div_nome.className = 'col-md-9 leg_via-txt'
                    div_nome.innerHTML = l_nome

                    div_item.appendChild(div_line)
                    div_item.appendChild(div_nome)

                    div_leg_via.append(div_item)

                }
            }
        }
        rep_item.send(null)
    }


    switch (sis_viario) {
        case 0:
            $('#nv-via_rodo').addClass('active')
            titulo_leg.html('Rodovias')
            add_linha_legenda(stroke_rodovias, legenda_rodovias, true)

            break;

        case 1:
            $('#nv-via_ferro').addClass('active')
            titulo_leg.html('Ferrovias')
            add_linha_legenda(stroke_ferrovias, legenda_ferrovias, true)
            break;

        case 2:
            $('#nv-via_hidro').addClass('active')
            titulo_leg.html('Hidrovias')
            add_linha_legenda(stroke_hidrovias, legenda_hidrovias, true)
            break;

        case 3:
            $('#nv-via_aero').addClass('active')
            titulo_leg.html('Aerodromos - Situação da pista')
            add_linha_legenda(stroke_aerodromos, legenda_aerodromos, false)
            break;
        default:
            console.log('ué')

    }
}







////## Adicionando botões de controle ##////
// let visao = 0;
let visao = 0
let sis_viario = null
// window.app = {}
// var app = window.app
// app.Visoes = function(opt_options) {

//     // reutiliza o campo de opções ou cria um vazio
//     var options = opt_options || {};

//     // div geral para os botões de controle próprios
//     var div = document.createElement('div')

//     // criando div onde ficarão os botões (Macrorregiões, Microrregiões, Províncias, Munícipios)
//     // var gr_visoes = document.createElement('div');
//     // gr_visoes.className = 'visoes';
//     // gr_visoes.role = 'group';

//     // // criando os botões dentro da div
//     // var nomes_vis = ['Macrorregiões', 'Microrregiões', 'Províncias', 'Municípios'];
//     // for (var i = 0; i < 4; i++){
//     //     var bt = document.createElement('button');
//     //     bt.className = 'btn'; // classe de css
//     //     bt.innerHTML = nomes_vis[i]; // nome apresentado na tela
//     //     const t = i; // valor para distinguir botão (opção) clicado
//     //     bt.addEventListener('click', function(){muda_visao(t)}, false);
//     //     // bt.addEventListener('touchstart', function(){muda_visao(t)}, false);
//     //     gr_visoes.appendChild(bt); // adicionado na div
//     // }

//     // div onde ficará o botão Rodovias
//     var gr_rodo = document.createElement('div')
//     gr_rodo.className = 'viario'

//     // criando o botão rodovias

//     for (let s in nomes_sisvs){
//         let bt = document.createElement('button')
//         bt.id = 'btn_' + nomes_sisvs[s]
//         bt.className = 'btn'
//         bt.innerHTML = nomes_sisvs[s]
//         const ts = parseInt(s)
//         // adicionando funções ao click
//         bt.addEventListener('click', function(){check_sisviario(ts)}, false)
//         // bt_rodv.addEventListener('touchstart', function(){check_sisviario()}, false)
//         gr_rodo.appendChild(bt) // add o botão a sua respectiva div
//     }

//     // adicionando as divs na geral
//     // div.appendChild(gr_visoes)
//     div.appendChild(gr_rodo)


//     // acrescentando a div no mapa
//     ol.control.Control.call(this, {
//         element: div,
//         target: options.target
//     })

// };
// // acrescentando a função de criar e manipular os botões de fato nos controles do mapa
// ol.inherits(app.Visoes, ol.control.Control);




////# Constante de cores e tamanhos p/ styles #////
// ToDo: add cores do cluster caso for manter
const stroke_mapa_color = '#2489b7'
const stroke_mapa_result_color = '#000'
const stroke_road_color = '#E27FA3'
const stroke_titulo = '#1e1e1e'
const stroke_rodovias = {
    'Duplicada': '#c91414',
    'Em obras de duplicao': '#ee5656',
    'Em obras de implantao': '#f0df6d',
    'Em obras de pavimentao': '#475053',
    'Implantada': '#bba513',
    'Leito Natural': '#693309',
    'Pavimentada': '#191c1d',
    'Planejada': '#095769',
}
const stroke_ferrovias = {
    'Ferrovia em Trafego': '#c91414',
    'Ferrovia Planejada': '#bba513',
    'Ferrovia em Projeto': '#693309',
}
const stroke_hidrovias = {
    'Trecho de Navegação Inexpressível': '#c91414',
    'Trecho Navegável nas Cheias': '#bba513',
    'Trecho Navegável Principal': '#693309',
}

const stroke_aerodromos = {
    'Areia': '#c91414',
    'Argila': '#ee5656',
    'Asfalto Ou Concreto Asfl': '#f0df6d',
    'Cascalho': '#475053',
    'Grama': '#bba513',
    'Piarra': '#693309',
    'Saibro': '#191c1d',
    'Terra': '#095769',
}

const fill_titulo = 'rgba(255, 255, 255, 0)'
const fill_mapa_color = 'rgba(230, 230, 230, 0.2)'
const fill_mapa_selected_color = 'rgba(50, 50, 50, 0.3)'
const fill_cluster_color = '#3399CC'

const fill_text_lightbackg = '#000'
const fill_text_darkbackg = '#fff'

const width_bordas = 1
const width_btitulos = 1.5


const legenda_rodovias = {
    0: 'Duplicada',
    1: 'Em obras de duplicao',
    2: 'Em obras de implantao',
    3: 'Em obras de pavimentao',
    4: 'Implantada',
    5: 'Leito Natural',
    6: 'Pavimentada',
    7: 'Planejada',
}

const legenda_ferrovias = {
    0: 'Ferrovia em Trafego',
    1: 'Ferrovia Planejada',
    2: 'Ferrovia em Projeto',
}
const legenda_hidrovias = {
    0: 'Trecho de Navegação Inexpressível',
    1: 'Trecho Navegável nas Cheias',
    2: 'Trecho Navegável Principal',
}

const legenda_aerodromos = {
    0: 'Areia',
    1: 'Argila',
    2: 'Asfalto Ou Concreto Asfl',
    3: 'Cascalho',
    4: 'Grama',
    5: 'Piarra',
    6: 'Saibro',
    7: 'Terra',
}

////# Styles #////

// style dos features de titulos
var titulos_style = new ol.style.Style({
    fill: new ol.style.Fill({
        color: fill_titulo,
    }),
    stroke: new ol.style.Stroke({
        color: stroke_titulo,
        width: width_btitulos
    }),

})

// Style auxiliar para fundo do mapa (quando GET vazio ou região sem dado)
var style_mapa = new ol.style.Style({
    fill: new ol.style.Fill({
        color: fill_mapa_color
    }),
    stroke: new ol.style.Stroke({
        color: stroke_mapa_color,
        width: width_bordas
    }),
});




// Style para layer do vetor do mapa das regiões
var styleRegioes = function(feature) {
    var style
    if (dados_apr){ // check se foi requisitado pesquisa de variável p/ apresentar

        if (dados_apr.max && feature.get('data')){ // check se existem realmente dados retornados
        style = new ol.style.Style({
            fill: new ol.style.Fill({
                // calcula a cor pelo dado normalizado
                color: getColorForPercentage(feature.get('data_nm'))
            }),
            stroke: new ol.style.Stroke({
                color: stroke_mapa_result_color,
                width: width_bordas,
            }),
            text: new ol.style.Text({
                text: check_float(feature.get('data'), 2),
                // text: feature.values_.features[0].values_.data.toFixed(2).toString(),
                fill: new ol.style.Fill({
                    color: fill_text_lightbackg
                })
            }),
        })
        }
        else{
            style = style_mapa
        }
    }
    else {
        style = style_mapa
    }

    return style
}


// Style para layer de rodovias
var style_sisvias = function(feature) {

    function get_color_v() {
        let clr = stroke_road_color
        switch (sis_viario) {
            case 0:
                clr = stroke_rodovias[feature.values_.tipo_pavimento] || stroke_road_color
                break
            case 1:
                clr = stroke_ferrovias[feature.values_.situacao] || stroke_road_color
                break
            case 2:
                clr = stroke_hidrovias[feature.values_.situacao] || stroke_road_color
                break
            case 3:
                clr = stroke_aerodromos[feature.values_.pavimento] || stroke_road_color
                break
        }

        return clr
    }

    let style
    if (sis_viario != 3){
        style = new ol.style.Style({
            stroke: new ol.style.Stroke({
                color: get_color_v(),
                width: 3
            })
        })
    } else {
        style = new ol.style.Style({
            image: new ol.style.Circle({
                radius: 5,
                fill: new ol.style.Fill({
                    color: get_color_v()
                })
            })
        })
    }
    return style;
}



// Style para layer de cluster (resultado em "discos" para variaveis)
var style_cluster = function(feature) {
    var style = new ol.style.Style({
        image: new ol.style.Circle({
            radius: (feature.get('data_nm') + 1.2) * 20, //calculo extra apenas para aumentar tamanho dos discos
            // stroke: new ol.style.Stroke({
            //     color: stroke_mapa_color
            // }),
            fill: new ol.style.Fill({
                color: fill_cluster_color
            }),

        }),
        text: new ol.style.Text({
            text: feature.get('data').toFixed(2).toString(),
            // text: feature.values_.features[0].values_.data.toFixed(2).toString(),
            fill: new ol.style.Fill({
                color: fill_text_darkbackg
            })
        })
    })
    return style
}


// Style para adicionar efeito de seleção à região clicada
var style_select = new ol.style.Style({
    fill: new ol.style.Fill({
        color: fill_mapa_selected_color
    }),
    stroke: new ol.style.Stroke({
        color: stroke_mapa_color,
        width: 1
    }),
    // text: new ol.style.Text()
});


////# Constantes dos names das layers #////
const lVias = 'viarios'
const lViasPontos = 'vpontos'
const lMapa = 'mapa'
const lTitulos = 'titulos'
const lCluster = 'cluster'

////# Pop-ups #////

//# Pop-ups ligados ao mapa #//

// associando o popup do html no js
var container = document.getElementById('popup');
var content = document.getElementById('popup-content');
var closer = document.getElementById('popup-closer');

// criando o elemento pra ser adicionado na frente do mapa
var overlay = new ol.Overlay({
    element: container,
    autoPan: true,
    autoPanAnimation: {
        duration: 250
    }
});

// handler para esconder o popup
closer.onclick = function() {
    overlay.setPosition(undefined);
    closer.blur();
    return false;
};


//# Pop-ups com posição fixa #//
$('#legenda').hide()





////# Layers #////

// Layer para adicionar linhas de sistemas viarios
var vl_sisvias = new ol.layer.Vector({
    renderMode: 'image',
    source: new ol.source.Vector({
        projection: 'EPSG:4326',
        // features: (new ol.format.GeoJSON()).readFeatures(rodovias_mt) // Inicia sem features
    }),
    style: style_sisvias,
    name: lVias,
    zIndex: 100,
})

//  Layer para adicionar pontos de sistemas viarios
let vl_svpontos = new ol.layer.Vector({
    renderMode: 'image',
    source: new ol.source.Vector({
        projection: 'EPSG: 4326'
    }),
    // style: style_svpontos,
    name: lViasPontos,
    zIndex: 150,
})

// Layer dos titulos
var vl_titulos = new ol.layer.Vector({
    renderMode: 'image',
    source: new ol.source.Vector({
        projection: 'EPSG:4326',
        // features: (new ol.format.GeoJSON()).readFeatures(titulos)

    }),

    style: titulos_style,

    name: lTitulos,

    zIndex: 500,
})


// Layer das regiões
var vl_mapas = new ol.layer.Vector({
    renderMode: 'image',
    source: new ol.source.Vector({
        projection: 'EPSG:4326',

        // features: (new ol.format.GeoJSON()).readFeatures(vis_meso)

    }),
    style: styleRegioes,   
    name: lMapa,
    zIndex: 200,
})

// volta a visão para que foi utilizada antes de alguma iteração com as pesquisas
if (visao_return){
    visao = visao_return
}

muda_visao(visao)


// Layer para apresentar resultados de variáveis em "discos"
var vl_cluster = new ol.layer.Vector({
    source: new ol.source.Vector(),
    style: style_cluster,
    name: lCluster,
    zIndex: 300,
})




////# MAPA #////
var map = new ol.Map({
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






let pk_click = null
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
var select = null; // objeto da interação Select
var selected; // objeto que irá conter o vetor com os ids das regiões selecionadas
var i = 0;

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

let select_mapa
function refresh_interaction_mapa(){
    if (select_mapa != null){
        map.removeInteraction(select_mapa)
    }
    select_mapa = new ol.interaction.Select({
        layers: function(layer){
            if (layer.get('name') == lMapa || layer.get('name') == lTitulos) {
                layer.setZIndex(layer.getZIndex() + 2)
                return true
            }
        },
        filter: function(feature, layer) { //filtro para layer correta para efeito
            if (layer.get('name') == lMapa || layer.get('name') == lTitulos) return true
        },
        style: style_select,
    });
    map.addInteraction(select_mapa);
    select_mapa.on('select', function(e){
        selected = e.target.getFeatures().getArray();
    })

    console.log(map.getInteractions())
    
}
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


////## caso retorne de uma analise por variavel (apresentar) ##////
// if (dados_apr){
//
//     if (dados_apr.max){
//         map.removeInteraction(select);
//         let vis; // variável auxiliar que salvará as features do shape selecionado
//         // var nm_cod
//         switch (visao_return) {
//             case 0: // caso selecionado Mesorregião
//                 // if (!vis_meso){
//                 //     vis_meso = requisita_visao()
//                 // }
//                 while(!vis_meso){
//                     console.log(vis_meso)
//                 }
//                 vis = jsonCopy(vis_meso)
//                 // nm_cod = 'cd_geocme'
//                 break;
//             case 1: // caso selecionado Microrregião
//                 // if (!vis_micro){
//                 //     vis_micro = requisita_visao()
//                 // }
//                 vis = jsonCopy(vis_micro)
//                 // nm_cod = 'cd_geocmi'
//                 break;
//             case 2: // caso selecionado Província
//                 // if (!vis_meso){
//                 //     vis_meso = requisita_visao()
//                 // }
//                 vis = jsonCopy(vis_meso) //adicionar shape certo
//                 // nm_cod = 'cd_geocme'
//                 break;
//             case 3: // caso selecionado Municípios
//                 // if (!vis_muni){
//                 //     vis_muni = requisita_visao()
//                 // }
//                 vis = jsonCopy(vis_muni)
//                 // nm_cod = 'cd_geocmu'
//                 break;
//             default:
//                 vis = jsonCopy(vis_meso)
//         }
//
//         // adicionando o título da pesquisa e os valores máximo, médio e mínimo na legenda
//         $("#legenda_tit")[0].innerHTML = dados_apr.var
//         $("#legenda_mx")[0].innerHTML = dados_apr.max.toFixed(2).toString()
//         $("#legenda_mn")[0].innerHTML = dados_apr.min.toFixed(2).toString()
//         $("#legenda_md")[0].innerHTML = ((dados_apr.max + dados_apr.min) / 2).toFixed(2).toString()
//
//         let denom = (dados_apr.max - dados_apr.min)
//         vis = new ol.format.GeoJSON().readFeatures(vis)
//
//         for (var i in vis) {
//             let cod = vis[i].values_['pk']
//             vis[i].values_.data = dados_apr.result[cod]
//             vis[i].values_.data_nm = (dados_apr.result[cod] - dados_apr.min) / denom
//             // #caso for manter os discos também, linha abaixo pega os centroids das regiões# //
//             // vis.features[i].geometry = turf.centroid(vis.features[i]).geometry
//         }
//
//         // #acrescentando o shape com pontos das regiões e valores dos dados para gerar o cluster# //
//         // vl_cluster.getSource().addFeatures((new ol.format.GeoJSON()).readFeatures(vis))
//
//         // limpando o layer do mapa para acrescentar o novo mapa pintado
//         let map_src = vl_mapas.getSource()
//         map_src.clear()
//         map_src.addFeatures(vis)
//         $('#legenda').show() // Adicionando a legenda na tela
//     }
// }










////# Controle dos formulários de pesquisa #////


// apresentar formulário conforme selecionado pelo usuário
$('#btn_dados').click(function(){
    $('#btn_dados').removeClass('selected');
    $('#btn_titulos').removeClass('selected');
    $('#btn_analisar').removeClass('selected');
    $('#btn_dados').addClass('selected');

    $('#formTitulo').hide();
    $('#formAnalisar').hide();
    $('#formDados').show();

    // checagem se algum campo já foi selecionado anteriormente (GET)
    check_dm();
    check_ec();
    check_sc();
    check_ar();
})
$('#btn_titulos').click(function(){
    $('#btn_dados').removeClass('selected');
    $('#btn_titulos').removeClass('selected');
    $('#btn_analisar').removeClass('selected');
    $('#btn_titulos').addClass('selected');

    $('#formDados').hide();
    $('#formAnalisar').hide();
    $('#formTitulo').show();
})

$('#btn_analisar').click(function(){
    $('#btn_dados').removeClass('selected');
    $('#btn_titulos').removeClass('selected');
    $('#btn_analisar').removeClass('selected');
    $('#btn_analisar').addClass('selected');

    $('#formDados').hide();
    $('#formTitulo').hide();
    $('#formAnalisar').show();

    // checagem se algum campo já foi selecionado anteriormente (GET)
    check_tipo_analise()

})


// ## CONTROLE DE CADA FORM ## //
////## FORM DOWNLOAD ##////

// função para checar se campo Arrecadação foi marcado
function check_ar(){
    if ($('#id_ar').is(':checked')){
        $('#arrecadacao').show();
        check_ar_taxa();
    } else {
        $('#arrecadacao').hide();
    }
}

// onClick do campo Arrecadação
$('#id_ar').click(function(){
    check_ar();
});

// função para checar se campo Socioeconômico foi marcado
function check_sc(){
    if ($('#id_sc').is(':checked')){
        $('#socioeconomico').show();
        check_sc_opc();
    } else {
        $('#socioeconomico').hide();
    }
}

// função para checar as opções do campo Socioeconômico foram marcados
function check_sc_opc(){
    if ($('#id_sc_todos').is(':checked')){
        $('#socioeconomico_opc').hide();
    } else {
        $('#socioeconomico_opc').show();
    }
}

// onClick do campo Socioeconômico
$('#id_sc').click(function(){
    check_sc();
});

// onClick do campo Todos dentro de Socioeconômico
$('#id_sc_todos').click(function(){
    check_sc_opc();
});


// função para checar se campo Economia foi marcado
function check_ec(){
    if ($('#id_ec').is(':checked')){
        $('#economico').show();
        check_ec_opc();
    } else {
        $('#economico').hide();
    }
}

// função para checar as opções do campo Economia foram marcados
function check_ec_opc() {
    if ($('#id_ec_todos').is(':checked')) {
        $('#economico_opc').hide();
    } else {
        $('#economico_opc').show();
    }
}

// onClick do campo Economia
$('#id_ec').click(function() {
    check_ec();
});

// onClick do campo Todos dentro de Economia
$('#id_ec_todos').click(function() {
    check_ec_opc();
});


// função para checar se campo Demográfico foi marcado
function check_dm() {
    if ($('#id_dm').is(':checked')) {
        $('#demografico').show();
        check_dm_opc();
    } else {
        $('#demografico').hide();
    }
}

// função para checar as opções do campo Demográfico foram marcados
function check_dm_opc( ){
    if ($('#id_dm_pop_total').is(':checked')) {
        $('#demografico_opc').hide();
    } else {
        $('#demografico_opc').show();
    }
}

// onClick do campo Demográfico
$('#id_dm').click(function() {
    check_dm();
});

// onClick do campo Todos dentro de Demográfico
$('#id_dm_pop_total').click(function() {
    check_dm_opc();
});



////## FORM TITULO ##////

function check_tit_num_proc(){
    if ($('#id_pesq_num_ano').is(':checked')){
        $('#tit_num_proc').show()
        $('#tit_sub_uso').hide()
        $('#tit_pf_pj').hide()
        $('#id_pesq_pf_pj').prop('checked', false)
    } else {
        $('#tit_num_proc').hide()
        $('#tit_sub_uso').show()
    }
}

function check_pessoa(){
    if ($('#id_pesq_pf_pj').is(':checked')){
        $('#tit_pf_pj').show()
        $('#tit_sub_uso').show()
        $('#tit_num_proc').hide()
        $('#id_pesq_num_ano').prop('checked', false)
    } else {
        $('#tit_pf_pj').hide()
    }
}

function check_pf_pj(){
    if ($('#id_pes_1').is(':checked')){
        $('#div_id_pessoa_juridica').hide()
        $('#div_id_pessoa_fisica').show()
    } else if ($('#id_pes_2').is(':checked')){
        $('#div_id_pessoa_fisica').hide()
        $('#div_id_pessoa_juridica').show()
    } else {
        $('#div_id_pessoa_fisica').hide()
        $('#div_id_pessoa_juridica').hide()
    }
}

check_tit_num_proc()
check_pf_pj()

// iniciando campo de numero de processo como vazio

if ($('#id_numero')[0].value == '0') {
    $('#id_numero')[0].value = ''
}

// acrescentando onclick nos radiobuttons para definir se pesquisa pf ou pj

$('#id_pesq_num_ano').click(function(){
    check_tit_num_proc()
});

$('#id_pesq_pf_pj').click(function(){
    check_pessoa()
})

$('#id_pes_1').click(function(){
    check_pf_pj()
});

$('#id_pes_2').click(function(){
    check_pf_pj()
});


////## FORM ANALISAR ##////

function check_tipo_analise(){
    if ($('#id_tipo_analise_1').is(':checked')) {
        $('#analisar_cruzar').hide();
        $('#analisar_apresentar').hide();
        $('#analisar_temporal').hide();
    }
    else if ($('#id_tipo_analise_2').is(':checked')) {
        $('#analisar_apresentar').hide();
        $('#analisar_temporal').hide();
        $('#analisar_cruzar').show();
    }
    else if ($('#id_tipo_analise_3').is(':checked')) {
        $('#analisar_cruzar').hide();
        $('#analisar_temporal').hide();
        $('#analisar_apresentar').show();
    }
    else if ($('#id_tipo_analise_4').is(':checked')) {
        $('#analisar_cruzar').hide();
        $('#analisar_apresentar').hide();
        $('#analisar_temporal').show();
    }
}


$('#id_tipo_analise_1').click(function() {
    check_tipo_analise()
});

$('#id_tipo_analise_2').click(function() {
    check_tipo_analise()
});

$('#id_tipo_analise_3').click(function() {
    check_tipo_analise()
});

$('#id_tipo_analise_4').click(function() {
    check_tipo_analise()
});

// $('#id_variavel').addEventListener('change', function(){
//     console.log($('#id_variavel').value)
// })

// function check_variavel(opc){
//     console.log(opc)
//     switch ($('#id_variavel').val()) {
//         case '0':
//             $('#analisar_apr_opcs_arr').hide()
//             $('#analisar_apr_subs').hide()
//             $('#analisar_apr_ano').hide()
//             break;
//
//         case '1':
//             $('#analisar_apr_opcs_arr').show()
//             $('#analisar_apr_ano').show()
//             if ($('#id_opc_arr_2').is(':checked')){
//                 $('#analisar_apr_subs').show()
//             } else {
//                 $('#analisar_apr_subs').hide()
//             }
//             break;
//
//         case '2':
//             $('#analisar_apr_opcs_arr').hide()
//             $('#analisar_apr_subs').show()
//             $('#analisar_apr_ano').show()
//             break;
//
//         case '3':
//             $('#analisar_apr_opcs_arr').show()
//             $('#analisar_apr_ano').hide()
//             if ($('#id_opc_arr_2').is(':checked')){
//                 $('#analisar_apr_subs').show()
//             } else {
//                 $('#analisar_apr_subs').hide()
//             }
//             break;
//
//         default:
//             $('#analisar_apr_opcs_arr').hide()
//             $('#analisar_apr_subs').hide()
//             $('#analisar_apr_ano').show()
//             break;
//     }
// }


function check_variavel(opc='apr', idx=''){
    let id = 'id_variavel'
    let id_opc1 = 'id_opc_arr_1'
    let id_opc2 = 'id_opc_arr_2'
    if (opc == 'temp'){
        id = `id_fvars-${idx}-vars`
        id_opc1 = `${id_opc1}-${opc}${idx}`
        id_opc2 = `${id_opc2}-${opc}${idx}`
    }
    switch ($(`#${id}`).val()) {
        case '0':
            $(`#analisar_${opc}_opcs_arr${idx}`).hide()
            $(`#analisar_${opc}_subs${idx}`).hide()
            if (opc == 'apr') {
                $(`#analisar_${opc}_ano`).hide()
            }
            break;

        case '1':
            $(`#analisar_${opc}_opcs_arr${idx}`).show()
            $(`#analisar_${opc}_ano`).show()

            if ($(`#${id_opc2}`).is(':checked')){
                $(`#analisar_${opc}_subs${idx}`).show()
            } else {
                $(`#analisar_${opc}_subs${idx}`).hide()
            }
            break;

        case '2':
            $(`#analisar_${opc}_opcs_arr${idx}`).hide()
            $(`#analisar_${opc}_subs${idx}`).show()
            if (opc == 'apr') {
                $(`#analisar_${opc}_ano`).show()
            }
            break;

        case '3':
            $(`#analisar_${opc}_opcs_arr${idx}`).show()
            if (opc == 'apr') {
                $(`#analisar_${opc}_ano`).hide()
            }
            if ($(`#${id_opc2}`).is(':checked')){
                $(`#analisar_${opc}_subs${idx}`).show()
            } else {
                $(`#analisar_${opc}_subs${idx}`).hide()
            }
            break;

        default:
            $(`#analisar_${opc}_opcs_arr${idx}`).hide()
            $(`#analisar_${opc}_subs${idx}`).hide()
            if (opc == 'apr') {
            $(`#analisar_${opc}_ano`).show()
            }
            break;
    }
}


$('#add_var').click(function(){

    add_opc_titulos('var')
})

check_variavel('apr')
check_variavel('temp')

$('#id_variavel').change(function(){
    check_variavel()
    // console.log($('#id_variavel :selected').text())
})

////////////////// AQUI TAMBÉM |||||||||||||||||||||||
$('#id_opc_arr_1').click(function(){
    $('#analisar_apr_subs').hide()
})

$('#id_opc_arr_2').click(function(){
    $('#analisar_apr_subs').show()
})




function add_opc_titulos(varv){
    let fmset = varv + 's'
    let tag = 'f' + fmset

    let form_idx = $(`#id_${tag}-TOTAL_FORMS`).val()
    let empf = $(`#empty_formset_${fmset}`)
    $(`#formset_${fmset}`).append(empf.html()
        .replace(`name="${tag}-__prefix__-${fmset}"`, `name="${tag}-${varv}"`)
        .replace(`name="${tag}-__prefix__-rep"`, `name="${tag}-rep"`)
        .replace(/__prefix__/g, form_idx)
        .replace(`rm_${varv}`, `rm_${varv}` + form_idx)
        .replace(/"id_opc_arr_1"/g, `"id_opc_arr_1-temp${form_idx}"`)
        .replace(/"id_opc_arr_2"/g, `"id_opc_arr_2-temp${form_idx}"`)
        .replace(/name="opc_arr"/g, `name="opc_arr-temp${form_idx}"`)
        .replace(/subs_ap/g, `subs-temp${form_idx}`)
    )
	$(`#id_${tag}-TOTAL_FORMS`).val(parseInt(form_idx) + 1)

    $(`#rm_${varv}` + form_idx).click(function(){
        $(`#box_${tag}`+ form_idx).remove()

        let form_tot = $(`#id_${tag}-TOTAL_FORMS`)
        form_tot.val(parseInt(form_tot.val()) - 1)
    })


    if (varv == 'var'){
        const idx = form_idx.toString()
        $(`#id_fvars-${form_idx}-vars`).change(function(){
            check_variavel('temp', idx)
        })

        $(`[name=opc_arr-temp${idx}]`).click(function(){
            check_variavel('temp', idx)
        })
    }


    // console.log($('#id_fvars-0-vars option[value="3"]').remove())
}


$('#add_sub').click(function(){

    add_opc_titulos('sub')
})



$('#add_uso').click(function(){

    add_opc_titulos('uso')
})

function organiza_subs_usos(name){
    let org = []
    $(`[name=${name}]`).each(function(){
        let val = $(this).val()
        if (!org.includes(val)){
            org.push(val)
        }
    })
    return org
}

// ## SUBMITS ## //
//# SUBMIT FORM TITULO #//
$('#fTitulo').submit(function(eventObj) {

    event.preventDefault()

    var ids = []; // lista dos ids das regiões selecionadas

    // verifica se alguma região foi selecionada
    if (typeof selected !== 'undefined' && selected.length) {

        // percorre o vetor de regiões selecionadas
        for (var s in selected) {
            ids.push(selected[s].values_.pk)
        }
    }

    document.getElementById('ids_tit').value = ids.toString();
    document.getElementById('visao_tit').value = visao.toString();


    let subs = organiza_subs_usos('fsubs-sub') // checando e listando subs adicionado p pesquisa
    let usos = organiza_subs_usos('fusos-uso') // checando e listando usos adicionado p pesquisa
    subs = '&subs=' + subs.toString() // preparando para inserir no form corrigido
    usos = '&usos=' + usos.toString() // preparando para inserir no form corrigido

    let data = $('#fTitulo').serialize().replace(/&fsubs-sub/g, '') + subs + usos // retirando fsubs e fusos do form e adiciona lista de ambos

    $(".loader").css("display", "block");
    // nesse caso tem problema o name
    $.ajax({
        type: 'GET',
        url: '',
        data: data,
        success: function(response){
            limpa_results()
            titulos = response
            add_titulos(titulos)
            $(".loader").css("display", "none");
        },

        error: function(error){
            $(".loader").css("display", "none");
            console.log('veio pra ca')
            console.log(error)
        },
    })
});




////## SUBMIT FORM DOWNLOAD ##////
$('#fDownload').submit(function(eventObj) {
    var ids = []; // lista dos ids das regiões selecionadas
    event.preventDefault()
    // verifica se alguma região foi selecionada
    if (typeof selected !== 'undefined' && selected.length) {

        // percorre o vetor de regiões selecionadas
        for (var s in selected) {

            // 0-Mesorregiões; 1-Microrregiões; 2-Províncias; 3-Munícipios
            switch (visao) {
                case 0:
                    ids.push(selected[s].values_.cd_geocme);
                    break;
                case 1:
                    ids.push(selected[s].values_.cd_geocmi);
                    break;
                case 2:
                    ids.push(selected[s].values_.cd_geoprv);
                    break;
                case 3:
                    ids.push(selected[s].values_.cd_geocmu);
                    break;
                default:
                    ids.push(-1);

            }
        }
    }

    // adicionando os valores nos campos hidden para o método GET
    document.getElementById('ids').value = ids.toString();
    document.getElementById('visao').value = visao.toString();
    $(".loader").css("display", "block");

    $.ajax({
        type: 'GET',
        url: '',
        data: $('#fDownload').serialize(),
        content_type: 'text/csv',
        success: function(response, status, xhr) {


            let filename
            let disposition = xhr.getResponseHeader('Content-Disposition')
            if (disposition && disposition.indexOf('attachment') !== -1) {
                var filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
                var matches = filenameRegex.exec(disposition);
                if (matches != null && matches[1]) {
                    filename = matches[1].replace(/['"]/g, '');
                }
            }

            let type = xhr.getResponseHeader('Content-Type')
            let blob = new File([response], filename, {type: type})
            let URL = window.URL || window.webkitURL
            let dUrl = URL.createObjectURL(blob)



            let a = document.createElement('a')
            a.id = 'download_csv'
            a.download = filename
            a.href = dUrl
            document.body.appendChild(a)
            a.click()
            URL.revokeObjectURL(dUrl)
            $('#download_csv').remove()

            $(".loader").css("display", "none");
        },
        error: function(xhr, text, error) {
            console.log(error)
            console.log(xhr)
        }
    })
});


let tipos_rep = null

//# SUBMIT FORM ANALISE #//
$('#fAnalisar').submit(function(eventObj) {
    event.preventDefault()
    document.getElementById('visao_an').value = visao.toString();
    // $(".loader").css("display", "block");

    // let vars = organiza_subs_usos('fvars-var') // checando e listando subs adicionado p pesquisa

    let vars = []
    $('[name=fvars-var]').each(function(){
        vars.push($(this).val())
    })
    vars = '&vars=' + vars.toString() // preparando para inserir no form corrigido

    let tp = {0: 'line', 1: 'bar'}
    tipos_rep = []
    $('[name=fvars-rep]').each(function(){
        tipos_rep.push($(this).val())
    })

    let series = {}
    for (let i in tipos_rep){
        series[i] = {type: tp[tipos_rep[i]]}
    }
    tipos_rep = series


    let data = $('#fAnalisar').serialize().replace(/&fvars-vars/g, '') + vars // retirando fsubs e fusos do form e adiciona lista de ambos

    if (true) {
        $(".loader").css("display", "block");
        $.ajax({
            type: 'GET',
            url: '',
            data: data,
            success: function(response) {
                limpa_results()
                visao_return = parseInt(response['visao'])
                delete response.visao

                if (response['substratos_regiao']) {
                    delete response.substratos_regiao
                    substratos_regiao = response
                }

                else if (response['resultado_analise']) {
                    pesquisado_analise = response.resultado_analise
                    delete response.resultado_analise
                    resultado_analise = response

                }

                else if (response['dados_apr']) {
                    delete response.dados_apr
                    dados_apr = response
                    let vis
                    switch (visao_return) {
                        case 0: // caso selecionado Mesorregião
                            vis = vis_meso_res
                            break;
                        case 1: // caso selecionado Microrregião
                            vis = vis_micro_res
                            break;
                        case 2: // caso selecionado Província
                            vis = vis_meso_res
                            break;
                        case 3: // caso selecionado Municípios
                            vis = vis_muni_res
                            break;
                        }


                    vis = organiza_dados_apr(vis)
                    muda_visao(visao)
                }

                else if (response['temporal']) {
                    temporal = response['temporal']
                    $('#pop_graf').show()
                    google.charts.load('current', {packages: ['corechart']});


                }


                $(".loader").css("display", "none");
            },
            error: function(xhr, text, error){
                console.log(xhr)
                console.log('Erro: ' + error)
                $(".loader").css("display", "none");
            }
        })
    }

    // return true;
});


function drawChart() {
    // ToDo: checar antes se aba já está aberta
    $('#graficos').collapse('show')
    let title = null

    function get_nome(regiao) {
        for (let r in regiao){
            if (regiao[r].values_.pk == pk_click){
                return regiao[r].values_.nome
            }
        }
        return null
    }
    if (visao == 0){
        title = 'MESORREGIÃO ' + get_nome(vis_meso)
    }
    else if (visao == 1) {
        title = 'MICRORREGIÃO ' + get_nome(vis_micro)
    }
    else if (visao == 2) {
        title = 'PROVÍNCIA ' + get_nome(vis_meso) // mudar para provincia
    }
    else if (visao == 3) {
        title = 'MUNICÍPIO ' + get_nome(vis_muni)
    }

    // let series = {}
    // for (let i in tipos_rep){
    //     console.log(tipos_rep[i])
    //     series[i] = {type: tp[tipos_rep[i]]}
    // }



    let data = google.visualization.arrayToDataTable(temporal[visao][pk_click]);

    let options = {
        title : title || 'Pesquisa',
        subtitle: 'Variáveis escolhidas',
        vAxis: {
            title: 'Valor',
            logScale: true
        },
        hAxis: {title: 'Ano'},
        seriesType: 'bars',
        series: tipos_rep,
        chartArea: {width: '65%'}
    }

    let chart = new google.visualization.ComboChart(document.getElementById('grafico_'));
    chart.draw(data, options);
}

function drawChart_uf() {
    // ToDo: checar antes se aba já está aberta
    $('#graficos').collapse('show')
    var data = google.visualization.arrayToDataTable(temporal[4][0]);

        var options = {
            title : 'MATO-GROSSO',
            subtitle: 'Variáveis escolhidas',
            vAxis: {
                title: 'Valor',
                logScale: true
            },
            hAxis: {title: 'Ano'},
            seriesType: 'bars',
            series: tipos_rep,
            chartArea: {width: '65%'}
        }

        var chart = new google.visualization.ComboChart(document.getElementById('grafico_uf'));
        chart.draw(data, options);
}

$('#graficos').on('shown.bs.collapse', function(){
    let btn = $('#btn_graf')
    btn.removeClass('btn-up')
    btn.addClass('btn-down')
})

$('#graficos').on('hidden.bs.collapse', function(){
    let btn = $('#btn_graf')
    btn.removeClass('btn-down')
    btn.addClass('btn-up')
})


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

// function check_btn_graf(){
//     let btn = $('#btn_graf')
//     if (btn.hasClass('btn-up')){
//         btn.removeClass('btn-up')
//         btn.addClass('btn-down')
//     }
//     else {
//         btn.removeClass('btn-down')
//         btn.addClass('btn-up')
//     }
// }
// $('#btn_graf').click(function(){
//     check_btn_graf()
// })


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








////# FUNÇÕES AUXILIARES #////

// function check_float(res, tam){
//     if (typeof res.toFixed === 'function'){
//         return res.toFixed(tam)
//     }
//     return res
// }

// function jsonCopy(src) {
//   return JSON.parse(JSON.stringify(src))
// }

// var percentColors = [
//     { pct: 0.0, color: { r: 0, g: 255, b: 0 } },
//     { pct: 0.5, color: { r: 255, g: 255, b: 0 } },
//     { pct: 1.0, color: { r: 255, g: 0, b: 0 } } ];

// var getColorForPercentage = function(pct) {
//     if (! isNaN(pct)){
//         for (var i = 1; i < percentColors.length - 1; i++) {
//             if (pct < percentColors[i].pct) {
//                 break;
//             }
//         }
//         var lower = percentColors[i - 1];
//         var upper = percentColors[i];
//         var range = upper.pct - lower.pct;
//         var rangePct = (pct - lower.pct) / range;
//         var pctLower = 1 - rangePct;
//         var pctUpper = rangePct;
//         var color = {
//             r: Math.floor(lower.color.r * pctLower + upper.color.r * pctUpper),
//             g: Math.floor(lower.color.g * pctLower + upper.color.g * pctUpper),
//             b: Math.floor(lower.color.b * pctLower + upper.color.b * pctUpper)
//         };
//         return 'rgb(' + [color.r, color.g, color.b].join(',') + ')';
//     }
//     return fill_mapa_color
//     // or output as hex if preferred
// }

// window.teste1 = 'teste'
// var teste1 = 'teste'

// loader.css('display', 'none')

// let div = $('#line_img').load('static/imagens/line.html')

// document.getElementById('line_img').addEventListener('load', function(){
//     let svg = this.getSVGDocument()
//     // let svg = div.children('#svg_line')
//     console.log(svg)
// })

// console.log(div)
// console.log($('#svg_line'))





// document.getElementById('svg1').addEventListener('load', function(){
//     console.log(document.getElementById('path816'))
//     console.log($('#path816'))
//     let doc = this.getSVGDocument()
//     console.log(doc)
//     let rect = doc.querySelector('path')
//     console.log(rect)
//     rect.setAttribute('fill', '#693309')
//     let svg = doc.querySelector('svg')
//     svg.setAttribute('fill', '#693309')
//     console.log(svg)
// })


// carregar api charts
// google.charts.load('current', {packages: ['corechart']});
// google.charts.setOnLoadCallback(drawChart); // callback da função de desenhar o gráfico
//
// function drawChart() {
//     var data = google.visualization.arrayToDataTable([
//           ['Month', 'Bolivia', 'Ecuador', 'Madagascar', 'Papua New Guinea', 'Rwanda', 'Average'],
//           ['2004/05',  165,      938,         522,             998,           450,      614.6],
//           ['2005/06',  135,      1120,        599,             1268,          288,      682],
//           ['2006/07',  157,      null,        587,             807,           397,      623],
//           ['2007/08',  139,      1110,        615,             968,           215,      609.4],
//           ['2008/09',  136,      691,         629,             1026,          366,      569.6]
//         ]);
//
//         var options = {
//           title : 'Monthly Coffee Production by Country',
//           vAxis: {title: 'Cups'},
//           hAxis: {title: 'Month'},
//           seriesType: 'bars',
//           series: {5: {type: 'line'}}
//         };
//
//         var chart = new google.visualization.ComboChart(document.getElementById('grafico_'));
//         chart.draw(data, options);
// }
// att
