import pandas as pd
import re

cfem = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/Cfem.csv', encoding='iso8859_2')
cfem_mt = cfem[cfem['Uf'] == 'MT'].reset_index().drop(columns=['index'])
cfem_mt.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/Cfem_mt.csv', encoding='utf-8', index=False)

cods = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cod_mun_mt_2.csv')
cods['nome'] = cods['nome'].map(lambda i: i[:-5])
cods['nome'] = cods['nome'].map(lambda i: i.upper())
cods.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cod_mun_mt_2.csv', index=False)


def cod_mun(i):
    r = cods[cods['nome'] == i]['cod'].reset_index(drop=True)

    if not r.empty:
        return r[0]

    return None


cfem_mt['cod_mun'] = cfem_mt['Município'].map(cod_mun, 'ingnore')

d_subs = {
    0: 'DADO NÃO CADASTRADO', 1: 'AMETISTA', 2: 'AREIA', 3: 'AREIA LAVADA',
    4: 'ARENITO', 5: 'ARGILA', 6: 'BASALTO', 7: 'BRITA DE GRANITO',
    8: 'CALCEDÔNIA', 9: 'CALCÁRIO', 10: 'CALCÁRIO CALCÍTICO',
    11: 'CALCÁRIO DOLOMÍTICO', 12: 'CALCÁRIO INDUSTRIAL', 13: 'CASCALHO',
    14: 'CASCALHO DIAMANTÍFERO', 15: 'CASSITERITA', 16: 'CAULIM', 17: 'CHUMBO',
    18: 'COBRE', 19: 'COLUMBITA', 20: 'CONGLOMERADO', 21: 'DIAMANTE',
    22: 'DIAMANTE INDUSTRIAL', 23: 'DOLOMITO', 24: 'ESTANHO', 25: 'FELDSPATO',
    26: 'FILITO', 27: 'FOSFATO', 28: 'GABRO', 29: 'GALENA', 30: 'GRANITO',
    31: 'GRANITO ORNAMENTAL', 32: 'HEMATITA', 33: 'ILMENITA', 34: 'LATERITA',
    35: 'MAGNETITA', 36: 'MANGANÊS', 37: 'MINÉRIO DE CHUMBO',
    38: 'MINÉRIO DE COBRE', 39: 'MINÉRIO DE ESTANHO', 40: 'MINÉRIO DE FERRO',
    41: 'MINÉRIO DE MANGANÊS', 42: 'MINÉRIO DE NIÓBIO', 43: 'MINÉRIO DE NÍQUEL',
    44: 'MINÉRIO DE OURO', 45: 'MINÉRIO DE TITÂNIO', 46: 'MINÉRIO DE VANDIO',
    47: 'MINÉRIO DE ZINCO', 48: 'MÁRMORE', 49: 'NÍQUEL', 50: 'OURO', 51: 'QUARTZITO',
    52: 'QUARTZO', 53: 'SAIBRO', 54: 'SIENITO', 55: 'TANTALITA', 56: 'TITÂNIO',
    57: 'TURFA', 58: 'TURMALINA', 59: 'TÂNTALO', 60: 'ZINCO', 61: 'ÁGUA MINERAL',
    62: 'ÁGUA POTÁVEL DE MESA', 63: 'ÁGUAS TERMAIS', 64: 'ARGILA COMUM',
    65: 'AREIA IN NATURA', 66: 'GEMA', 67: 'AREIA QUARTZOSA', 68: 'CALCÁRIO P/ BRITA',
    69: 'AREIA COMUM', 70: 'ARGILA P/CER. VERMELH', 71: 'PEDRA CALCÁRIA', 72: 'FERRO',
    73: 'SEIXOS ROLADOS', 74: 'CASCALHO SILICOSO', 75: 'BASALTO P/ BRITA',
    76: 'GRANITO P/ BRITA', 77: 'MINÉRIO DE PRATA', 78: 'OURO NATIVO'
    }

subs = dict(zip(list(d_subs.values()), list(d_subs.keys())))

