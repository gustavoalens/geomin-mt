# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
# from django.views import View
# from django.views.generic.edit import FormView

from django.core.serializers import serialize
from django.template import Context
from django.db.models import Sum, Avg, Max, Min, Func, Value,\
    ExpressionWrapper, F, IntegerField, FloatField, CharField, Subquery, OuterRef
from django.contrib.postgres.aggregates import ArrayAgg
from django.contrib.gis.db.models import Union

# from django.db.models import Q  # para utilizar or e and nos filters

from .models import cidades, mesorregioes, microrregioes, demografico, economia, \
    socioeconomico, arrecadacao, pessoa_fisica, pessoa_juridica, titulos_minerarios, \
    cfem, tah, rodovias, ferrovias, hidrovias, aerodromos

from map.forms import FormConsulta, FormTitulo, FormAnalisar, FormsetSubs
from map import constantes as ct
from map import queries as qr

import json
import numpy as np
import pandas as pd
import re
import sys

class Object(object):
    pass

# Create your views here.


# Filtragem dos campos selecionados para resultante do query
def q_campos(query, keys_bd, keys_rq, dict_bd):
    """
    """
    inters = set(keys_bd).intersection(keys_rq)
    if inters:
        values = []
        for nome in inters:
            values.append(dict_bd[nome])
        return query.values(*values, ct.cid_id, 'ano')

    return None


# Adicionado o alias dos campos categoricos
def valores_catg(df):
    """
    """
    cols = set(list(df.columns)).intersection(ct.d_choices.keys())
    for c in cols:
        df[c].fillna(0, inplace=True)
        df[c] = df[c].map(lambda i: ct.d_choices[c][i])


class NanConverter(json.JSONEncoder):
    def default(self, obj):
        try:
            _ = iter(obj)
        except TypeError:
            if isinstance(obj, float) and np.isnan(obj):
                return "null"
        return json.JSONEncoder.default(self, obj)


