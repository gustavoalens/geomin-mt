from map import constantes as ct
from django.db.models import Sum, Avg, Max, Min, Func, Value,\
    ExpressionWrapper, F, Q, IntegerField, FloatField, CharField, Subquery, OuterRef,\
    Case, When
from django.contrib.postgres.aggregates import ArrayAgg
from map.models import cidades, mesorregioes, microrregioes, demografico, economia, \
    socioeconomico, arrecadacao, pessoa_fisica, pessoa_juridica, titulos_minerarios, \
    cfem, tah, rodovias

import numpy as np

def get_cidades(reg, visao):

    if visao != 3:
        return cidades.objects.filter(geom__contained=reg.geom)
    else:
        return [reg]

    return reg

def results_t4(query, var_db, fc):
    results = query.values('ano').order_by('ano')\
        .annotate(total=fc(var_db))
    return list(results.values_list('ano', 'total'))


def get_val_var(tipo, reg, id_var, anos, visao, extras=None):
    # ToDO: criar uma variavel de extras (usar dict)
    #   receber o valores extras necessários, como qual substrato caso tenha (por ora só tem substrato p isso)
    print('*'*50)
    print(f'var:{ct.d_variaveis_db[id_var]}, anos: {anos}')
    print('*'*50)

    reg_val = None
    if id_var > 0:

        var_db = ct.d_variaveis_db[id_var]
        reg_val = dict()

        for r in reg:
            # filtrando as cidades contidas em cada região p/ CFEM e demais dados
            cid = get_cidades(r, visao)
            reg_val[r.id] = dict()


            if id_var < 3: # tabela cfem

                if tipo == 3:
                    results = cfem.objects.filter(cidade__in=cid, ano=anos)
                elif tipo == 4:
                    results = cfem.objects.filter(cidade__in=cid, ano__in=anos)

                if id_var == 1:
                    if extras and extras['subs']:
                        results = results.filter(subs=int(extras['subs']))
                    # elif 'opc_arr' in request.GET and request.GET['opc_arr'] == '2': # ToDo: retirar aqui depois que atualizar Analise-Apresentar
                    #     results = results.filter(subs=int(request.GET['subs_ap']))

                    if tipo == 4:
                        # results = results.values('ano').order_by('ano')\
                        #     .annotate(total=Sum(var_db))
                        # results = list(results.values_list('ano', 'total'))
                        results = results_t4(results, var_db, Sum)
                        reg_val[r.id] = results

                    elif tipo == 3:
                        results = results.aggregate(sum=Sum(var_db))
                        reg_val[r.id] = results['sum']

                else: # quantidade por substrato. Esperar definir o que fazer
                    pass

            elif id_var == 3: # tabela tah
                # print('entrou tabela tah')
                tit_subs = titulos_minerarios.objects.filter(geom__intersects=r.geom)
                if extras and extras['subs']:
                    tit_subs = tit_subs.filter(subs=int(extras['subs']))
                # elif 'opc_arr' in request.GET and request.GET['opc_arr'] == '2':  # ToDo: retirar aqui depois que atualizar Analise-Apresentar
                #     tit_subs = tit_subs.filter(subs=int(request.GET['subs_ap']))

                results = tah.objects.filter(titulos_minerarios__in=tit_subs).aggregate(sum=Sum(var_db))
                reg_val[r.id] = results['sum']
            elif id_var < 7: # tabela demografico
                # print('entrou tabela demografico')
                if tipo == 3:
                    results = demografico.objects.filter(cidade__in=cid, ano=anos)\
                        .aggregate(sum=Sum(var_db))['sum']

                elif tipo == 4:
                    results = demografico.objects.filter(cidade__in=cid, ano__in=anos)
                    results = results_t4(results, var_db, Sum)
                reg_val[r.id] = results

            elif id_var < 28: # tabela socioeconomico
                if tipo == 3:
                    results = socioeconomico.objects.filter(cidade__in=cid, ano=anos)
                elif tipo == 4:
                    results = socioeconomico.objects.filter(cidade__in=cid, ano__in=anos)

                if id_var in ct.d_variaveis_calc['proporcao']:
                    pop = demografico.objects.filter(cidade=OuterRef('cidade'), ano=OuterRef('ano'))
                    if tipo == 3:
                        pop_tot = demografico.objects.filter(cidade__in=cid, ano=anos).aggregate(tot=Sum('populacao_total'))['tot']
                        results = (results.aggregate(
                            sm = Sum(
                                (F(var_db) / 100) * Subquery(
                                    pop.values(('populacao_total'))[:1]
                                ), output_field=FloatField()
                            )
                        ) ['sm'] / pop_tot) * 100
                    elif tipo == 4:
                        pop_total = demografico.objects.filter(cidade__in=cid, ano__in=anos)\
                            .values('ano')\
                                .annotate(populacao_total=Sum('populacao_total'))

                        pop_total = pop_total.filter(ano=OuterRef('ano'))

                        results = results.values('ano').order_by('ano')\
                            .annotate(
                                total=ExpressionWrapper(
                                    Sum(
                                        (F(var_db) / 100) * Subquery(pop.values('populacao_total')[:1]), output_field=FloatField()
                                    ) / Subquery(pop_total.values('populacao_total')[:1]), output_field=FloatField()
                                ) * 100)

                        results = list(results.values_list('ano', 'total'))

                    reg_val[r.id] = results

                elif id_var in ct.d_variaveis_calc['idhm']:
                    # ainda definir calculo e se continua #
                    if tipo == 3:
                        results = results.aggregate(avg=Avg(var_db))['avg']
                    elif tipo == 4:
                        results = results_t4(results, var_db, Avg)
                    
                    print(f'results: {results}')
                    reg_val[r.id] = results


                elif id_var in ct.d_variaveis_calc['ideb']:
                    # ainda definir calculo e se continua #
                    if tipo == 3:
                        results = results.aggregate(avg=Avg(var_db))
                        reg_val[r.id] = results['avg']
                    elif tipo == 4:
                        results = results_t4(results, var_db, Avg)
                        reg_val[r.id] = results

                    # print(reg_val[r.id])
            else: # tabela economico
                if tipo == 3:
                    results = economia.objects.filter(cidade__in=cid, ano=anos)
                elif tipo == 4:
                    results = economia.objects.filter(cidade__in=cid, ano__in=anos)
                if id_var in ct.d_variaveis_calc['soma']:
                    if tipo == 3:
                        results = results.aggregate(sum=Sum(var_db))
                        reg_val[r.id] = results['sum']
                    elif tipo == 4:
                        results = results_t4(results, var_db, Avg)
                        reg_val[r.id] = results

                elif id_var in ct.d_variaveis_calc['proporcao']:

                    if tipo == 3: # Confirmar resultados
                        results = results.aggregate(
                            total=(
                                Sum(
                                    F(var_db) * F('pop_ativa_18mais'), 
                                    output_field=FloatField()
                                )
                            ) / Sum('pop_ativa_18mais', output_field=FloatField()) * 100
                        )['total']
                    elif tipo == 4:
                        pop_atv_total = economia.objects.filter(cidade__in=cid, ano__in=anos)\
                            .values('ano')\
                                .annotate(pop_ativa_18mais=Sum('pop_ativa_18mais'))

                        pop_atv_total = pop_atv_total.filter(ano=OuterRef('ano'))
                        
                        results = results.values('ano').order_by('ano')\
                            .annotate(
                                total=
                                     ExpressionWrapper(
                                        Sum(F(var_db) * F('pop_ativa_18mais'), output_field=FloatField()) 
                                        / Subquery(pop_atv_total.values('pop_ativa_18mais')[:1]),
                                        output_field=FloatField()
                                    ) * 100
                            )
                        results = list(results.values_list('ano', 'total'))

                    reg_val[r.id] = results

                elif id_var == ct.d_variaveis_calc['pib_pc']:
                    # ainda definir calculo e se continua #
                    # calculo 1: retornar a receitas da regiao total e calcular pela quantidade demografica
                    if tipo == 3:
                        results = results.aggregate(avg=Avg(var_db))
                        reg_val[r.id] = results['avg']
                    elif tipo == 4:
                        results = results_t4(results, var_db, Avg)
                        reg_val[r.id] = results



        return reg_val


    else: # caso nenhuma variável seja selecionada
        return None