col = ['ano', 'processo', 'anoProc', 'cpfcnpj', 'pessoa', 'fase', 'subs', 'uf',
       'mun', 'un', 'qtd', 'valor', 'cod_mun']
cfem_mt.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/Cfem_mt.csv', index=False)

cfem_mt['cod_subs'] = cfem_mt['subs'].map(lambda i: subs[i], 'ignore')

un = {'ct': 1, 'g': 2, 'kg': 3, 'l': 4, 'm³': 5, 't': 6}


def un2cod(i):
    i = i.strip()
    if i == 'm3':
        i = 'm³'
    return un[i]


cfem_mt['cod_un'] = cfem_mt['un'].map(un2cod, 'ignore')

cfem_mt['processo'] = cfem_mt['processo'].fillna(-1).astype(int)
cfem_mt['anoProc'] = cfem_mt['anoProc'].fillna(-1).astype(int)


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


cfem_mt['qtd'] = cfem_mt['qtd'].map(lambda i: i.replace(',', '.'))
cfem_mt['qtd'] = cfem_mt['qtd'].astype(float)

cfem_mt['valor'] = cfem_mt['valor'].map(lambda i: i.replace(',', '.'))
cfem_mt['valor'] = cfem_mt['valor'].astype(float)

fisica = cfem_mt['cpfcnpj'].map(cpf)
pes_fisica = cfem_mt[cfem_mt['cpfcnpj'] == fisica].reset_index(drop=True)

juridica = cfem_mt['cpfcnpj'].map(cnpj)
pes_juridica = cfem_mt[cfem_mt['cpfcnpj'] == juridica].reset_index(drop=True)

pes_fisica.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/Cfem_mt_pf.csv', index=False)
pes_juridica.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/Cfem_mt_pj.csv', index=False)


cfem_mt = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/Cfem_mt.csv')


# organizando dados do TAH

tah = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/Tah.csv', encoding='iso8859_2')
tah.info()
tah['uf'] = tah['Superintendęncia'].map(lambda i: i[-2:], 'ignore')

tah_mt = tah[tah['uf'] == 'MT']
tah_mt.columns = ['processo', 'anoProc', 'cpfcnpj', 'pessoa', 'fase',
                  'superintendencia', 'area', 'valorPago', 'valorCobrado', 'uf']

tah_mt.info()
tah_mt.drop(columns=['uf', 'superintendencia'], inplace=True)


def comma2dot(i):
    return i.replace(',', '.')


tah_mt['area'] = tah_mt['area'].map(comma2dot, 'ignore')
tah_mt['valorPago'] = tah_mt['valorPago'].map(comma2dot, 'ignore')
tah_mt['valorCobrado'] = tah_mt['valorCobrado'].map(comma2dot, 'ignore')


tah_mt['area'] = tah_mt['area'].astype(float)
tah_mt['valorPago'] = tah_mt['valorPago'].astype(float)
tah_mt['valorCobrado'] = tah_mt['valorCobrado'].astype(float)

tah_mt.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/tah_mt.csv', encoding='utf-8', index=False)
tah_mt['cpfcnpj'] = tah_mt['cpfcnpj'].astype(str)

fisica = tah_mt['cpfcnpj'].map(cpf)
pes_fisica = tah_mt[tah_mt['cpfcnpj'] == fisica].reset_index(drop=True)

juridica = tah_mt['cpfcnpj'].map(cnpj)
pes_juridica = tah_mt[tah_mt['cpfcnpj'] == juridica].reset_index(drop=True)

pes_fisica.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/tah_mt_pf.csv', index=False)
pes_juridica.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/tah_mt_pj.csv', index=False)


# add + cnpj e cpf na tabela de processos

s = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/novos/sig_comp_unique.csv')

import numpy as np


def sep2un(i):
    if i:
        return i


s['cpfcnpj'] = None


s['cpfcnpj'] = s['CNPJ']

s['cpfcnpj'].values[-1] = s['cpfcnpj'].values[-1][:-2]