@csrf_exempt
def index(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """

    # Instancias inicias
    form_dados = None
    form_titulos = None
    form_analise = None
    form_subs = None
    reg_dados = None
    visao = None
    reg_subs = None
    titulos = None
    form_selecionado = None
    dados_apr = None

    if request.method == 'GET':

        form_dados = FormConsulta(request.GET or None)
        form_titulos = FormTitulo(request.GET or None)
        form_analise = FormAnalisar(request.GET or None)
        form_subs = FormsetSubs(request.GET or None)

        if 'check' in request.GET.keys():
            form_selecionado = int(request.GET['check'])

            visao = int(request.GET['visao']) # tipo de região que foi selecionada (0: Meso, 1: Micro, 2: Prov, 3: Cid)

            ## caso form de Dados for chamado ##
            if form_selecionado == 0:
                print('Entrou form Dados')
                dm = ec = sc = ar = None
                df_dm = df_ec = df_sc = df_ar = None
                dfs = list()
                # Recebendo os parametros passados pelo método GET
                ids_selecionados = request.GET['ids'] # código das regiões selecionadas
                anos = list(range(int(request.GET['ano_i']), int(request.GET['ano_f']) + 1))
                keys = list(request.GET.keys()) # listagem de todos os parametros passados

                # filtrar as cidade dependendo da visão
                if not ids_selecionados: # quando não é selecionada nenhuma região, buscar todas as cidades do estado
                    print('Buscando todas cidades do estado')
                    ids_regiao = None

                else:
                    print('Buscando cidades da região selecionada')
                    ids_regiao = list(map(int, ids.split(',')))

                # cid_aux (dict) auxiliar para acrescentar nome da cidade na tabela
                # re_ci (list) irá salvar uma lista de ids das cidades contidas na região
                re_ci, cid_aux = getCidades(ids_regiao, visao)

                # checando os campos selecionados para pesquisa
                if 'dm' in request.GET: # caso Demográfico esteja marcado
                    dm = demografico.objects.filter(ano__in=anos)
                    if re_ci:
                        dm = dm.filter(cidade__id__in=re_ci)

                    # verifica se o campo 'todos' foi marcado
                    if 'dm_pop_total' in request.GET:
                        res = list(dm.values())
                        if res:
                            df_dm = pd.DataFrame(res)
                            df_dm['populacao_total'] = df_dm['populacao_urbana'] + df_dm['populacao_rural']
                        else:
                            pass

                    # busca pelos campos marcados
                    else:
                        dm = q_campos(dm, list(ct.d_bd_dm.keys()), keys, ct.d_bd_dm)
                        if dm:
                            df_dm = pd.DataFrame(list(dm))
                        else:
                            print('Nenhum campo marcado')

                    if df_dm is not None:
                        dfs.append(df_dm) # acrescentando na lista de todas tabelas selecionadas

                if 'ec' in request.GET: # caso Econômico esteja marcado
                    ec = economia.objects.filter(ano__in=anos)
                    if re_ci:
                        ec = ec.filter(cidade__id__in=re_ci)

                    # verifica se o campo 'todos' foi marcado
                    if 'ec_todos' in request.GET:
                        res = list(ec.values())
                        if res:
                            df_ec = pd.DataFrame(res)
                        else:
                            pass

                    # busca pelos campos marcados
                    else:
                        ec = q_campos(ec, list(ct.d_bd_ec.keys()), keys, ct.d_bd_ec)
                        if ec:
                            df_ec = pd.DataFrame(list(ec))
                        else:
                            print('Nenhum campo marcado')

                    if df_ec is not None:
                        dfs.append(df_ec) # acrescentando na lista de todas tabelas selecionadas

                if 'sc' in request.GET: # caso Socioeconômico esteja marcado
                    sc = socioeconomico.objects.filter(ano__in=anos)
                    if re_ci:
                        sc = sc.filter(cidade__id__in=re_ci)

                    # verificar se o campo 'todos' foi marcado
                    if 'sc_todos' in request.GET:
                        res = list(sc.values())
                        if res:
                            df_sc = pd.DataFrame(res)
                        else:
                            pass

                    # busca pelos campos marcados
                    else:
                        sc = q_campos(sc, list(ct.d_bd_sc.keys()), keys, ct.d_bd_sc)
                        if sc:
                            df_sc = pd.DataFrame(list(sc))
                        else:
                            print('Nenhum campo marcado')

                    if df_sc is not None:
                        dfs.append(df_sc) # acrescentando na lista de todas tabelas selecionadas

                if 'ar' in request.GET: # caso Arrecadação esteja marcado
                    # ar = arrecadacao.objects.filter(ano__in=anos)
                    # if re_ci:
                    #     ar = ar.filter(cidade__id__in=re_ci)

                    ar = cfem.objects.filter(ano__in=anos)
                    if re_ci:
                        ar = ar.filter(cidade__id__in=re_ci)
                    subs = int(request.GET['ar_subs'])
                    if subs != 0:
                        ar = ar.filter(subs=subs)

                    if ar:
                        pf = list()
                        pj = list()
                        for a in ar:
                            pf.append(str(a.pessoa_fisica))
                            pj.append(str(a.pessoa_juridica))
                        df_ar = pd.DataFrame(list(ar.values()))
                        df_ar.drop(columns=['titulos_minerarios_id'], inplace=True)
                        df_ar.rename(columns={'pessoa_fisica_id': 'pessoa_fisica', 'pessoa_juridica_id': 'pessoa_juridica'}, inplace=True)
                        df_ar['subs'] = df_ar['subs'].map(lambda s: ct.d_subs[s])
                        df_ar['unidade'] = df_ar['unidade'].map(lambda un: ct.d_un_ab[un])
                        df_ar['pessoa_fisica'] = pf
                        df_ar['pessoa_juridica'] = pj

                    else:
                        df_ar = pd.DataFrame()


                    if not df_ar.empty:
                        dfs.append(df_ar) # acrescentando na lista de todas tabelas selecionadas

                if dfs:
                    df_final = dfs[0] # objeto que será salvo a união de todas a tabelas pesquisadas
                    for df in dfs[1:]:
                        # Unindo as colunas das tabelas usando como referência o id da cidade e ano
                        df_final = pd.merge(df_final, df, how='outer', on=[ct.cid_id, 'ano'])

                    # Removendo as colunas ids geradas pelo merge dos dataframes utilizando regex
                    r = re.compile('(id)$|(id_\w)')
                    df_final.drop(columns=list(filter(r.match, list(df_final.columns))), inplace=True)

                    # Acrescentando uma coluna com os nomes das cidades de acordo com seus códigos
                    if not cid_aux: # caso não tenha sido selecionada nenhuma região
                        cid_aux = dict(list(cidades.objects.all().values_list('id', 'nome')))
                    df_final['nome_cidade'] = df_final[ct.cid_id].map(lambda i: cid_aux[i].title())

                    # busca se existe colunas categoricas e as transforma pelo nome
                    valores_catg(df_final)
                    df_final.sort_values('ano', inplace=True)

                    # disponibilizar para download - ToDo: colocar em um botão na janela em que serão apresentados os resultados
                    response = HttpResponse(content_type='text/csv')
                    response['Content-Disposition'] = 'attachment; filename=results.csv'
                    df_final.to_csv(path_or_buf=response, index=False, sep=';', decimal=',')
                    return response

                else: # retornar erro
                    print('Nenhuma busca')

            ## caso form de Títulos for chamado ##
            if form_selecionado == 1:
                print('-'*30)
                print('Entrou Form Titulo')
                print(request.GET.keys())
                print('-'*30)

                ids = request.GET['ids_tit'] # código das regiões selecionadas

                cids = cidades.objects.filter(geom__intersects=OuterRef('geom'))
                # primeira filtragem por numero/ano do processo ou buscar pela região
                if 'pesq_num_ano' in request.GET: #ToDO: filtrar se está correto o numero
                    num = request.GET['numero']
                    ano = request.GET['ano']
                    titulos = titulos_minerarios.objects.filter(numero=num, ano=ano)


                else:
                    # Filtrar as cidade dependendo da visão
                    if not ids: # quando não é selecionada nenhuma região, buscar todas as cidades do estado
                        print('Buscando todos os titulos do estado')
                        reg = mesorregioes.objects.aggregate(Union('geom'))

                    else:
                        print('Buscando os titulos das regioes selecionada')
                        ids_regiao = list(map(int, ids.split(',')))

                        reg = None # auxiliar que irá conter a união da geometria das regiões selecionadas
                        if visao == ct.VIS_MESORREGIAO:
                            reg = mesorregioes.objects.filter(id__in=ids_regiao).aggregate(Union('geom'))
                        elif visao == ct.VIS_MICRORREGIAO:
                            reg = microrregioes.objects.filter(id__in=ids_regiao).aggregate(Union('geom'))
                        elif visao == ct.VIS_PROVINCIA:
                            # ToDo: Alterar para provincias
                            reg = mesorregioes.objects.filter(id__in=ids_regiao).aggregate(Union('geom'))
                        else: # caso as regiões selecionadas já sejam cidades
                            reg = cidades.objects.filter(id__in=ids_regiao).aggregate(Union('geom'))

                    # Buscando os titulos que intersectam nas regiões unidas
                    titulos = titulos_minerarios.objects.filter(geom__intersects=reg['geom__union'])


                # filtragem dos encontrados:
                # filtro por tipo de substrato
                if request.GET['subs']:
                    subs = list(map(int, request.GET['subs'].split(',')))
                    titulos = titulos.filter(subs__in=subs)

                # filtro por tipo de uso
                if request.GET['usos']:
                    usos = list(map(int, request.GET['usos'].split(',')))
                    titulos = titulos.filter(uso__in=usos)

                # filtro por pf ou pj
                # ToDo: Checar porque 'pes' não tá indo no get
                if 'pes' in request.GET:
                    if request.GET['pes'] == '1': #1 - pessoa fisca; 2 - pessoa juridica
                        pf = int(request.GET['pessoa_fisica'])
                        titulos = titulos.filter(pessoa_fisica_id = pf)
                    else:
                        pj = int(request.GET['pessoa_juridica'])
                        titulos = titulos.filter(pessoa_juridica_id = pj)


                if titulos:
                    # substituindo código por escrita do "choices"
                    for titulo in titulos:
                        titulo.subs = ct.d_subs[titulo.subs]
                        titulo.uso = ct.d_uso_tm[titulo.uso]
                        titulo.fase = ct.d_fase[titulo.fase]

                    titulos = serialize('geojson', titulos, fields=('pk', 'numero','geom', 'ano', 'fase', 'ult_evento',
                    'nome_prop', 'subs', 'uso', 'cidades'))


                else:
                    titulos = -1

                return HttpResponse(json.dumps(titulos), content_type='application/json')


            ## caso form de Análise for chamado ##
            if form_selecionado == 2:
                print('Entrou form Analisar')
                print(request.GET.keys())

                reg_dados = None
                reg = None # auxiliar que irá conter a união da geometria das regiões selecionadas

                # prepara filtro das regiões que será organizado a pesquisa
                if visao == ct.VIS_MESORREGIAO:
                    reg = mesorregioes.objects.all()
                elif visao == ct.VIS_MICRORREGIAO:
                    reg = microrregioes.objects.all()
                elif visao == ct.VIS_PROVINCIA:
                    # ToDo: Alterar para provincias
                    reg = mesorregioes.objects.all()
                else:
                    reg = cidades.objects.all()


                # buscando todos substratos (quantidade) encontrados nas respectivas regiões
                if request.GET['tipo_analise'] == '1':
                    """
                    Requisição do menu Análise - Opção: Substrato por região
                    Busca a quantidade de todos os substratos encontrados em cada região
                        na tabela cfem
                    """
                    reg_subs = dict()
                    for r in reg:
                        cids = cidades.objects.filter(geom__contained=r.geom)
                        cfm = cfem.objects.filter(cidade__in=cids)\
                            .values('subs', 'unidade')\
                            .annotate(quantidade=Sum('quantidade')).order_by('subs')

                        subs = dict()
                        for c in cfm:
                            s = ct.d_subs[c['subs']]
                            un = ct.d_un_ab[c['unidade']]
                            if s not in subs:
                                subs[s] = {un: c['quantidade']}
                            else:
                                subs[s][un] = c['quantidade']

                        reg_subs[r.id] = subs
                    reg_subs['substratos_regiao'] = True
                    reg_subs['visao'] = visao
                    return HttpResponse(json.dumps(reg_subs), content_type='application/json')

                # caso vai cruzar substrato com algum dado
                elif request.GET['tipo_analise'] == '2':
                    """
                    Requisição do menu Análise - Opção: Cruzar dados por substrato
                    Busca o substrato escolhido na tabela cfem (quantidade e valor arrecadado)
                    Seguida busca os dados de uma das tabelas (demografico, economia, socioeconomico)
                        conforme a escolha do usuário;
                    Esses dados são filtrados também por um dado intervalo de ano
                    """
                    reg_dados = dict()

                    for r in reg:
                        # iniciando dicionario de dados encontrados sobre a região
                        reg_dados[r.id] = dict()

                        # checar dados de arrecadação e produção (TAH e CFEM)
                        # filtrando titulos que intersectam com cada região
                        subs = int(request.GET['subs_cr'])
                        tit_subs = titulos_minerarios.objects.filter(geom__intersects=r.geom, subs=subs)
                        if len(tit_subs) > 0:
                            # tah
                            tah_ = tah.objects.filter(titulos_minerarios__in=tit_subs)\
                                .aggregate(valorCobrado=Sum('valorCobrado'), valorPago=Sum('valorPago'))

                            if (tah_):
                                reg_dados[r.id]['tah'] = [tah_['valorCobrado'], tah_['valorPago']]

                        # filtrando as cidades contidas em cada região p/ CFEM e demais dados
                        cid = get_cidades(r, visao)
                        # if visao != 4:
                        #     cid = cidades.objects.filter(geom__contained=r.geom)
                        # else:
                        #     cid = r

                        anos = [r for r in range(int(request.GET['ano_i']), int(request.GET['ano_f']) + 1)]
                        for ano in anos:
                            # cfem
                            cfem_ = cfem.objects.filter(cidade__in=cid, ano=ano, subs=subs)\
                                .values('unidade').annotate(quantidade=Sum('quantidade'), valor=Sum('valor')).order_by('unidade')

                            for c in cfem_:
                                if ano not in reg_dados[r.id]:
                                    reg_dados[r.id][ano] = {'cfem': dict()}
                                reg_dados[r.id][ano]['cfem'][ct.d_un_ab[c['unidade']]] = [c['quantidade'], c['valor']]



                            # checar qual "classe" de dado foi escolhida (1- Demográfico, 2- Econômico, 3- Socioeconômico)
                            if request.GET['dados'] == '1':
                                dm = demografico.objects.filter(cidade__in=cid, ano=ano)
                                dmm = demografico.objects.filter(cidade__in=cid, ano=ano)\
                                    .aggregate(pop_urbana=Sum('populacao_urbana'), pop_rural=Sum('populacao_rural'),
                                        pop_total=Sum('populacao_total'))
                                pop_ur = dmm['pop_urbana']
                                pop_ru = dmm['pop_rural']
                                pop_tot = dmm['pop_total']

                                if pop_ur and pop_ru:
                                    if ano not in reg_dados[r.id]:
                                        reg_dados[r.id][ano] = dict()
                                    reg_dados[r.id][ano]['demografico'] = [pop_ur, pop_ru, pop_tot]

                            elif request.GET['dados'] == '2':


                                # pop = demografico.objects.filter(cidade__in=cid, ano=2017).values('cidade', 'populacao_total') # pegando somente do último ano, mas melhor seria ter pro ano dos dados economicos
                                pop = demografico.objects.filter(cidade=OuterRef('cidade'))
                                # print(pop.get(cidade_id=5101258))
                                # //## TROCAR pop_ativa PARA pop_ativa_18mais ##//
                                ec = economia.objects.filter(cidade__in=cid, ano=ano)\
                                    .values('id', 'receitas', 'receitas_fontext', 'despesas', 'pop_ativa_18mais')\
                                    .annotate(
                                        pop_total=Subquery(pop.values('populacao_total')[:1]),
                                        pib=ExpressionWrapper(F('pib_pc') * F('pop_total'), output_field=FloatField()),
                                        # pop_ocupada_bruto=ExpressionWrapper(('pop_ocupada') * F('pop_total'), output_field=FloatField()),
                                        ocup_agropecuario=ExpressionWrapper((F('ocup_agropecuario') / 100) * F('pop_ativa_18mais'), output_field=FloatField()),
                                        ocup_comercio=ExpressionWrapper((F('ocup_comercio') / 100) * F('pop_ativa_18mais'), output_field=FloatField()),
                                        ocup_construcao=ExpressionWrapper((F('ocup_construcao') / 100) * F('pop_ativa_18mais'), output_field=FloatField()),
                                        ocup_mineral=ExpressionWrapper((F('ocup_mineral') / 100) * F('pop_ativa_18mais'), output_field=FloatField()),
                                        ocup_industria_utilpub=ExpressionWrapper((F('ocup_industria_utilpub') / 100) * F('pop_ativa_18mais'), output_field=FloatField()),
                                        ocup_servic=ExpressionWrapper((F('ocup_servic') / 100) * F('pop_ativa_18mais'), output_field=FloatField()),
                                        ocup_industria_transf=ExpressionWrapper((F('ocup_industria_transf') / 100) * F('pop_ativa_18mais'), output_field=FloatField()),
                                        ocup_grau_form=ExpressionWrapper((F('ocup_grau_form') / 100) * F('pop_ativa_18mais'), output_field=FloatField()),
                                        ocup_fundamental=ExpressionWrapper((F('ocup_fundamental') / 100) * F('pop_ativa_18mais'), output_field=FloatField()),
                                        ocup_medio=ExpressionWrapper((F('ocup_medio') / 100) * F('pop_ativa_18mais'), output_field=FloatField()),
                                        ocup_superior=ExpressionWrapper((F('ocup_superior') / 100) * F('pop_ativa_18mais'), output_field=FloatField()),
                                    )

                                # montar annotate com os calculos já
                                # ec = economia.objects.filter(cidade__in=cid, ano=ano)

                                if ec:
                                    if ano not in reg_dados[r.id]:
                                        reg_dados[r.id][ano] = dict()
                                    reg_dados[r.id][ano]['economico'] = [
                                        [0.0, True], [0.0, True], [0.0, True], [0.0, True], [0, True], # 0, 1, 2, 3, 4
                                        [0.0, True], [0.0, True], [0.0, True], [0.0, True], [0.0, True], # 5, 6, 7, 8
                                        [0.0, True], [0.0, True], [0.0, True], [0.0, True], [0.0, True],  # 9, 10, 11, 12
                                        [0.0, True], [0.0, True], [0.0, True], [0.0, True], [0, True] # 13, 14, 15
                                    ]
                                    pop_total = 0
                                    for e in ec:

                                        if e['pop_total'] is not None:
                                            pop_total += e['pop_total']

                                        if e['pib'] is not None and not np.isnan(e['pib']): # prop a pop
                                            reg_dados[r.id][ano]['economico'][0][0] += e['pib']
                                        else:
                                            reg_dados[r.id][ano]['economico'][0][1] = False

                                        if e['receitas_fontext'] is not None and not np.isnan(e['receitas_fontext']):
                                            reg_dados[r.id][ano]['economico'][1][0] += e['receitas_fontext']
                                        else:
                                            reg_dados[r.id][ano]['economico'][1][1] = False

                                        if e['receitas'] is not None and not np.isnan(e['receitas']):
                                            reg_dados[r.id][ano]['economico'][2][0] += e['receitas']
                                        else:
                                            reg_dados[r.id][ano]['economico'][2][1] = False

                                        if e['despesas'] is not None and not np.isnan(e['despesas']):
                                            reg_dados[r.id][ano]['economico'][3][0] += e['despesas']
                                        else:
                                            reg_dados[r.id][ano]['economico'][3][1] = False

                                        if e['pop_ativa_18mais'] is not None and not np.isnan(e['pop_ativa_18mais']):
                                            reg_dados[r.id][ano]['economico'][4][0] += e['pop_ativa_18mais']
                                        else:
                                            reg_dados[r.id][ano]['economico'][4][1] = False

                                        if e['ocup_agropecuario'] is not None and not np.isnan(e['ocup_agropecuario']): # prop a pop_ativ
                                            reg_dados[r.id][ano]['economico'][5][0] += e['ocup_agropecuario']
                                        else:
                                            reg_dados[r.id][ano]['economico'][5][1] = False

                                        if e['ocup_comercio'] is not None and not np.isnan(e['ocup_comercio']): # prop a pop_ativ
                                            reg_dados[r.id][ano]['economico'][6][0] += e['ocup_comercio']
                                        else:
                                            reg_dados[r.id][ano]['economico'][6][1] = False

                                        if e['ocup_construcao'] is not None and not np.isnan(e['ocup_construcao']): # prop a pop_ativ
                                            reg_dados[r.id][ano]['economico'][7][0] += e['ocup_construcao']
                                        else:
                                            reg_dados[r.id][ano]['economico'][7][1] = False

                                        if e['ocup_mineral'] is not None and not np.isnan(e['ocup_mineral']): # prop a pop_ativ
                                            reg_dados[r.id][ano]['economico'][8][0] += e['ocup_mineral']
                                        else:
                                            reg_dados[r.id][ano]['economico'][8][1] = False

                                        if e['ocup_industria_utilpub'] is not None and not np.isnan(e['ocup_industria_utilpub']): # prop a pop_ativ
                                            reg_dados[r.id][ano]['economico'][9][0] += e['ocup_industria_utilpub']
                                        else:
                                            reg_dados[r.id][ano]['economico'][9][1] = False

                                        if e['ocup_servic'] is not None and not np.isnan(e['ocup_servic']): # prop a pop_ativ
                                            reg_dados[r.id][ano]['economico'][10][0] += e['ocup_servic']
                                        else:
                                            reg_dados[r.id][ano]['economico'][10][1] = False

                                        if e['ocup_industria_transf'] is not None and not np.isnan(e['ocup_industria_transf']): # prop a pop_ativ
                                            reg_dados[r.id][ano]['economico'][11][0] += e['ocup_industria_transf']
                                        else:
                                            reg_dados[r.id][ano]['economico'][11][1] = False

                                        if e['ocup_grau_form'] is not None and not np.isnan(e['ocup_grau_form']): # prop a pop_ativ
                                            reg_dados[r.id][ano]['economico'][12][0] += e['ocup_grau_form']
                                        else:
                                            reg_dados[r.id][ano]['economico'][12][1] = False

                                        if e['ocup_fundamental'] is not None and not np.isnan(e['ocup_fundamental']): # prop a pop_ativ
                                            reg_dados[r.id][ano]['economico'][13][0] += e['ocup_fundamental']
                                        else:
                                            reg_dados[r.id][ano]['economico'][13][1] = False

                                        if e['ocup_medio'] is not None and not np.isnan(e['ocup_medio']): # prop a pop_ativ
                                            reg_dados[r.id][ano]['economico'][14][0] += e['ocup_medio']
                                        else:
                                            reg_dados[r.id][ano]['economico'][14][1] = False

                                        if e['ocup_superior'] is not None and not np.isnan(e['ocup_superior']): # prop a pop_ativ
                                            reg_dados[r.id][ano]['economico'][15][0] += e['ocup_superior']
                                        else:
                                            reg_dados[r.id][ano]['economico'][15][1] = False

                                        # if e['pop_ocupada'] is not None and not np.isnan(e['pop_ocupada']):
                                        #     reg_dados[r.id][ano]['economico'][16][0] += e['pop_ocupada']
                                        # else:
                                        #     reg_dados[r.id][ano]['economico'][16][1] = False

                                        # if e['pop_ocupada_bruto'] is not None and not np.isnan(e['pop_ocupada_bruto']):
                                        #     reg_dados[r.id][ano]['economico'][16][0] += e['pop_ocupada_bruto']
                                        # else:
                                        #     reg_dados[r.id][ano]['economico'][16][1] = False


                                    reg_dados[r.id][ano]['economico'][0][0] = (reg_dados[r.id][ano]['economico'][0][0] / pop_total)
                                    reg_dados[r.id][ano]['economico'][5][0] = (reg_dados[r.id][ano]['economico'][5][0] / (reg_dados[r.id][ano]['economico'][16][0] or np.nan)) * 100
                                    reg_dados[r.id][ano]['economico'][6][0] = (reg_dados[r.id][ano]['economico'][6][0] / (reg_dados[r.id][ano]['economico'][16][0] or np.nan)) * 100
                                    reg_dados[r.id][ano]['economico'][7][0] = (reg_dados[r.id][ano]['economico'][7][0] / (reg_dados[r.id][ano]['economico'][16][0] or np.nan)) * 100
                                    reg_dados[r.id][ano]['economico'][8][0] = (reg_dados[r.id][ano]['economico'][8][0] / (reg_dados[r.id][ano]['economico'][16][0] or np.nan)) * 100
                                    reg_dados[r.id][ano]['economico'][9][0] = (reg_dados[r.id][ano]['economico'][9][0] / (reg_dados[r.id][ano]['economico'][16][0] or np.nan)) * 100
                                    reg_dados[r.id][ano]['economico'][10][0] = (reg_dados[r.id][ano]['economico'][10][0] / (reg_dados[r.id][ano]['economico'][16][0] or np.nan)) * 100
                                    reg_dados[r.id][ano]['economico'][11][0] = (reg_dados[r.id][ano]['economico'][11][0] / (reg_dados[r.id][ano]['economico'][16][0] or np.nan)) * 100
                                    reg_dados[r.id][ano]['economico'][12][0] = (reg_dados[r.id][ano]['economico'][12][0] / (reg_dados[r.id][ano]['economico'][16][0] or np.nan)) * 100
                                    reg_dados[r.id][ano]['economico'][13][0] = (reg_dados[r.id][ano]['economico'][13][0] / (reg_dados[r.id][ano]['economico'][16][0] or np.nan)) * 100
                                    reg_dados[r.id][ano]['economico'][14][0] = (reg_dados[r.id][ano]['economico'][14][0] / (reg_dados[r.id][ano]['economico'][16][0] or np.nan)) * 100
                                    reg_dados[r.id][ano]['economico'][15][0] = (reg_dados[r.id][ano]['economico'][15][0] / (reg_dados[r.id][ano]['economico'][16][0] or np.nan)) * 100

                                    for aux in reg_dados[r.id][ano]['economico']:
                                        if not aux[0] or np.isnan(aux[0]):
                                            aux[0] = str(np.nan) # json.dumps não estava convertendo np.nan em str (porque não sei)
                                            # print(type(aux[0]))
                                        # print(aux)





                            elif request.GET['dados'] == '3':

                                pop = demografico.objects.filter(cidade=OuterRef('cidade'), ano=2017) # ano do registro demográfico (padronizar depois para ultimo censo)
                                sc = socioeconomico.objects.filter(cidade__in=cid, ano=ano)\
                                    .values('idhm', 'idhm_renda', 'idhm_longevidade', 'idhm_educacao',
                                        'expc_vida', 'prob_60anos', 'expc_anos_estudo18', 'salario_trab_form',
                                        'ideb_inicias', 'ideb_finais')\
                                    .annotate(
                                        pop_total=Subquery(pop.values('populacao_total')[:1]),
                                        pop_ocupada=ExpressionWrapper((F('pop_ocupada') / 100) * F('pop_total'), output_field=FloatField()),
                                        renda_pc=ExpressionWrapper((F('renda_pc') / 100) * F('pop_total'), output_field=FloatField()),
                                        prop_extr_pobre=ExpressionWrapper((F('prop_extr_pobre') / 100) * F('pop_total'), output_field=FloatField()),
                                        prop_pobre=ExpressionWrapper((F('prop_pobre') / 100) * F('pop_total'), output_field=FloatField()),
                                        prop_vuln_pobre=ExpressionWrapper((F('prop_vuln_pobre') / 100) * F('pop_total'), output_field=FloatField()),
                                        taxa_analfab_15mais=ExpressionWrapper((F('taxa_analfab_15mais') / 100) * F('pop_total'), output_field=FloatField()),
                                        perc_pop_agua_enc=ExpressionWrapper((F('perc_pop_agua_enc') / 100) * F('pop_total'), output_field=FloatField()),
                                        perc_pop_coleta_lixo=ExpressionWrapper((F('perc_pop_coleta_lixo') / 100) * F('pop_total'), output_field=FloatField()),
                                        perc_pop_eletricidade=ExpressionWrapper((F('perc_pop_eletricidade') / 100) * F('pop_total'), output_field=FloatField()),
                                        esg_sanit_adequado=ExpressionWrapper((F('esg_sanit_adequado') / 100) * F('pop_total'), output_field=FloatField()),
                                        perc_pop_esg_inadequado=ExpressionWrapper((F('perc_pop_esg_inadequado') / 100) * F('pop_total'), output_field=FloatField()),
                                        perc_urban_vias_public=ExpressionWrapper((F('perc_urban_vias_public') / 100) * F('pop_total'), output_field=FloatField()),
                                    )
                                pop_total = 0

                                if sc:
                                    if ano not in reg_dados[r.id].keys():
                                        reg_dados[r.id][ano] = dict()

                                    if 'socioeconomico' not in reg_dados[r.id][ano].keys():
                                        reg_dados[r.id][ano]['socioeconomico'] = [
                                            [0.0, True], [0.0, 0, True], [0.0, 0, True], [0.0, 0, True], [0.0, 0, True], # 0, 1, 2, 3, 4
                                            [0.0, 0, True], [0.0, 0, True], [0.0, 0, True], [0.0, True], # 5, 6, 7, 8
                                            [0.0, 0, True], [0.0, True], [0.0, True], [0.0, True],  # 9, 10, 11, 12
                                            [0.0, True], [0.0, True], [0.0, True], [0.0, True], # 13, 14, 15, 16
                                            [0.0, True], [0.0, True], [0.0, True], [0.0, True], # 17, 18, 19, 20
                                        ]

                                    for s in sc:
                                        if s['pop_total'] is not None:
                                            pop_total += s['pop_total']

                                        if s['pop_ocupada'] is not None and not np.isnan(s['pop_ocupada']):
                                            reg_dados[r.id][ano]['socioeconomico'][0][0] += s['pop_ocupada']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][0][1] = False

                                        if s['idhm'] is not None and not np.isnan(s['idhm']):
                                            reg_dados[r.id][ano]['socioeconomico'][1][0] += s['idhm']
                                            reg_dados[r.id][ano]['socioeconomico'][1][1] += 1
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][1][2] = False

                                        if s['idhm_renda'] is not None and not np.isnan(s['idhm_renda']):
                                            reg_dados[r.id][ano]['socioeconomico'][2][0] += s['idhm_renda']
                                            reg_dados[r.id][ano]['socioeconomico'][2][1] += 1
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][2][2] = False

                                        if s['idhm_longevidade'] is not None and not np.isnan(s['idhm_longevidade']):
                                            reg_dados[r.id][ano]['socioeconomico'][3][0] += s['idhm_longevidade']
                                            reg_dados[r.id][ano]['socioeconomico'][3][1] += 1
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][3][2] = False

                                        if s['idhm_educacao'] is not None and not np.isnan(s['idhm_educacao']):
                                            reg_dados[r.id][ano]['socioeconomico'][4][0] += s['idhm_educacao']
                                            reg_dados[r.id][ano]['socioeconomico'][4][1] += 1
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][4][2] = False

                                        if s['expc_vida'] is not None and not np.isnan(s['expc_vida']):
                                            reg_dados[r.id][ano]['socioeconomico'][5][0] += s['expc_vida']
                                            reg_dados[r.id][ano]['socioeconomico'][5][1] += 1
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][5][2] = False

                                        if s['prob_60anos'] is not None and not np.isnan(s['prob_60anos']):
                                            reg_dados[r.id][ano]['socioeconomico'][6][0] += s['prob_60anos']
                                            reg_dados[r.id][ano]['socioeconomico'][6][1] += 1
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][6][2] = False

                                        if s['expc_anos_estudo18'] is not None and not np.isnan(s['expc_anos_estudo18']):
                                            reg_dados[r.id][ano]['socioeconomico'][7][0] += s['expc_anos_estudo18']
                                            reg_dados[r.id][ano]['socioeconomico'][7][1] += 1
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][7][2] = False

                                        if s['renda_pc'] is not None and not np.isnan(s['renda_pc']):
                                            reg_dados[r.id][ano]['socioeconomico'][8][0] += s['renda_pc']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][8][1] = False

                                        if s['salario_trab_form'] is not None and not np.isnan(s['salario_trab_form']):
                                            reg_dados[r.id][ano]['socioeconomico'][9][0] += s['salario_trab_form']
                                            reg_dados[r.id][ano]['socioeconomico'][9][1] += 1
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][9][2] = False

                                        if s['prop_extr_pobre'] is not None and not np.isnan(s['prop_extr_pobre']):
                                            reg_dados[r.id][ano]['socioeconomico'][10][0] += s['prop_extr_pobre']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][10][1] = False

                                        if s['prop_pobre'] is not None and not np.isnan(s['prop_pobre']):
                                            reg_dados[r.id][ano]['socioeconomico'][11][0] += s['prop_pobre']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][11][1] = False

                                        if s['prop_vuln_pobre'] is not None and not np.isnan(s['prop_vuln_pobre']):
                                            reg_dados[r.id][ano]['socioeconomico'][12][0] += s['prop_vuln_pobre']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][12][1] = False

                                        if s['taxa_analfab_15mais'] is not None and not np.isnan(s['taxa_analfab_15mais']):
                                            reg_dados[r.id][ano]['socioeconomico'][13][0] += s['taxa_analfab_15mais']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][13][1] = False

                                        if s['ideb_inicias'] is not None and not np.isnan(s['ideb_inicias']):
                                            reg_dados[r.id][ano]['socioeconomico'][14][0] += s['ideb_inicias']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][14][1] = False

                                        if s['ideb_finais'] is not None and not np.isnan(s['ideb_finais']):
                                            reg_dados[r.id][ano]['socioeconomico'][15][0] += s['ideb_finais']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][15][1] = False

                                        if s['perc_pop_agua_enc'] is not None and not np.isnan(s['perc_pop_agua_enc']):
                                            reg_dados[r.id][ano]['socioeconomico'][16][0] += s['perc_pop_agua_enc']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][16][1] = False

                                        if s['perc_pop_eletricidade'] is not None and not np.isnan(s['perc_pop_eletricidade']):
                                            reg_dados[r.id][ano]['socioeconomico'][17][0] += s['perc_pop_eletricidade']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][17][1] = False

                                        if s['esg_sanit_adequado'] is not None and not np.isnan(s['esg_sanit_adequado']):
                                            reg_dados[r.id][ano]['socioeconomico'][18][0] += s['esg_sanit_adequado']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][18][1] = False

                                        if s['perc_pop_esg_inadequado'] is not None and not np.isnan(s['perc_pop_esg_inadequado']):
                                            reg_dados[r.id][ano]['socioeconomico'][19][0] += s['perc_pop_esg_inadequado']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][19][1] = False

                                        if s['perc_urban_vias_public'] is not None and not np.isnan(s['perc_urban_vias_public']):
                                            reg_dados[r.id][ano]['socioeconomico'][20][0] += s['perc_urban_vias_public']
                                        else:
                                            reg_dados[r.id][ano]['socioeconomico'][20][1] = False

                                    reg_dados[r.id][ano]['socioeconomico'][0][0] = (reg_dados[r.id][ano]['socioeconomico'][0][0] / (pop_total or np.nan)) * 100
                                    reg_dados[r.id][ano]['socioeconomico'][8][0] = (reg_dados[r.id][ano]['socioeconomico'][8][0] / (pop_total or np.nan)) * 100
                                    reg_dados[r.id][ano]['socioeconomico'][10][0] = (reg_dados[r.id][ano]['socioeconomico'][10][0] / (pop_total or np.nan)) * 100
                                    reg_dados[r.id][ano]['socioeconomico'][11][0] = (reg_dados[r.id][ano]['socioeconomico'][11][0] / (pop_total or np.nan)) * 100
                                    reg_dados[r.id][ano]['socioeconomico'][12][0] = (reg_dados[r.id][ano]['socioeconomico'][12][0] / (pop_total or np.nan)) * 100
                                    reg_dados[r.id][ano]['socioeconomico'][13][0] = (reg_dados[r.id][ano]['socioeconomico'][13][0] / (pop_total or np.nan)) * 100
                                    reg_dados[r.id][ano]['socioeconomico'][14][0] = (reg_dados[r.id][ano]['socioeconomico'][14][0] / (pop_total or np.nan)) * 100
                                    reg_dados[r.id][ano]['socioeconomico'][15][0] = (reg_dados[r.id][ano]['socioeconomico'][15][0] / (pop_total or np.nan)) * 100
                                    reg_dados[r.id][ano]['socioeconomico'][16][0] = (reg_dados[r.id][ano]['socioeconomico'][16][0] / (pop_total or np.nan)) * 100
                                    reg_dados[r.id][ano]['socioeconomico'][17][0] = (reg_dados[r.id][ano]['socioeconomico'][17][0] / (pop_total or np.nan)) * 100
                                    reg_dados[r.id][ano]['socioeconomico'][18][0] = (reg_dados[r.id][ano]['socioeconomico'][18][0] / (pop_total or np.nan)) * 100
                                    reg_dados[r.id][ano]['socioeconomico'][19][0] = (reg_dados[r.id][ano]['socioeconomico'][19][0] / (pop_total or np.nan)) * 100
                                    reg_dados[r.id][ano]['socioeconomico'][20][0] = (reg_dados[r.id][ano]['socioeconomico'][20][0] / (pop_total or np.nan)) * 100

                                    reg_dados[r.id][ano]['socioeconomico'][1] = [reg_dados[r.id][ano]['socioeconomico'][1][0] / (reg_dados[r.id][ano]['socioeconomico'][1][1] or np.nan), reg_dados[r.id][ano]['socioeconomico'][1][2]]
                                    reg_dados[r.id][ano]['socioeconomico'][2] = [reg_dados[r.id][ano]['socioeconomico'][2][0] / (reg_dados[r.id][ano]['socioeconomico'][2][1] or np.nan), reg_dados[r.id][ano]['socioeconomico'][2][2]]
                                    reg_dados[r.id][ano]['socioeconomico'][3] = [reg_dados[r.id][ano]['socioeconomico'][3][0] / (reg_dados[r.id][ano]['socioeconomico'][3][1] or np.nan), reg_dados[r.id][ano]['socioeconomico'][3][2]]
                                    reg_dados[r.id][ano]['socioeconomico'][4] = [reg_dados[r.id][ano]['socioeconomico'][4][0] / (reg_dados[r.id][ano]['socioeconomico'][4][1] or np.nan), reg_dados[r.id][ano]['socioeconomico'][4][2]]
                                    reg_dados[r.id][ano]['socioeconomico'][5] = [reg_dados[r.id][ano]['socioeconomico'][5][0] / (reg_dados[r.id][ano]['socioeconomico'][5][1] or np.nan), reg_dados[r.id][ano]['socioeconomico'][5][2]]
                                    reg_dados[r.id][ano]['socioeconomico'][6] = [reg_dados[r.id][ano]['socioeconomico'][6][0] / (reg_dados[r.id][ano]['socioeconomico'][6][1] or np.nan), reg_dados[r.id][ano]['socioeconomico'][6][2]]
                                    reg_dados[r.id][ano]['socioeconomico'][7] = [reg_dados[r.id][ano]['socioeconomico'][7][0] / (reg_dados[r.id][ano]['socioeconomico'][7][1] or np.nan), reg_dados[r.id][ano]['socioeconomico'][7][2]]
                                    reg_dados[r.id][ano]['socioeconomico'][9] = [reg_dados[r.id][ano]['socioeconomico'][9][0] / (reg_dados[r.id][ano]['socioeconomico'][9][1] or np.nan), reg_dados[r.id][ano]['socioeconomico'][9][2]]

                                    for aux in reg_dados[r.id][ano]['socioeconomico']:
                                        if not aux[0]:
                                            aux[0] = str(np.nan)
                                        elif np.isnan(aux[0]):
                                            aux[0] = str(np.nan)

                                if ano in reg_dados[r.id]:
                                    if 'cfem' in reg_dados[r.id][ano]:
                                        for aux in reg_dados[r.id][ano]['cfem']:
                                            if not aux[0]:
                                                aux[0] = str(np.nan)

                    reg_dados['visao'] = visao
                    reg_dados['resultado_analise'] = ct.d_opcs[request.GET['dados']]
                    print(json.dumps(reg_dados))

                    return HttpResponse(json.dumps(reg_dados), content_type='application/json')


                elif request.GET['tipo_analise'] == '3':
                    """
                    Requisição do menu Análise - Opção: Apresentar Mapa
                    As variáveis estão salvas por um código no arquivo de constantes
                    O calculo por tipo de variável é feita na função get_val_var
                    Organiza o resultado de forma que retorna a variavel que foi pesquisada;
                        os valores calculados em cada região de acordo com a visão de requisão;
                        os valores minimos e máximos para facilitar calculo da rampa de cor no front
                    """
                    print('Entrou analise - apresentar mapa')
                    id_var = int(request.GET['variavel'])
                    ano = None
                    if 'ano_v' in request.GET:
                        print(f'ano: {request.GET["ano_v"]}, ano_f_t: {request.GET["ano_f_t"]}')
                        ano = request.GET['ano_v']
                    reg_val = None
                    if id_var > 0:
                        extras = dict()
                        if 'opc_arr' in request.GET: # caso a variável escolhida contenha substrato específico a ser pesquisado
                            if request.GET['opc_arr'] == '2':
                                extras['subs'] = int(request.GET['subs_ap'])
                        reg_val = qr.get_val_var(3, reg, id_var, ano, visao, extras)
                        print(reg_val)
                        vals = [x for x in list(reg_val.values()) if x and x != 'nan']
                        maior = None
                        menor = None
                        if vals:
                            maior = max(vals)
                            menor = min(vals)

                        # ToDo: acrescentar ano em var para aparecer na legenda
                        dados_apr = {'var': ct.d_variaveis_pesq[id_var] + ((' - ' + ct.d_subs[int(request.GET['subs_ap'])]) if 'subs' in request.GET and id_var < 4 else ''),
                                    'result': reg_val,
                                    'max': maior, # problema ao procurar max e min em alguns dados ('>' not supported between instances of 'dict' and 'dict') update: provavelmente porque está tudo vazio
                                    'min': menor,
                                    }

                        dados_apr['visao'] = visao
                        dados_apr['dados_apr'] = True
                        return HttpResponse(json.dumps(dados_apr), content_type='application/json')

                    else: # caso nenhuma variável seja selecionada
                        pass # retornar "erro"

                elif request.GET['tipo_analise'] == '4':
                    """
                    Requisição do menu Análise - Opção: Temporal
                    As variáveis estão salvas por um código no arquivo de constantes
                    O calculo por tipo de cada variável é feita na função get_val_var
                    Procura os dados encontrados em uma período de ano de cada
                        variável selecionada pelo usuário.
                    A pesquisa é feita em todos as "visões" do estado e no estado como um todo.
                    Os dados são tabelados e organizados em listas (formato utilizado pelo google charts).

                    """
                    get = request.GET

                    vars = list(map(int, get['vars'].split(',')))

                    mt = [Object()]
                    mt[0].id = 0

                    mt[0].geom = mesorregioes.objects.aggregate(g=Union('geom'))['g']

                    vis = [
                        mesorregioes.objects.all(),
                        microrregioes.objects.all(),
                        mesorregioes.objects.all(),  # ToDo: trocar por provincia
                        cidades.objects.all(),
                        mt
                    ]

                    anos = list(range(int(get['ano_i_t']), int(get['ano_f_t'])))
                    reg_val = []
                    # for visao in range(len(vis)):
                    for visao in range(5):

                        # criar dataframe pandas, adicionar na serie cada uma variavel
                        results = dict()
                        for i in range(len(vars)):
                            var_id = vars[i]
                            extras = dict()
                            ig = f'opc_arr-temp{i}'
                            if ig in get and get[ig] == '2':
                                extras['subs'] = int(get[f'subs-temp{i}'])

                            aux = qr.get_val_var(4, vis[visao], var_id, anos, visao, extras)

                            header = f'{ct.d_variaveis_pesq[var_id]}'
                            if extras and extras['subs']:
                                header += f' - {ct.d_subs[extras["subs"]]}'

                            for k in aux:
                                aux[k] = pd.DataFrame(aux[k], columns=['Ano', header]).set_index('Ano')
                                if k not in results:
                                    results[k] = aux[k]
                                else:
                                    results[k] = results[k].join(aux[k], how='outer', on='Ano')

                        for r in results:
                            res = results[r].sort_index()
                            cols = list(res.columns)
                            res.index = res.index.astype(str)
                            res.fillna(0, inplace=True)
                            aux = list()
                            headers = ['Ano']
                            headers += list(res.columns)
                            # headers.append('Ano')
                            aux.append(headers)
                            index = res.index.values
                            values = res.values.tolist()
                            for v in range(len(values)):
                                values[v] = [index[v]] + values[v]
                                # values[v].append(index[v])
                                aux.append(values[v])

                            results[r] = aux

                        reg_val.append(results)

                    return HttpResponse(json.dumps({'temporal': reg_val}), content_type='application/json')



        else:
            # criando o formulário novamente em caso de não ter sido acrescentado corretamente

            form_dados = FormConsulta()
            form_titulos = FormTitulo()
            form_analise = FormAnalisar()


        # deletar? ##
        pesq = None
        if 'dados' in request.GET.keys():
            pesq = ct.d_opcs[request.GET['dados']]




        return render(request, 'map/index.html',
                    {
                        'form_dados': form_dados,
                        'form_titulos': form_titulos,
                        'form_analise': form_analise,
                        'titulos': json.dumps(titulos),
                        'resultado_analise': json.dumps(reg_dados),
                        'substratos_regiao': json.dumps(reg_subs),
                        'visao_return': json.dumps(visao),
                        'pesquisado_analise': json.dumps(pesq),
                        'form_selecionado': json.dumps(form_selecionado),
                        'dados_apr': json.dumps(dados_apr),
                    },
                    )



    if request.method == 'POST':

        response = None


        if 'visao' in request.POST:
            """
            Retorna o shape de diferentes divisões do estado.
            É chamado quando o usuário requisita no menu de 'visões'
            """
            vis = request.POST['visao']
            if vis == '0': #mesorregioes
                response = serialize('geojson', mesorregioes.objects.all())

            elif vis == '1': #microrregioes
                response = serialize('geojson', microrregioes.objects.all())

            elif vis == '2': #provincia - atualizar quando tiver o shape
                response = serialize('geojson', mesorregioes.objects.all())

            elif vis == '3': # municipios
                response = serialize('geojson', cidades.objects.all())
                pass



        if 'titulo_click' in request.POST:
            """
            Procurando as cidades em que o título minerario intersecta.
            É chamado quando o usuário clica pra obter mais informações de um título
            """
            pk = request.POST['titulo_click']
            tm = titulos_minerarios.objects.filter(pk=pk)
            response = list(cidades.objects.filter(geom__intersects=Subquery(tm.values('geom'))).values_list('nome', flat=True))



        if 'sis_viario' in request.POST:
            """
            Retorna o shape do sistema viário que se encontra na base dados.
            É chamado quando o usuário requisita no menu de sistemas viários
            """
            sis_viario = request.POST['sis_viario']
            if sis_viario == 'rodovias':
                shp = rodovias
                fields = ('id', 'geom', 'tipo_pavimento')
            elif sis_viario == 'ferrovias':
                shp = ferrovias
                fields = ('id', 'geom', 'situacao')
            elif sis_viario == 'hidrovias':
                shp = hidrovias
                fields = ('id', 'geom', 'situacao')
            elif sis_viario == 'aerodromos':
                shp = aerodromos
                fields = ('id', 'geom', 'pavimento')

            response = serialize('geojson', shp.objects.all(),
                fields=fields)

        return HttpResponse(json.dumps(response), content_type='application/json')

def get_cidades(reg, visao):

    if visao != 4:
        return cidades.objects.filter(geom__contained=reg.geom)

    return reg

def getCidades(ids_regiao, visao):
    # Intancias iniciais dos objetos que vão conter id das cidades da região & id e nome das cidades
    re_ci = None
    cid_aux = None

    # Caso de regiões selecionadas
    if ids_regiao:

        # Buscando e unindo a geometria das regiões selecionadas
        reg = None # auxiliar que irá conter a união da geometria das regiões selecionadas
        if visao == ct.VIS_MESORREGIAO:
            reg = mesorregioes.objects.filter(id__in=ids_regiao).aggregate(Union('geom'))
        elif visao == ct.VIS_MICRORREGIAO:
            reg = microrregioes.objects.filter(id__in=ids_regiao).aggregate(Union('geom'))
        elif visao == ct.VIS_PROVINCIA:
            # ToDo: Alterar para provincias
            reg = mesorregioes.objects.filter(id__in=ids_regiao).aggregate(Union('geom'))
        else: # caso as regiões selecionadas já sejam cidades
            re_ci = cidades.objects.filter(id__in=ids_regiao)

        # Buscando as cidades que estão contidas nas regiões unidas
        if reg:
            re_ci = cidades.objects.filter(geom__contained=reg['geom__union'])

        cid_aux = dict(list(re_ci.values_list('id', 'nome'))) # auxiliar para acrescentar nome da cidade na tabela
        re_ci = list(re_ci.values_list('id')) # objeto que irá salvar uma lista de ids das cidades contidas na região

    return re_ci, cid_aux

# class serialize_(serialize):
#     cidades = serialize.SerializerMethodField()
#
#     def get_cidades(self, obj):
#         return obj.cidades
#
