function drawChart() {
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