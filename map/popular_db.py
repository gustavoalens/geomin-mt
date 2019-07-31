import re
import pandas as pd
from .models import cidades, mesorregioes, microrregioes, demografico, economia, \
    socioeconomico, arrecadacao, pessoa_fisica, pessoa_juridica, titulos_minerarios, \
    cfem, tah


# # index = 0
# # for i in range(arr['id_cidade'].count()):
# #     if not np.isnan(arr['agua_min_pot'][i]):
# #         arr2['id_cidade'].at[index] = arr['id_cidade'][i]
# #         arr2['total'].at[index] = arr['agua_min_pot'][i]
# #         arr2['tipo_taxa'].at[index] = 2
# #         arr2['atv'].at[index] = 1
# #         arr2['ano'].at[index] = 2017
# #         index += 1
# #         print(index)
# #
# #     if not np.isnan(arr['calcario'][i]):
# #         arr2['id_cidade'].at[index] = arr['id_cidade'][i]
# #         arr2['total'].at[index] = arr['calcario'][i]
# #         arr2['tipo_taxa'].at[index] = 2
# #         arr2['atv'].at[index] = 2
# #         arr2['ano'].at[index] = 2017
# #         index += 1
# #         print(index)
# #
# #     if not np.isnan(arr['calca_cal'][i]):
# #         arr2['id_cidade'].at[index] = arr['id_cidade'][i]
# #         arr2['total'].at[index] = arr['calca_cal'][i]
# #         arr2['tipo_taxa'].at[index] = 2
# #         arr2['atv'].at[index] = 3
# #         arr2['ano'].at[index] = 2017
# #         index += 1
# #         print(index)
# #
# #     if not np.isnan(arr['calc_dol'][i]):
# #         arr2['id_cidade'].at[index] = arr['id_cidade'][i]
# #         arr2['total'].at[index] = arr['calc_dol'][i]
# #         arr2['tipo_taxa'].at[index] = 2
# #         arr2['atv'].at[index] = 4
# #         arr2['ano'].at[index] = 2017
# #         index += 1
# #         print(index)
# #
# #     if not np.isnan(arr['agua_term'][i]):
# #         arr2['id_cidade'].at[index] = arr['id_cidade'][i]
# #         arr2['total'].at[index] = arr['agua_term'][i]
# #         arr2['tipo_taxa'].at[index] = 2
# #         arr2['atv'].at[index] = 5
# #         arr2['ano'].at[index] = 2017
# #         index += 1
# #         print(index)
# #
# #     if not np.isnan(arr['granito_brita'][i]):
# #         arr2['id_cidade'].at[index] = arr['id_cidade'][i]
# #         arr2['total'].at[index] = arr['granito_brita'][i]
# #         arr2['tipo_taxa'].at[index] = 2
# #         arr2['atv'].at[index] = 6
# #         arr2['ano'].at[index] = 2017
# #         index += 1
# #         print(index)
# #
# #     if not np.isnan(arr['min_manganes'][i]):
# #         arr2['id_cidade'].at[index] = arr['id_cidade'][i]
# #         arr2['total'].at[index] = arr['min_manganes'][i]
# #         arr2['tipo_taxa'].at[index] = 2
# #         arr2['atv'].at[index] = 7
# #         arr2['ano'].at[index] = 2017
# #         index += 1
# #         print(index)
# #
# #     if not np.isnan(arr['miner_ouro_ouro'][i]):
# #         arr2['id_cidade'].at[index] = arr['id_cidade'][i]
# #         arr2['total'].at[index] = arr['miner_ouro_ouro'][i]
# #         arr2['tipo_taxa'].at[index] = 2
# #         arr2['atv'].at[index] = 8
# #         arr2['ano'].at[index] = 2017
# #         index += 1
# #         print(index)
# #
# #     if not np.isnan(arr['gema_diamante'][i]):
# #         arr2['id_cidade'].at[index] = arr['id_cidade'][i]
# #         arr2['total'].at[index] = arr['gema_diamante'][i]
# #         arr2['tipo_taxa'].at[index] = 2
# #         arr2['atv'].at[index] = 9
# #         arr2['ano'].at[index] = 2017
# #         index += 1
# #         print(index)
# #
# #     if not np.isnan(arr['argila'][i]):
# #         arr2['id_cidade'].at[index] = arr['id_cidade'][i]
# #         arr2['total'].at[index] = arr['argila'][i]
# #         arr2['tipo_taxa'].at[index] = 2
# #         arr2['atv'].at[index] = 10
# #         arr2['ano'].at[index] = 2017
# #         index += 1
# #         print(index)
# #
# #     if not np.isnan(arr['areia'][i]):
# #         arr2['id_cidade'].at[index] = arr['id_cidade'][i]
# #         arr2['total'].at[index] = arr['areia'][i]
# #         arr2['tipo_taxa'].at[index] = 2
# #         arr2['atv'].at[index] = 11
# #         arr2['ano'].at[index] = 2017
# #         index += 1
# #         print(index)
# #
#
# index = 0
# for i in range(op['id_cidade'].count()):
#     if not np.isnan(op['agua_min_pot'][i]):
#         arr2['id_cidade'].at[index] = op['id_cidade'][i]
#         arr2['total'].at[index] = op['agua_min_pot'][i]
#         arr2['atv'].at[index] = 1
#         arr2['ano'].at[index] = 2017
#         arr2['qtd_emp'].at[index] = op['agua_min_pot_emp'][i]
#         index += 1
#         print(index)
#
#     if not np.isnan(op['calcario'][i]):
#         arr2['id_cidade'].at[index] = op['id_cidade'][i]
#         arr2['total'].at[index] = op['calcario'][i]
#         arr2['atv'].at[index] = 2
#         arr2['ano'].at[index] = 2017
#         arr2['qtd_emp'].at[index] = op['calcario_emp'][i]
#         index += 1
#         print(index)
#
#     if not np.isnan(op['agua_term'][i]):
#         arr2['id_cidade'].at[index] = op['id_cidade'][i]
#         arr2['total'].at[index] = op['agua_term'][i]
#         arr2['atv'].at[index] = 5
#         arr2['ano'].at[index] = 2017
#         arr2['qtd_emp'].at[index] = op['agua_term_emp'][i]
#         index += 1
#         print(index)
#
#     if not np.isnan(op['granito_brita'][i]):
#         arr2['id_cidade'].at[index] = op['id_cidade'][i]
#         arr2['total'].at[index] = op['granito_brita'][i]
#         arr2['atv'].at[index] = 6
#         arr2['ano'].at[index] = 2017
#         arr2['qtd_emp'].at[index] = op['granito_brita_emp'][i]
#         index += 1
#         print(index)
#
#     if not np.isnan(op['min_manganes'][i]):
#         arr2['id_cidade'].at[index] = op['id_cidade'][i]
#         arr2['total'].at[index] = op['min_manganes'][i]
#         arr2['atv'].at[index] = 7
#         arr2['ano'].at[index] = 2017
#         arr2['qtd_emp'].at[index] = op['min_manganes_emp'][i]
#         index += 1
#         print(index)
#
#     if not np.isnan(op['miner_ouro_ouro'][i]):
#         arr2['id_cidade'].at[index] = op['id_cidade'][i]
#         arr2['total'].at[index] = op['miner_ouro_ouro'][i]
#         arr2['atv'].at[index] = 8
#         arr2['ano'].at[index] = 2017
#         arr2['qtd_emp'].at[index] = op['miner_ouro_ouro_emp'][i]
#         index += 1
#         print(index)
#
#     if not np.isnan(op['gema_diamante'][i]):
#         arr2['id_cidade'].at[index] = op['id_cidade'][i]
#         arr2['total'].at[index] = op['gema_diamante'][i]
#         arr2['atv'].at[index] = 9
#         arr2['ano'].at[index] = 2017
#         arr2['qtd_emp'].at[index] = op['gema_diamante_emp'][i]
#         index += 1
#         print(index)
#
#     if not np.isnan(op['argila'][i]):
#         arr2['id_cidade'].at[index] = op['id_cidade'][i]
#         arr2['total'].at[index] = op['argila'][i]
#         arr2['atv'].at[index] = 10
#         arr2['ano'].at[index] = 2017
#         arr2['qtd_emp'].at[index] = op['argila_emp'][i]
#         index += 1
#         print(index)
#
#     if not np.isnan(op['areia'][i]):
#         arr2['id_cidade'].at[index] = op['id_cidade'][i]
#         arr2['total'].at[index] = op['areia'][i]
#         arr2['atv'].at[index] = 11
#         arr2['ano'].at[index] = 2017
#         arr2['qtd_emp'].at[index] = op['areia_emp'][i]
#         index += 1
#         print(index)

