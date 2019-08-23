function check_float(res, tam){
    if (typeof res.toFixed === 'function'){
        return res.toFixed(tam)
    }
    return null
}

function jsonCopy(src) {
    return JSON.parse(JSON.stringify(src))
  }
  
let percentColors = [
    { pct: 0.0, color: { r: 0, g: 255, b: 0 } },
    { pct: 0.5, color: { r: 255, g: 255, b: 0 } },
    { pct: 1.0, color: { r: 255, g: 0, b: 0 } } ];

let getColorForPercentage = function(pct) {
    if (! isNaN(pct)){
        for (var i = 1; i < percentColors.length - 1; i++) {
            if (pct < percentColors[i].pct) {
                break;
            }
        }
        let lower = percentColors[i - 1];
        let upper = percentColors[i];
        let range = upper.pct - lower.pct;
        let rangePct = (pct - lower.pct) / range;
        let pctLower = 1 - rangePct;
        let pctUpper = rangePct;
        let color = {
            r: Math.floor(lower.color.r * pctLower + upper.color.r * pctUpper),
            g: Math.floor(lower.color.g * pctLower + upper.color.g * pctUpper),
            b: Math.floor(lower.color.b * pctLower + upper.color.b * pctUpper)
        };
        return 'rgb(' + [color.r, color.g, color.b].join(',') + ')';
    }
    return fill_mapa_color
    // or output as hex if preferred
}


// limpa dados associados no mapa
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
    muda_visao(visao)

}


// checa interação com mapa e adiciona o shape de visão
function add_shape_lmapa(vis, clickable){
    let map_src = vl_mapas.getSource()
    map_src.clear()
    map_src.addFeatures(vis);

    // limpando seleção de região
    if (select_mapa != null){
        map.removeInteraction(select_mapa);
    }
    // reiniciando a função para reconhecer click
    if (clickable){
        refresh_interaction_mapa()
    }

    overlay.setPosition(undefined);
    closer.blur();
}


// prepara dados para apresentar no mapa como uma escala de calor
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


// requisita shape de divisão do estado ao servidor e chama função de adicionar ao mapa
function requisita_visao(opc){

    let clickable = true
    $('#loader').show()
    $.ajax({
        type: 'POST',
        url: '',
        // async: false,
        data: {'visao': opc},
        success: function(response){
            visao = opc;
            let vis
            if (response){
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
                default:
                    $('#error_modal_text').append('Problema desconhecido')
                    $('#error_modal').modal('show')
                    break
                }
            } else {
                $('#error_modal_text').append('Não recebeu os dados do servidor')
                $('#error_modal').modal('show')
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
            $('#error_modal_text').append('Subdivisão do estado requisitado não é reconhecida pelo sistema')
            $('#error_modal').modal('show')
        }
    })

}


// controla o shape de subdivisão do estado de acordo com as escolhas do usuário
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

// função para adicionar títulos ao layer
function add_titulos(titulos){
    if (titulos == -1){
        $('#error_modal_text').append('Nenhum título foi encontrado')
        $('#error_modal').modal('show')
    }
    else {

        // map.removeInteraction(select);
        let src_titulos = vl_titulos.getSource()
        src_titulos.clear()
        src_titulos.addFeatures((new ol.format.GeoJSON()).readFeatures(titulos))
        // criando um layer para adicionar o shape do titulos retornados

        // map.addLayer(vl_titulos)
        // refresh_interaction_mapa()
    }
}

// função para checar qual sistema viário está ativo no mapa e requisitar se necessário ou desativar
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


// adiciona o shape do sistema viário no mapa e a respectiva legenda
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
            $('#error_modal_text').append('Sistema viário selecionado é desconhecido pelo sistema')
            $('#error_modal').modal('show')

    }
}


// requisitará ao servidor o shape do sistema viário selecionado pelo usuário
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
            $('#error_modal_text').append('Sistema viário selecionado é desconhecido pelo sistema')
            $('#error_modal').modal('show')
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
                    $('#error_modal_text').append('Dados não foram encontrados')
                    $('#error_modal').modal('show')
                }
                $('#loader').hide()
            },
            error: function (data) {
                $('#error_modal_text').append('Problema no servidor')
                $('#error_modal').modal('show')
            }
        })
    }

    return null
}


function refresh_interaction_mapa(){
    if (select_mapa != null){
        map.removeInteraction(select_mapa)
        selected = []
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
    
}

// função para checar campos de ano inicial e ano final
function check_ano_i2ano_f(id_ano_i, id_ano_f){
    let obj_ano_i = document.getElementById(id_ano_i)
    let obj_ano_f = document.getElementById(id_ano_f)
    let ano_i = parseInt(obj_ano_i.options[obj_ano_i.selectedIndex].value)
    let ano_f = parseInt(obj_ano_f.options[obj_ano_f.selectedIndex].value)
    return ano_i > ano_f
}

$('#error_modal').on('hidden.bs.modal', function(){
    $('#error_modal_text').empty()
})