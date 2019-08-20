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

// criando o elemento pra ser adicionado na frente do mapa
let overlay = new ol.Overlay({
    element: container,
    autoPan: true,
    autoPanAnimation: {
        duration: 250
    }
});