# utilizar Series.isin(Series) para verificar se acha o processo
# juntar todas tabelas com dados cpf/cnpj e verificar com a tabela do sigmine
# checar e pegar valores de CPF/CNPJ, nome?, cidades e substratos das tabelas DNPM
# verificar melhor forma de salvar e acrescentar ao bd
pr_s = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/sigmine_proc.csv')
pr_p = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/Alvara_de_Pesquisa.csv', encoding='iso8859_2')
pr_c = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/Cessoes_de_Direitos.csv', encoding='iso8859_2')
pr_g = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/Guia_de_Utilizacao_Autorizada.csv', encoding='iso8859_2')
pr_l = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/Licenciamento.csv', encoding='iso8859_2')
pr_rl = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/Portaria_de_Lavra.csv', encoding='iso8859_2')
pr_re = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/Registro_de_Extracao_Publicado.csv', encoding='iso8859_2')
pr_rp = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/Relatorio_de_Pesquisa_Aprovado.csv', encoding='iso8859_2')
pr_plg = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/Requerimento_de_PLG.csv', encoding='iso8859_2')
pr_rep = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/Requerimento_de_Registro_de_Extracao_Protocolizado.csv', encoding='iso8859_2')

prs = [pr_p, pr_p, pr_c, pr_g, pr_l, pr_rl, pr_re, pr_rp, pr_plg, pr_rep]
final = prs[0]
for l in prs[1:]:
    final = final.append(l, True, sort=False)