for i in range(len(s['cpfcnpj'].values)):
    if s['CPF'].values[i]:
        s['cpfcnpj'].values[i] = s['CPF'].values[i]


tah_mt['pessoa_b'] = tah_mt['pessoa'].map(lambda i: i.encode('ascii', 'ignore'))
pes = list(tah_mt['pessoa_b'].values)

cf = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/Cfem_mt.csv')
cf['pessoa_b'] = cf['pessoa'].map(lambda i: i.encode('ascii', 'ignore'))
pes2 = list(cf['pessoa_b'].values)


qtd = 0
for i in range(len(s['cpfcnpj'].values)):
    if s['NOME'].values[i].encode('ascii', 'ignore') in pes:
        qtd += 1

print(qtd)


p = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/procs.csv')
procs = p.drop_duplicates('PROCESSO')

procs['cpfcnpj'] = None
procs['cpf'] = None
procs['cnpj'] = None


for i in range(len(procs['cpfcnpj'].values)):
    if not procs['cpfcnpj'].values[i]:
        nome = procs['NOME'].values[i].encode('ascii', 'ignore')
        if nome in pes:
            procs['cpfcnpj'].values[i] = tah_mt['cpfcnpj'].values[pes.index(nome)]
        elif nome in pes2:
            procs['cpfcnpj'].values[i] = cf['cpfcnpj'].values[pes2.index(nome)]


for i in range(len(procs['cpfcnpj'].values)):
    t = procs['cpfcnpj'].values[i]
    if t:
        if cpf(t):
            procs['cpf'].values[i] = t
        elif cnpj(t):
            procs['cnpj'].values[i] = t


procs.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/procs_cpf_cnpj_3.csv', index=False)

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

procs['SUBS'] = procs['SUBS'].astype('category')
procs['USO'] = procs['USO'].astype('category')
procs['SUBS'] = procs['SUBS'].cat.rename_categories(subs_cor)
procs['USO'] = procs['USO'].cat.rename_categories(uso_cor)

procs.info()

un = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/processos_min/uniao.csv')
un.drop(columns=['Superintendęncia', 'Processo', 'Tipo de requerimento', 'Fase Atual',
                 'Municipio(s)', 'Substância(s)', 'Tipo(s) de Uso',
                 'Situaçăo', 'Data da Cessăo', 'Unnamed: 0', 'SuperintendÄncia',
                 'SubstĂ˘ncia(s)', 'SituaĂ§Äo'], inplace=True)

un = un.drop_duplicates('CPF/CNPJ do titular').reset_index(drop=True)
un['nomeb'] = un['Titular'].map(lambda i: i.encode('ascii', 'ignore'), 'ignore')

procs = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/procs_cpf_cnpj_2.csv')
procs['cpfcnpj'].fillna('', inplace=True)

pess = list(un['nomeb'].values)

df = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/procs_f.csv')
df2 = df.copy()
df2['nomeb'] = df2['nome'].map(lambda i: i.encode('ascii', 'ignore'), 'ignore')
df2 = df2.drop_duplicates('cpfcnpj').reset_index(drop=True)
pess = list(df2['nomeb'].values)
procs['cpfcnpj'].fillna('', inplace=True)
a = 0
for i in range(len(procs['cpfcnpj'].values)):
    if not procs['cpfcnpj'].values[i]:
        nome = procs['NOME'].values[i].encode('ascii', 'ignore')
        if nome in pess:
            a += 1
            procs['cpfcnpj'].values[i] = df2['cpfcnpj'].values[pess.index(nome)]

print(a)


def cpf2(i):
    r = re.compile(r'\*\*\*.\d\d\d.\d\d\d-\*\*')
    f = r.match(i)
    if f:
        return f.group()
    else:
        r = re.compile(r'\d\d\d.\d\d\d.\d\d\d-\d\d')
        f = r.match(i)
        if f:
            return f.group()
    return None


df = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/procs_cpf_cnpj_3.csv')
df['cpf'] = df['cpfcnpj'].map(cpf2, 'ignore')
df.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/procs_cpf_cnpj_3.csv', index=False)

d = df[['cpfcnpj', 'NOME', 'cpf', 'cnpj']].copy()
d = d.drop_duplicates('cpfcnpj').reset_index(drop=True)
d.dropna(subset=['cpfcnpj'], inplace=True)

d['cpf'].fillna('', inplace=True)
d['cnpj'].fillna('', inplace=True)


pf = {'cpf': [], 'nome': []}
pj = {'cnpj': [], 'nome': []}

for p in range(len(d)):
    if d.iloc[p]['cpf']:
        pf['cpf'].append(d.iloc[p]['cpf'])
        pf['nome'].append(d.iloc[p]['NOME'])

    elif d.iloc[p]['cnpj']:
        pj['cnpj'].append(d.iloc[p]['cnpj'])
        pj['nome'].append(d.iloc[p]['NOME'])

d_pf = pd.DataFrame(pf)
d_pj = pd.DataFrame(pj)

d_pf.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pf_novo.csv', index=False)
d_pj.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pj_novo.csv', index=False)

pf_id = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pf_id.csv')
pj_id = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pj_id.csv')


def id_pf(i):
    pes = pf_id[pf_id['cpf'] == i].reset_index(drop=True)['id']
    if len(pes) > 0:
        return pes[0]
    return None


def id_pj(i):
    pes = pj_id[pj_id['cnpj'] == i].reset_index(drop=True)['id']
    if len(pes) > 0:
        return pes[0]
    return None


df['pf_id'] = df['cpf'].map(id_pf, 'ignore')
df['pj_id'] = df['cnpj'].map(id_pj, 'ignore')


df.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/procs_cpf_cnpj_id.csv', index=False)

f = {'DADO NÃO CADASTRADO': 0, 'AUTORIZAÇÃO DE PESQUISA': 1, 'CONCESSO DE LAVRA': 2, 'DISPONIBILIDADE': 3, 'LAVRA GARIMPEIRA': 4, 'LICENCIAMENTO': 5, 'REGISTRO DE EXTRAÇÃO': 6, 'REQUERIMENTO DE LAVRA': 7, 'REQUERIMENTO DE LAVRA GARIMPEIRA': 8, 'REQUERIMENTO DE LICENCIAMENTO': 9, 'REQUERIMENTO DE PESQUISA': 10, 'REQUERIMENTO DE REGISTRO DE EXTRAÇÃO': 11}

df['fase_c'] = df['FASE'].map(lambda i: f[i], 'ignore').astype(int)
df['fase_c'].fillna(0, inplace=True)
df['fase_c'] = df['fase_c'].astype(int)

# checar e adicionar pfs e pjs das planilhas de cfem e tah no bd
pft = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/tah_mt_pf.csv')
pfc = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/Cfem_mt_pf.csv')

pf_id = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pf_id.csv')

pft.drop(columns=['processo', 'anoProc', 'fase', 'area', 'valorPago', 'valorCobrado'], inplace=True)
pfc.drop(columns=['processo', 'ano', 'anoProc', 'fase', 'subs', 'uf', 'valor', 'un', 'mun', 'qtd', 'valor', 'cod_mun', 'cod_subs', 'cod_un'], inplace=True)
pfs = pd.concat([pft, pfc], ignore_index=True, sort=False)
pfs.drop_duplicates('cpfcnpj', inplace=True)
pfs = pfs.reset_index(drop=True)

n = {'cpf': [], 'nome': []}
for i in range(len(pfs['cpfcnpj'].values)):
    if pfs['cpfcnpj'].at[i] not in pf_id['cpf'].values:
        n['cpf'].append(pfs['cpfcnpj'].at[i])
        n['nome'].append(pfs['pessoa'].at[i])

pf_novo = pd.DataFrame(n)
pf_novo.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pfs_novos.csv')


pj_id = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pj_id.csv')
pjt = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/tah_mt_pj.csv')
pjc = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/Cfem_mt_pj.csv')

