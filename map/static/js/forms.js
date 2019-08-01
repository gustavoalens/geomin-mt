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