pr_s2 = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/sigmine_proc_2.csv')

final.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/uniao.csv', index=False, encoding='utf-8')

final = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/uniao.csv')
final['Superintendęncia'] = final['Superintendęncia'].map(lambda i: i[-2:], 'ignore')

mt = final[final['Superintendęncia'] == 'MT']
mt.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/uniao_mt.csv', index=False)

p = pr_s2[pr_s2['PROCESSO'].isin(mt['Processo'])]
p['CPF/CNPJ'] = p['PROCESSO'].map(lambda i: ((mt[mt['Processo'] == i]).reset_index())['CPF/CNPJ do titular'][0],
                                  'ignore')

p.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/sig_proc_cpfcnpj_notnull.csv', index=False)


def pegando_cpf(i):
    v = ((p[p['NOME'] == i]).reset_index())['CPF/CNPJ']
    if len(v):
        return v[0]

    return ''


def cpf2id(i):
    if i:
        v = fis_id[fis_id['cpf'] == i].reset_index()['id']
        if len(v):
            return int(v[0])

    return -1


def cnpj2id(i):
    if i:
        v = jur_id[jur_id['cnpj'] == i].reset_index()['id']
        if len(v):
            return int(v[0])
    return -1


pr_s2['CPF/CNPJ'] = pr_s2['NOME'].map(pegando_cpf, 'ignore')

