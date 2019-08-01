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