pjt.drop(columns=['processo', 'anoProc', 'fase', 'area', 'valorPago', 'valorCobrado'], inplace=True)
pjc.drop(columns=['processo', 'ano', 'anoProc', 'fase', 'subs', 'uf', 'valor', 'un', 'mun', 'qtd', 'valor', 'cod_mun', 'cod_subs', 'cod_un'], inplace=True)
pjs = pd.concat([pjt, pjc], ignore_index=True, sort=False)
pjs.drop_duplicates('cpfcnpj', inplace=True)
pjs = pjs.reset_index(drop=True)

n = {'cnpj': [], 'nome': []}
for i in range(len(pjs['cpfcnpj'].values)):
    if pjs['cpfcnpj'].at[i] not in pj_id['cnpj'].values:
        n['cnpj'].append(pjs['cpfcnpj'].at[i])
        n['nome'].append(pjs['pessoa'].at[i])

pj_novo = pd.DataFrame(n)
pj_novo.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pjs_novos.csv')

# reorganizando cfem e tah para adicionar ID das pjs e pfs e fase

cf = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/Cfem_mt.csv')
cf['cpf'] = cf['cpfcnpj'].map(cpf2, 'ignore')
cf['cnpj'] = cf['cpfcnpj'].map(cnpj, 'ignore')

pf_id = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pf_id_n.csv')
pj_id = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pj_id_n.csv')

cf['cpf_c'] = cf['cpf'].map(id_pf, 'ignore')
cf['cnpj_c'] = cf['cnpj'].map(id_pj, 'ignore')

f = {'': 0, 'AUTORIZAÇĂO DE PESQUISA': 1, 'CONCESSĂO DE LAVRA': 2, 'DISPONIBILIDADE': 3, 'LAVRA GARIMPEIRA': 4, 'LICENCIAMENTO': 5, 'REGISTRO DE EXTRAÇÃO': 6, 'REQUERIMENTO DE LAVRA': 7, 'REQUERIMENTO DE LAVRA GARIMPEIRA': 8, 'REQUERIMENTO DE LICENCIAMENTO': 9, 'REQUERIMENTO DE PESQUISA': 10, 'REQUERIMENTO DE REGISTRO DE EXTRAÇÃO': 11}


cf['fase'].fillna('', inplace=True)

cf['fase_c'] = cf['fase'].map(lambda i: f[i.upper()], 'ignore')

cf.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/cfem_mt_comp.csv', index=False)

th = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/tah_mt.csv')

th['cpf'] = th['cpfcnpj'].map(cpf2, 'ignore')
th['cnpj'] = th['cpfcnpj'].map(cnpj, 'ignore')

pf_id = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pf_id_n.csv')
pj_id = pd.read_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/pj_id_n.csv')

th['cpf_c'] = th['cpf'].map(id_pf, 'ignore')
th['cnpj_c'] = th['cnpj'].map(id_pj, 'ignore')

f = {'': 0, 'AUTORIZAÇĂO DE PESQUISA': 1, 'CONCESSĂO DE LAVRA': 2, 'DISPONIBILIDADE': 3, 'LAVRA GARIMPEIRA': 4, 'LICENCIAMENTO': 5, 'REGISTRO DE EXTRAÇÃO': 6, 'REQUERIMENTO DE LAVRA': 7, 'REQUERIMENTO DE LAVRA GARIMPEIRA': 8, 'REQUERIMENTO DE LICENCIAMENTO': 9, 'REQUERIMENTO DE PESQUISA': 10, 'REQUERIMENTO DE REGISTRO DE EXTRAÇÃO': 11}


th['fase'].fillna('', inplace=True)

th['fase_c'] = th['fase'].map(lambda i: f[i.strip(' \n\t').upper()], 'ignore')

th.to_csv('/mnt/e7a19ebd-2ae9-44e1-8a25-7684571238f5/Gustavo/Materiais/cfem_tah/tah_mt_comp.csv', index=False)