subs_cor = {'AMETISTA': 'AMETISTA',
            'AREIA': 'AREIA',
            'AREIA LAVADA': 'AREIA LAVADA',
            'ARENITO': 'ARENITO',
            'ARGILA': 'ARGILA',
            'BASALTO': 'BASALTO',
            'BRITA DE GRANITO': 'BRITA DE GRANITO',
            'CALCEDNIA': 'CALCEDÔNIA',
            'CALCRIO': 'CALCÁRIO',
            'CALCRIO CALCTICO': 'CALCÁRIO CALCÍTICO',
            'CALCRIO DOLOMTICO': 'CALCÁRIO DOLOMÍTICO',
            'CALCRIO INDUSTRIAL': 'CALCÁRIO INDUSTRIAL',
            'CASCALHO': 'CASCALHO',
            'CASCALHO DIAMANTFERO': 'CASCALHO DIAMANTÍFERO',
            'CASSITERITA': 'CASSITERITA',
            'CAULIM': 'CAULIM',
            'CHUMBO': 'CHUMBO',
            'COBRE': 'COBRE',
            'COLUMBITA': 'COLUMBITA',
            'CONGLOMERADO': 'CONGLOMERADO',
            'DADO NO CADASTRADO': 'DADO NÃO CADASTRADO',
            'DIAMANTE': 'DIAMANTE',
            'DIAMANTE INDUSTRIAL': 'DIAMANTE INDUSTRIAL',
            'DOLOMITO': 'DOLOMITO',
            'ESTANHO': 'ESTANHO',
            'FELDSPATO': 'FELDSPATO',
            'FILITO': 'FILITO',
            'FOSFATO': 'FOSFATO',
            'GABRO': 'GABRO',
            'GALENA': 'GALENA',
            'GRANITO': 'GRANITO',
            'GRANITO ORNAMENTAL': 'GRANITO ORNAMENTAL',
            'GUA MINERAL': 'ÁGUA MINERAL',
            'GUA POTVEL DE MESA': 'ÁGUA POTÁVEL DE MESA',
            'GUAS TERMAIS': 'ÁGUAS TERMAIS',
            'HEMATITA': 'HEMATITA',
            'ILMENITA': 'ILMENITA',
            'LATERITA': 'LATERITA',
            'MAGNETITA': 'MAGNETITA',
            'MANGANS': 'MANGANÊS',
            'MINRIO DE CHUMBO': 'MINÉRIO DE CHUMBO',
            'MINRIO DE COBRE': 'MINÉRIO DE COBRE',
            'MINRIO DE ESTANHO': 'MINÉRIO DE ESTANHO',
            'MINRIO DE FERRO': 'MINÉRIO DE FERRO',
            'MINRIO DE MANGANS': 'MINÉRIO DE MANGANÊS',
            'MINRIO DE NIBIO': 'MINÉRIO DE NIÓBIO',
            'MINRIO DE NQUEL': 'MINÉRIO DE NÍQUEL',
            'MINRIO DE OURO': 'MINÉRIO DE OURO',
            'MINRIO DE TITNIO': 'MINÉRIO DE TITÂNIO',
            'MINRIO DE VANDIO': 'MINÉRIO DE VANDIO',
            'MINRIO DE ZINCO': 'MINÉRIO DE ZINCO',
            'MRMORE': 'MÁRMORE',
            'NQUEL': 'NÍQUEL',
            'OURO': 'OURO',
            'QUARTZITO': 'QUARTZITO',
            'QUARTZO': 'QUARTZO',
            'SAIBRO': 'SAIBRO',
            'SIENITO': 'SIENITO',
            'TANTALITA': 'TANTALITA',
            'TITNIO': 'TITÂNIO',
            'TNTALO': 'TÂNTALO',
            'TURFA': 'TURFA',
            'TURMALINA': 'TURMALINA',
            'ZINCO': 'ZINCO',
            }

uso_cor = {'Artesanato  mineral': 'Artesanato  mineral',
           'Balneoterapia': 'Balneoterapia',
           'Brita': 'Brita',
           'Cermica vermelha': 'Cerâmica vermelha',
           'Construo civil': 'Construção civil',
           'Corretivo de solo': 'Corretivo de solo',
           'DADO NO CADASTRADO': 'DADO NÃO CADASTRADO',
           'Energtico': 'Energético',
           'Engarrafamento': 'Engarrafamento',
           'Fabricao de cal': 'Fabricação de cal',
           'Fabricao de cimento': 'Fabricação de cimento',
           'Fertilizantes': 'Fertilizantes',
           'Gema': 'Gema',
           'Industrial': 'Industrial',
           'Insumo agrcola': 'Insumo agrícola',
           'Metalurgia': 'Metalurgia',
           'No informado': 'Não informado',
           'Ourivesaria': 'Ourivesaria',
           'Pedra de coleo': 'Pedra de coleção',
           'Pedra decorativa': 'Pedra decorativa',
           'Revestimento': 'Revestimento',
           }

pr_s2['SUBS'] = pr_s2['SUBS'].cat.rename_categories(subs_cor)
pr_s2['USO'] = pr_s2['USO'].cat.rename_categories(uso_cor)
pr_s2.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/sig_proc_cpfcnpj.csv', index=False)
pr = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/sig_proc_cpfcnpj.csv')
# pr['CPF'] = pr['CPF/CNPJ'].map(cpf, 'ignore')
# pr['CNPJ'] = pr['CPF/CNPJ'].map(cnpj, 'ignore')

fis = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/mt_fisica.csv')
jur = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/mt_juridica.csv')

fis_u = pd.DataFrame(
    {'cpf': fis['CPF'].unique(), 'nome': fis['Titular'].unique()}
)

jur_u = pd.DataFrame(
    {'nome': jur['Titular'].unique()}
)

jur_u['cnpj'] = jur_u['nome'].map(lambda i: ((jur[jur['Titular'] == i]).reset_index())['CNPJ'][0],
                                  'ignore')

fis_u.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/mt_fisica.csv', index=False)
jur_u.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/mt_juridica.csv', index=False)

fis_u = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/mt_fisica.csv')
jur_u = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/mt_juridica.csv')

pr['CPF_f'] = pr['CPF'].map(lambda i: i if i in list(fis_u['cpf']) else None)
pr['CNPJ_f'] = pr['CNPJ'].map(lambda i: i if i in list(jur_u['cnpj']) else None)
pr.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/sig_proc_cpfcnpj_sep2.csv', index=False)

fis_id = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/fis_id.csv')
jur_id = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/jur_id.csv')

pr['FIS_ID'] = pr['CPF_f'].map(cpf2id)
pr['JUR_ID'] = pr['CNPJ_f'].map(cnpj2id)

pr.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/sig_proc_cpfcnpj_id_sep.csv', index=False)

# ler pr, ler id_cpf e id_cnpj
# criar função para lidar com cada uma das duas (procurar nas tabelas de id, se não achar retornar None)



def cpf(i):
    r = re.compile(r'\d\d\d.\d\d\d.\d\d\d-\d\d')
    f = r.match(i)
    if f:
        return f.group()
    return None


def cnpj(i):
    r = re.compile(r'\d\d.\d\d\d.\d\d\d/\d\d\d\d-\d\d')
    f = r.match(i)
    if f:
        return f.group()
    return None


fisica = mt['CPF/CNPJ do titular'].map(cpf)
pes_fisica = mt[mt['CPF/CNPJ do titular'] == fisica]

juridica = mt['CPF/CNPJ do titular'].map(cnpj)
pes_juridica = mt[mt['CPF/CNPJ do titular'] == juridica]

pes_fisica.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/mt_fisica.csv', index=False)
pes_juridica.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/mt_juridica.csv', index=False)

pr_s2 = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/sigmine_proc_2.csv')


enc = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/encontrados.csv')

# retirar processo duplicado
pr = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/novos/sig_proc_cpfcnpj_id_sep.csv')
pr2 = pr.sort_values(by='ANO', ascending=False)
pr2 = pr2.reset_index()
pr2.drop(columns=['index'], inplace=True)
pr3 = pr2.drop_duplicates('NUMERO')
pr3.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/novos/sig_comp_unique.csv', index=False)


def popular_demograficos():
    # print(os.path)
    dem = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/METAMAT/django/metamat/map/static/demografico.csv')
    print(dem.columns)
    for d in dem.values:
        novo = demografico(
            populacao_rural=d[2],
            populacao_urbana=d[3],
            populacao_total=d[2] + d[3],
            ano=2017,
            cidades_id_id=d[1])
        novo.save()


def popular_economia():
    ec = pd.read_csv(
        '/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/METAMAT/django/metamat/map/static/economia_2.csv')
    for e in ec.values:
        n = economia(
            receitas=e[3] * 1000,
            despesas=e[4] * 1000,
            ano=2014,
            cidades_id_id=e[0]
        )
        n.save()

    for e in ec.values:
        n = economia(
            pib_pc=e[1],
            receitas_fontext=e[2],
            # receitas=e[3],
            # despesas=e[4],
            pop_ativa_18mais=e[5],
            ocup_agropecuario=e[6],
            ocup_comercio=e[7],
            ocup_construcao=e[8],
            ocup_mineral=e[9],
            ocup_industria_utilpub=e[10],
            ocup_servic=e[11],
            ocup_industria_transf=e[12],
            ocup_grau_form=e[13],
            ocup_fundamental=e[14],
            ocup_medio=e[15],
            ocup_superior=e[16],
            atv_1maior_valor=e[-3],
            atv_2maior_valor=e[-2],
            atv_3maior_valor=e[-1],
            ano=2015,
            cidades_id_id=e[0]
        )
        n.save()


def popular_socioeconomico():
    se = pd.read_csv(
        '/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/METAMAT/django/metamat/map/static/socioeconomico_2.csv')
    for s in se.values:
        n = socioeconomico(
            pop_ocupada=s[1],
            idhm=s[2],
            idhm_renda=s[3],
            idhm_longevidade=s[4],
            idhm_educacao=s[5],
            expc_vida=s[6],
            prob_60anos=s[7],
            expc_anos_estudo18=s[8],
            renda_pc=s[9],
            salario_trab_form=s[10],
            prop_extr_pobre=s[11],
            prop_pobre=s[12],
            prop_vuln_pobre=s[13],
            taxa_analfab_15mais=s[14],
            ideb_inicias=s[15],
            ideb_finais=s[16],
            perc_pop_agua_enc=s[17],
            perc_pop_coleta_lixo=s[18],
            perc_pop_eletricidade=s[19],
            esg_sanit_adequado=s[20],
            perc_pop_esg_inadequado=s[21],
            perc_urban_vias_public=s[22],
            ano=2015,
            cidades_id_id=s[23]
        )
        n.save()
    pass


def popular_arrecadacao():
    ar = pd.read_csv(
        '/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/METAMAT/django/metamat/map/static/arrecadacao_2.csv')
    for a in ar.values:
        n = arrecadacao(
            total=a[2],
            tipo_taxa=a[3],
            tipo_atv=a[4],
            ano=a[5],
            cidades_id_id=a[1]
        )
        n.save()


def popular_pes_fisica():
    pf = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pf_novo.csv')

    for p in pf.values:
        n = pessoa_fisica(
            cpf=p[0],
            nome=p[1]
        )
        n.save()


def popular_pes_juridica():
    pj = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pj_novo.csv')
    for p in pj.values:
        n = pessoa_juridica(
            cnpj=p[0],
            razaosocial=p[1]
        )
        n.save()


def pop_cfem():
    cf = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/cfem_mt_comp.csv')

    for c in cf.values:
        np = c[1]
        ap = c[2]

        idp = None
        if np != -1:
            res = titulos_minerarios.objects.filter(numero=np, ano=ap)
            if len(res) > 0:
                idp = res[0].id

        cf['cpf_c'].fillna(-1, inplace=True)
        cf['cpf_c'] = cf['cpf_c'].astype(int)

        cf['cnpj_c'].fillna(-1, inplace=True)
        cf['cnpj_c'] = cf['cnpj_c'].astype(int)

        id_pf = None
        id_pj = None

        if c[17] > -1:
            id_pf = c[17]

        if c[18] > -1:
            id_pj = c[18]

        n = cfem(
            ano=c[0],
            num_proc=np,
            ano_proc=ap,
            subs=c[13],
            valor=c[11],
            quantidade=c[10],
            unidade=c[14],
            pessoa_fisica_id=id_pf,
            pessoa_juridica_id=id_pj,
            cidade_id=c[12],
            titulos_minerarios_id=idp,
        )
        n.save()


def pop_tah():
    th = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/tah_mt_comp.csv')

    for t in th.values:
        np = t[0]
        ap = t[1]

        idp = None
        if np != -1:
            res = titulos_minerarios.objects.filter(numero=np, ano=ap)
            if len(res) == 1:
                idp = res[0].id
            else:
                res = titulos_minerarios.objects.filter(numero=np)
                if len(res) == 1:
                    idp = res[0].id

                elif len(res) > 1:
                    print('---- Processo estranho ----')
                    print(res)
                    print('-' * 30)

        th['cpf_c'].fillna(-1, inplace=True)
        th['cpf_c'] = th['cpf_c'].astype(int)

        th['cnpj_c'].fillna(-1, inplace=True)
        th['cnpj_c'] = th['cnpj_c'].astype(int)

        id_pf = None
        id_pj = None

        if t[10] > -1:
            id_pf = t[10]

        if t[11] > -1:
            id_pj = t[11]

        n = tah(
            numProcesso=np,
            anoProcesso=ap,
            valorPago=t[6],
            valorCobrado=t[7],
            pessoa_fisica_id=id_pf,
            pessoa_juridica_id=id_pj,
            titulos_minerarios_id=idp,
        )
        n.save()


# utilizando dados atlasbrasil
at = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/atlas2013_dadosbrutos_pt.csv', sep=';', decimal=',')

at.drop(columns=['FECTOT', 'MORT1', 'MORT5', 'RAZDEP', 'SOBRE40', 'T_ENV', 'ANALF11A14', 'T_ANALF15A17', 'T_ANALF18A24', 'T_ANALF18M', 'T_ANALF25A29',
                 'T_ANALF25M', 'T_ATRASO_0_MED', 'T_ATRASO_1_BASICO', 'T_ATRASO_1_FUND', 'T_ATRASO_1_MED', 'T_ATRASO_2_BASICO', 'T_ATRASO_2_FUND',
                 'T_ATRASO_2_MED', 'T_FBBAS', 'T_FBFUND', 'T_FBMED', 'T_FBPRE', 'T_FBSUPER', 'T_FLBAS', 'T_FLFUND',
                 'T_FLMED', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '', '', '', '', '', '', '', '', '', '', '', '', '', '',]
        )

a = at[[
    'UF', 'UFN', 'CODMUN6', 'CODMUN7', 'ESPVIDA', 'SOBRE60', 'E_ANOSESTUDO', 'T_ANALF15M', 'PIND', 'PMPOB', 'PPOB',
    'RDPC', 'P_AGRO', 'P_COM', 'P_CONSTR', 'P_EXTR', 'P_FORMAL', 'P_FUND', 'P_MED', 'P_SERV',
    'P_SIUP', 'P_SUPER', 'P_TRANSF', 'RENOCUP', 'TRABPUB', 'T_AGUA', 'T_BANAGUA', 'T_LIXO', 'T_LUZ',
    'IDHM', 'IDHM-E', 'IDHM-L', 'IDHM-R', 'PESORUR', 'PESOTOT', 'PESOURB', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
]]

socio = [
'cod_mun',
'idhm',
'idhm_renda',
'idhm_longevidade',
'idhm_educacao',
'expc_vida',
'prob_60anos',
'expc_anos_estudo18',
'renda_pc',
'prop_extr_pobre',
'prop_pobre',
'prop_vuln_pobre',
'taxa_analfab_15mais',
'perc_pop_agua_enc',
'perc_pop_coleta_lixo',
'perc_pop_eletricidade',
'esg_sanit_adequado',
'perc_pop_esg_inadequado',
'ano']

class socioeconomico(models.Model):
    +pop_ocupada = models.FloatField(null=True)
    -idhm = models.FloatField(null=True)
    -idhm_renda = models.FloatField(null=True)
    -idhm_longevidade = models.FloatField(null=True)
    -idhm_educacao = models.FloatField(null=True)
    -expc_vida = models.FloatField(null=True)
    -prob_60anos = models.FloatField(null=True)
    -expc_anos_estudo18 = models.FloatField(null=True)
    -renda_pc = models.FloatField(null=True)
    +salario_trab_form = models.FloatField(null=True)
    -prop_extr_pobre = models.FloatField(null=True)
    -prop_pobre = models.FloatField(null=True)
    -prop_vuln_pobre = models.FloatField(null=True)
    -taxa_analfab_15mais = models.FloatField(null=True)
    *ideb_inicias = models.FloatField(null=True)
    *ideb_finais = models.FloatField(null=True)
    -perc_pop_agua_enc = models.FloatField(null=True)
    -perc_pop_coleta_lixo = models.FloatField(null=True)
    -perc_pop_eletricidade = models.FloatField(null=True)
    -esg_sanit_adequado = models.FloatField(null=True)
    -perc_pop_esg_inadequado = models.FloatField(null=True)
    perc_urban_vias_public = models.FloatField(null=True)
    ano = models.IntegerField(choices=ct.ano_chs(), default=ct.ano_atual())
    cidade = models.ForeignKey(cidades, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.cidade} : {self.ano}'

econ = [
'cod_mun',
'pop_ativa_18mais',
'ocup_agropecuario',
'ocup_comercio',
'ocup_construcao',
'ocup_mineral',
'ocup_industria_utilpub',
'ocup_servic',
'ocup_industria_transf',
'ocup_grau_form',
'ocup_fundamental',
'ocup_medio',
'ocup_superior',
'ano']
class economia(models.Model):

    +pib_pc = models.FloatField(null=True)
    receitas_fontext = models.FloatField(null=True)
    receitas = models.FloatField(null=True)
    despesas = models.FloatField(null=True)
    -pop_ativa_18mais = models.IntegerField(null=True)
    pop_ocupada = models.IntegerField(null=True) # calculada a partir da pop_ocupada da socioeconomico
    # pop_ocupada possui mais de uma opção:
    #   CPR - Percentual de ocupados de 18 anos ou mais que são trabalhadores por conta própria.
    #   EMP - Percentual de ocupados de 18 anos ou mais que são empregadores
    #   TRABCC - Percentual de ocupados de 18 anos ou mais que são empregados com carteira
    #   TRABSC - Percentual de ocupados de 18 anos ou mais que são empregados sem carteira
    -ocup_agropecuario = models.FloatField(null=True)
    -ocup_comercio = models.FloatField(null=True)
    -ocup_construcao = models.FloatField(null=True)
    -ocup_mineral = models.FloatField(null=True)
    -ocup_industria_utilpub = models.FloatField(null=True)
    -ocup_servic = models.FloatField(null=True)
    -ocup_industria_transf = models.FloatField(null=True)
    -ocup_grau_form = models.FloatField(null=True)
    -ocup_fundamental = models.FloatField(null=True)
    -ocup_medio = models.FloatField(null=True)
    -ocup_superior = models.FloatField(null=True)
    +atv_1maior_valor = models.IntegerField(null=True, choices=ct.t_atv_ec)
    +atv_2maior_valor = models.IntegerField(null=True, choices=ct.t_atv_ec)
    +atv_3maior_valor = models.IntegerField(null=True, choices=ct.t_atv_ec)
    ano = models.IntegerField(choices=ct.ano_chs(), default=ct.ano_atual())
    cidade = models.ForeignKey(cidades, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.cidade} : {self.ano}'

dem = [
'cod_mun',
'populacao_urbana',
'populacao_rural',
'populacao_total',
'ano']
class demografico(models.Model):
    -populacao_urbana = models.IntegerField()
    -populacao_rural = models.IntegerField()
    -populacao_total = models.IntegerField() # Acrescentar no banco e atualizar
    ano = models.IntegerField(choices=ct.ano_chs(), default=ct.ano_atual())
    cidade = models.ForeignKey(cidades, on_delete=models.PROTECT)



pib_co = ['Ano',
       'Código da Unidade da Federação',
       'Código do Município',
       'Valor adicionado bruto da Agropecuária, a preços correntes\n(R$ 1.000)',
       'Valor adicionado bruto da Indústria, a preços correntes\n(R$ 1.000)',
       'Valor adicionado bruto dos Serviços, a preços correntes - exclusive Administração, defesa, educação e saúde públicas e seguridade social\n(R$ 1.000)',
       'Valor adicionado bruto da Administração, defesa, educação e saúde públicas e seguridade social\n(R$ 1.000)',
       'Valor adicionado bruto total, a preços correntes\n(R$ 1.000)',
       'Impostos, líquidos de subsídios, sobre produtos, a preços correntes\n(R$ 1.000)',
       'Produto Interno Bruto, a preços correntes\n(R$ 1.000)',
       'População\n(Nº de habitantes)',
       'Produto Interno Bruto per capita\n(R$ 1,00)',
       'Atividade com maior valor adicionado bruto',
       'Atividade com segundo maior valor adicionado bruto',
       'Atividade com terceiro maior valor adicionado bruto']
