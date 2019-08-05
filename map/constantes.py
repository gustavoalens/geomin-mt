import datetime

# Dicionário p/ tipos de taxa, usado p/ transf. colunas catg.
d_tipos_tx = {
    0: '',
    1: 'TAH',
    2: 'CFEM',
}

# Dicionário p/ tipos de atv. mineradora, usado p/ transf. colunas catg.
d_atv_min = {
    0: '',
    1: 'Água Mineral/Potável',
    2: 'Calcário',
    3: 'Calcário Calcítico',
    4: 'Calcário Dolomítico',
    5: 'Água Termal',
    6: 'Granito/Brita',
    7: 'Minério de Manganês',
    8: 'Minério de Ouro/Ouro',
    9: 'Gema/Diamantes',
    10: 'Argila',
    11: 'Areia',
}

d_opcs = {
    '1': 'Demográfico',
    '2': 'Econômico',
    '3': 'Socioeconômico',
}

# Dicionário p/ tipos de atv. economica, usado p/ transf. colunas catg.
# d_atv_ec = {
#     0: 'Sem registro',
#     1: 'Indústrias de transformação',
#     2: 'Indústrias extrativas',
#     3: 'Construção',
#     4: 'Agricultura, inclusive apoio à agricultura e a pós colheita',
#     5: 'Administração, educação, saúde, pesquisa e desenvolvimento públicas, defesa, seguridade social',
#     6: 'Comércio e reparação de veículos automotores e motocicletas',
#     7: 'Produção florestal, pesca e aquicultura',
#     8: 'Pecuária, inclusive apoio à pecuária',
#     9: 'Eletricidade e gás, água, esgoto, atividades de gestão de resíduos e descontaminação',
#     10: 'Demais serviços',
# }

d_atv_ec = {
    0: 'Sem registro',
    1: 'Administração, defesa, educação e saúde públicas e seguridade social',
    2: 'Agricultura, inclusive apoio à agricultura e a pós colheita',
    3: 'Comércio e reparação de veículos automotores e motocicletas',
    4: 'Construção',
    5: 'Demais serviços',
    6: 'Eletricidade e gás, água, esgoto, atividades de gestão de resíduos e descontaminação',
    7: 'Indústrias de transformação',
    8: 'Indústrias extrativas',
    9: 'Pecuária, inclusive apoio à pecuária',
    10: 'Produção florestal, pesca e aquicultura'
}

d_fase = {
    0: 'DADO NÃO CADASTRADO', 1: 'AUTORIZAÇÃO DE PESQUISA', 2: 'CONCESSO DE LAVRA',
    3: 'DISPONIBILIDADE', 4: 'LAVRA GARIMPEIRA', 5: 'LICENCIAMENTO',
    6: 'REGISTRO DE EXTRAÇÃO', 7: 'REQUERIMENTO DE LAVRA', 8: 'REQUERIMENTO DE LAVRA GARIMPEIRA',
    9: 'REQUERIMENTO DE LICENCIAMENTO', 10: 'REQUERIMENTO DE PESQUISA',
    11: 'REQUERIMENTO DE REGISTRO DE EXTRAÇÃO',
    }

t_fase = (
    (0, 'DADO NÃO CADASTRADO'),
    (1, 'AUTORIZAO DE PESQUISA'), (2, 'CONCESSO DE LAVRA'), (3, 'DISPONIBILIDADE'),
    (4, 'LAVRA GARIMPEIRA'), (5, 'LICENCIAMENTO'), (6, 'REGISTRO DE EXTRAO'),
    (7, 'REQUERIMENTO DE LAVRA'), (8, 'REQUERIMENTO DE LAVRA GARIMPEIRA'),
    (9, 'REQUERIMENTO DE LICENCIAMENTO'), (10, 'REQUERIMENTO DE PESQUISA'),
    (11, 'REQUERIMENTO DE REGISTRO DE EXTRAO'),
    )

# Dicionário p/ substratos da tabela do titulos_minerarios
d_subs_tm = {
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
    47: 'MINÉRIO DE ZINCO', 48: 'MÁRMORE', 49: 'NÍQUEL', 50: 'OURO',
    51: 'QUARTZITO', 52: 'QUARTZO', 53: 'SAIBRO', 54: 'SIENITO',
    55: 'TANTALITA', 56: 'TITÂNIO', 57: 'TURFA', 58: 'TURMALINA', 59: 'TÂNTALO',
    60: 'ZINCO', 61: 'ÁGUA MINERAL', 62: 'ÁGUA POTÁVEL DE MESA',
    63: 'ÁGUAS TERMAIS'
    }

t_subs_tm = (
    (-1, '-------'),
    (0, 'DADO NÃO CADASTRADO'), (1, 'AMETISTA'), (2, 'AREIA'), (3, 'AREIA LAVADA'),
    (4, 'ARENITO'), (5, 'ARGILA'), (6, 'BASALTO'), (7, 'BRITA DE GRANITO'),
    (8, 'CALCEDÔNIA'), (9, 'CALCÁRIO'), (10, 'CALCÁRIO CALCÍTICO'),
    (11, 'CALCÁRIO DOLOMÍTICO'), (12, 'CALCÁRIO INDUSTRIAL'), (13, 'CASCALHO'),
    (14, 'CASCALHO DIAMANTÍFERO'), (15, 'CASSITERITA'), (16, 'CAULIM'),
    (17, 'CHUMBO'), (18, 'COBRE'), (19, 'COLUMBITA'), (20, 'CONGLOMERADO'),
    (21, 'DIAMANTE'), (22, 'DIAMANTE INDUSTRIAL'), (23, 'DOLOMITO'),
    (24, 'ESTANHO'), (25, 'FELDSPATO'), (26, 'FILITO'), (27, 'FOSFATO'),
    (28, 'GABRO'), (29, 'GALENA'), (30, 'GRANITO'), (31, 'GRANITO ORNAMENTAL'),
    (32, 'HEMATITA'), (33, 'ILMENITA'), (34, 'LATERITA'), (35, 'MAGNETITA'),
    (36, 'MANGANÊS'), (37, 'MINÉRIO DE CHUMBO'), (38, 'MINÉRIO DE COBRE'),
    (39, 'MINÉRIO DE ESTANHO'), (40, 'MINÉRIO DE FERRO'),
    (41, 'MINÉRIO DE MANGANÊS'), (42, 'MINÉRIO DE NIÓBIO'),
    (43, 'MINÉRIO DE NÍQUEL'), (44, 'MINÉRIO DE OURO'),
    (45, 'MINÉRIO DE TITÂNIO'), (46, 'MINÉRIO DE VANDIO'),
    (47, 'MINÉRIO DE ZINCO'), (48, 'MÁRMORE'), (49, 'NÍQUEL'), (50, 'OURO'),
    (51, 'QUARTZITO'), (52, 'QUARTZO'), (53, 'SAIBRO'), (54, 'SIENITO'),
    (55, 'TANTALITA'), (56, 'TITÂNIO'), (57, 'TURFA'), (58, 'TURMALINA'),
    (59, 'TÂNTALO'), (60, 'ZINCO'), (61, 'ÁGUA MINERAL'),
    (62, 'ÁGUA POTÁVEL DE MESA'), (63, 'ÁGUAS TERMAIS')
    )

d_uso_tm = {
    -1: '-------',
    0: 'DADO NÃO CADASTRADO', 1: 'Artesanato  mineral', 2: 'Balneoterapia',
    3: 'Brita', 4: 'Cerâmica vermelha', 5: 'Construção civil',
    6: 'Corretivo de solo', 7: 'Energético', 8: 'Engarrafamento',
    9: 'Fabricação de cal', 10: 'Fabricação de cimento', 11: 'Fertilizantes',
    12: 'Gema', 13: 'Industrial', 14: 'Insumo agrícola', 15: 'Metalurgia',
    16: 'Não informado', 17: 'Ourivesaria', 18: 'Pedra de coleção',
    19: 'Pedra decorativa', 20: 'Revestimento'
    }

t_uso_tm = (
    (-1, '-------'),
    (0, 'DADO NÃO CADASTRADO'), (1, 'Artesanato  mineral'), (2, 'Balneoterapia'),
    (3, 'Brita'), (4, 'Cerâmica vermelha'), (5, 'Construção civil'),
    (6, 'Corretivo de solo'), (7, 'Energético'), (8, 'Engarrafamento'),
    (9, 'Fabricação de cal'), (10, 'Fabricação de cimento'), (11, 'Fertilizantes'),
    (12, 'Gema'), (13, 'Industrial'), (14, 'Insumo agrícola'), (15, 'Metalurgia'),
    (16, 'Não informado'), (17, 'Ourivesaria'), (18, 'Pedra de coleção'),
    (19, 'Pedra decorativa'), (20, 'Revestimento')
    )

d_subs_ar = {
    0: 'DADO NÃO CADASTRADO', 1: 'AREIA', 2: 'AREIA COMUM', 3: 'AREIA IN NATURA', 4: 'AREIA LAVADA',
    5: 'AREIA QUARTZOSA', 6: 'ARENITO', 7: 'ARGILA', 8: 'ARGILA COMUM',
    9: 'ARGILA P/CER. VERMELH', 10: 'BASALTO', 11: 'BASALTO P/ BRITA',
    12: 'BRITA DE GRANITO', 13: 'CALCÁRIO', 14: 'CALCÁRIO CALCÍTICO',
    15: 'CALCÁRIO DOLOMÍTICO', 16: 'CALCÁRIO P/ BRITA', 17: 'CASCALHO',
    18: 'CASCALHO SILICOSO', 19: 'CASSITERITA', 20: 'COBRE', 21: 'DIAMANTE',
    22: 'DIAMANTE INDUSTRIAL', 23: 'DOLOMITO', 24: 'FERRO', 25: 'FILITO',
    26: 'GABRO', 27: 'GEMA', 28: 'GRANITO', 29: 'GRANITO P/ BRITA',
    30: 'MINÉRIO DE FERRO', 31: 'MINÉRIO DE MANGANÊS', 32: 'MINÉRIO DE OURO',
    33: 'MINÉRIO DE PRATA', 34: 'MINÉRIO DE ZINCO', 35: 'OURO',
    36: 'OURO NATIVO', 37: 'PEDRA CALCÁRIA', 38: 'QUARTZITO', 39: 'QUARTZO',
    40: 'SEIXOS ROLADOS', 41: 'ÁGUA MINERAL', 42: 'ÁGUA POTÁVEL DE MESA',
    43: 'ÁGUAS TERMAIS'
    }

t_subs_ar = (
    (0, 'DADO NÃO CADASTRADO'), (1, 'AREIA'), (2, 'AREIA COMUM'), (3, 'AREIA IN NATURA'),
    (4, 'AREIA LAVADA'), (5, 'AREIA QUARTZOSA'), (6, 'ARENITO'),
    (7, 'ARGILA'), (8, 'ARGILA COMUM'), (9, 'ARGILA P/CER. VERMELH'),
    (10, 'BASALTO'), (11, 'BASALTO P/ BRITA'), (12, 'BRITA DE GRANITO'),
    (13, 'CALCÁRIO'), (14, 'CALCÁRIO CALCÍTICO'), (15, 'CALCÁRIO DOLOMÍTICO'),
    (16, 'CALCÁRIO P/ BRITA'), (17, 'CASCALHO'), (18, 'CASCALHO SILICOSO'),
    (19, 'CASSITERITA'), (20, 'COBRE'), (21, 'DIAMANTE'),
    (22, 'DIAMANTE INDUSTRIAL'), (23, 'DOLOMITO'), (24, 'FERRO'), (25, 'FILITO'),
    (26, 'GABRO'), (27, 'GEMA'), (28, 'GRANITO'), (29, 'GRANITO P/ BRITA'),
    (30, 'MINÉRIO DE FERRO'), (31, 'MINÉRIO DE MANGANÊS'), (32, 'MINÉRIO DE OURO'),
    (33, 'MINÉRIO DE PRATA'), (34, 'MINÉRIO DE ZINCO'), (35, 'OURO'), (36, 'OURO NATIVO'),
    (37, 'PEDRA CALCÁRIA'), (38, 'QUARTZITO'), (39, 'QUARTZO'), (40, 'SEIXOS ROLADOS'),
    (41, 'ÁGUA MINERAL'), (42, 'ÁGUA POTÁVEL DE MESA'), (43, 'ÁGUAS TERMAIS')
    )

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

t_subs = (
    (0, '---------'), (1, 'AMETISTA'), (2, 'AREIA'),
    (3, 'AREIA LAVADA'), (4, 'ARENITO'), (5, 'ARGILA'), (6, 'BASALTO'),
    (7, 'BRITA DE GRANITO'), (8, 'CALCEDÔNIA'), (9, 'CALCÁRIO'),
    (10, 'CALCÁRIO CALCÍTICO'), (11, 'CALCÁRIO DOLOMÍTICO'),
    (12, 'CALCÁRIO INDUSTRIAL'), (13, 'CASCALHO'), (14, 'CASCALHO DIAMANTÍFERO'),
    (15, 'CASSITERITA'), (16, 'CAULIM'), (17, 'CHUMBO'), (18, 'COBRE'),
    (19, 'COLUMBITA'), (20, 'CONGLOMERADO'), (21, 'DIAMANTE'),
    (22, 'DIAMANTE INDUSTRIAL'), (23, 'DOLOMITO'), (24, 'ESTANHO'),
    (25, 'FELDSPATO'), (26, 'FILITO'), (27, 'FOSFATO'), (28, 'GABRO'),
    (29, 'GALENA'), (30, 'GRANITO'), (31, 'GRANITO ORNAMENTAL'),
    (32, 'HEMATITA'), (33, 'ILMENITA'), (34, 'LATERITA'), (35, 'MAGNETITA'),
    (36, 'MANGANÊS'), (37, 'MINÉRIO DE CHUMBO'), (38, 'MINÉRIO DE COBRE'),
    (39, 'MINÉRIO DE ESTANHO'), (40, 'MINÉRIO DE FERRO'),
    (41, 'MINÉRIO DE MANGANÊS'), (42, 'MINÉRIO DE NIÓBIO'),
    (43, 'MINÉRIO DE NÍQUEL'), (44, 'MINÉRIO DE OURO'),
    (45, 'MINÉRIO DE TITÂNIO'), (46, 'MINÉRIO DE VANDIO'),
    (47, 'MINÉRIO DE ZINCO'), (48, 'MÁRMORE'), (49, 'NÍQUEL'),
    (50, 'OURO'), (51, 'QUARTZITO'), (52, 'QUARTZO'), (53, 'SAIBRO'),
    (54, 'SIENITO'), (55, 'TANTALITA'), (56, 'TITÂNIO'), (57, 'TURFA'),
    (58, 'TURMALINA'), (59, 'TÂNTALO'), (60, 'ZINCO'), (61, 'ÁGUA MINERAL'),
    (62, 'ÁGUA POTÁVEL DE MESA'), (63, 'ÁGUAS TERMAIS'), (64, 'ARGILA COMUM'),
    (65, 'AREIA IN NATURA'), (66, 'GEMA'), (67, 'AREIA QUARTZOSA'),
    (68, 'CALCÁRIO P/ BRITA'), (69, 'AREIA COMUM'), (70, 'ARGILA P/CER. VERMELH'),
    (71, 'PEDRA CALCÁRIA'), (72, 'FERRO'), (73, 'SEIXOS ROLADOS'),
    (74, 'CASCALHO SILICOSO'), (75, 'BASALTO P/ BRITA'), (76, 'GRANITO P/ BRITA'),
    (77, 'MINÉRIO DE PRATA'), (78, 'OURO NATIVO')
    )

d_un_ab = {1: 'ct', 2: 'g', 3: 'kg', 4: 'l', 5: 'm³', 6: 't'}
d_un = {0: 'DADO NÃO CADASTRADO', 1: 'Quilate', 2: 'Grama', 3: 'Quilograma', 4: 'Litro',
        5: 'Metro cúbico', 6: 'Tonelada'}

t_un = ((0, 'DADO NÃO CADASTRADO'), (1, 'Quilate'), (2, 'Grama'), (3, 'Quilograma'), (4, 'Litro'), (5, 'Metro cúbico'), (6, 'Tonelada'))


# Dicionário p/ escolher o dicionário correto pra transf. das colunas catg na função.
d_choices = {
    'atv_1maior_valor': d_atv_ec,
    'atv_2maior_valor': d_atv_ec,
    'atv_3maior_valor': d_atv_ec,
    'tipo_taxa': d_tipos_tx,
    'tipo_atv': d_atv_min,
}

# nomes dos campos no formulários e bd da tabela demografico
d_bd_dm = {
    'dm_pop_total': 'populacao_total',
    'dm_pop_urb': 'populacao_urbana',
    'dm_pop_ru': 'populacao_rural',
}

# nomes dos campos no formulários e bd da tabela economia
d_bd_ec = {
    'ec_pib_pc': 'pib_pc',
    'ec_receitas_fontext': 'receitas_fontext',
    'ec_receitas': 'receitas',
    'ec_despesas': 'despesas',
    'ec_pop_ativa_18mais': 'pop_ativa_18mais',
    'ec_ocup_agropecuario': 'ocup_agropecuario',
    'ec_ocup_comercio': 'ocup_comercio',
    'ec_ocup_construcao': 'ocup_construcao',
    'ec_ocup_mineral': 'ocup_mineral',
    'ec_ocup_industria_utilpub': 'ocup_industria_utilpub',
    'ec_ocup_servic': 'ocup_servic',
    'ec_ocup_industria_transf': 'ocup_industria_transf',
    'ec_ocup_grau_form': 'ocup_grau_form',
    'ec_ocup_fundamental': 'ocup_fundamental',
    'ec_ocup_medio': 'ocup_medio',
    'ec_ocup_superior': 'ocup_superior',
    'ec_atv_1maior_valor': 'atv_1maior_valor',
    'ec_atv_2maior_valor': 'atv_2maior_valor',
    'ec_atv_3maior_valor': 'atv_3maior_valor',
}

# nomes dos campos no formulários e bd da tabela socioeconomico
d_bd_sc = {
    'sc_pop_ocupada': 'pop_ocupada',
    'sc_idhm': 'idhm',
    'sc_idhm_renda': 'idhm_renda',
    'sc_idhm_longevidade': 'idhm_longevidade',
    'sc_idhm_educacao': 'idhm_educacao',
    'sc_expc_vida': 'expc_vida',
    'sc_prob_60anos': 'prob_60anos',
    'sc_expc_anos_estudo18': 'expc_anos_estudo18',
    'sc_renda_pc': 'renda_pc',
    'sc_salario_trab_form': 'salario_trab_form',
    'sc_prop_extr_pobre': 'prop_extr_pobre',
    'sc_prop_pobre': 'prop_pobre',
    'sc_prop_vuln_pobre': 'prop_vuln_pobre',
    'sc_taxa_analfab_15mais': 'taxa_analfab_15mais',
    'sc_ideb_inicias': 'ideb_inicias',
    'sc_ideb_finais': 'ideb_finais',
    'sc_perc_pop_agua_enc': 'perc_pop_agua_enc',
    'sc_perc_pop_coleta_lixo': 'perc_pop_coleta_lixo',
    'sc_perc_pop_eletricidade': 'perc_pop_eletricidade',
    'sc_esg_sanit_adequado': 'esg_sanit_adequado',
    'sc_perc_pop_esg_inadequado': 'perc_pop_esg_inadequado',
    'sc_perc_urban_vias_public': 'perc_urban_vias_public',
}

# nomes dos campos no formulários e bd da tabela arrecadação
d_bd_ar = {

}

t_variaveis_pesq = (
    (0, '-------'), (1, 'Arrecadação CFEM'), (2, 'Quantidade de substrato comercializada'),
    (3, 'Arrecadação TAH'), (4, 'População'), (5, 'População urbana'), (6, 'População rural'),
    (7, 'IDHM'), (8, 'IDHM Renda'), (9, 'IDHM Longevidade'), (10, 'IDHM Educação'),
    (11, 'Expectativa de vida'), (12, 'Probabilidade alcançar 60 anos'),
    (13, 'Expectativa de anos de estudo aos 18 anos'), (14, 'Renda per capita'),
    (15, 'Salario médio do trabalhador formal'), (16, 'População em extrema pobreza (%)'),
    (17, 'População em pobreza (%)'), (18, 'População em vulnerabilidade a pobreza (%)'),
    (19, 'Analfabetismo aos 15 anos ou mais (%)'), (20, 'IDEB anos iniciais'),
    (21, 'IDEB anos finais'), (22, 'População com agua encanada (%)'),
    (23, 'População com coleta lixo (%)'), (24, 'População com eletricidade (%)'),
    (25, 'População com esgoto sanitário adequado (%)'), (26, 'População com esgoto sanitario inadequado (%)'),
    (27, 'Urbanização das vias públicas (%)'), (28, 'PIB per capita'), (29, 'Receitas'), (30, 'Despesas'),
    (31, 'População ativa maior de 18 anos'), (32, 'População ocupada no setor agropecuario (%)'),
    (33, 'População ocupada no setor comercial (%)'), (34, 'População ocupada no setor de construção (%)'),
    (35, 'População ocupada no setor mineral (%)'),
    (36, 'População ocupada no setor de industria de utilidade pública (%)'),
    (37, 'População ocupada no setor de industria de transformação (%)'),
    (38, 'População ocupada no setor de serviços (%)'),
    (39, 'Grau de formalização do trabalho das pessoas ocupadas (%)'),
    (40, 'População ocupada com ensino fundamental completo (%)'),
    (41, 'População ocupada com ensino médio completo (%)'),
    (42, 'População ocupada com ensino superior completo (%)')
)

d_variaveis_pesq = {
    0: '-------', 1: 'Arrecadação CFEM', 2: 'Quantidade de substrato comercializada',
    3: 'Arrecadação TAH', 4: 'População', 5: 'População urbana', 6: 'População rural',
    7: 'IDHM', 8: 'IDHM Renda', 9: 'IDHM Longevidade', 10: 'IDHM Educação',
    11: 'Expectativa de vida', 12: 'Probabilidade alcançar 60 anos',
    13: 'Expectativa de anos de estudo aos 18 anos', 14: 'Renda per capita',
    15: 'Salario médio do trabalhador formal', 16: 'População em extrema pobreza (%)',
    17: 'População em pobreza (%)', 18: 'População em vulnerabilidade a pobreza (%)',
    19: 'Analfabetismo aos 15 anos ou mais (%)', 20: 'IDEB anos iniciais', 21: 'IDEB anos finais',
    22: 'População com agua encanada (%)', 23: 'População com coleta lixo (%)',
    24: 'População com eletricidade (%)', 25: 'População com esgoto sanitário adequado (%)',
    26: 'População com esgoto sanitario inadequado (%)', 27: 'Urbanização das vias públicas (%)',
    28: 'PIB per capita', 29: 'Receitas', 30: 'Despesas', 31: 'População ativa maior de 18 anos',
    32: 'População ocupada no setor agropecuario (%)', 33: 'População ocupada no setor comercial (%)',
    34: 'População ocupada no setor de construção (%)', 35: 'População ocupada no setor mineral (%)',
    36: 'População ocupada no setor de industria de utilidade pública (%)',
    37: 'População ocupada no setor de industria de transformação (%)',
    38: 'População ocupada no setor de serviços (%)',
    39: 'Grau de formalização do trabalho das pessoas ocupadas (%)',
    40: 'População ocupada com ensino fundamental completo (%)',
    41: 'População ocupada com ensino médio completo (%)',
    42: 'População ocupada com ensino superior completo (%)'
}

d_variaveis_db = {
    0: '-------', 1: 'valor', 2: ['quantidade', 'unidade'],
    3: 'valorPago', 4: 'populacao_total', 5: 'populacao_urbana', 6: 'populacao_rural',
    7: 'idhm', 8: 'idhm_renda', 9: 'idhm_longevidade', 10: 'idhm_educacao',
    11: 'expc_vida', 12: 'prob_60anos', 13: 'expc_anos_estudo18', 14: 'renda_pc',
    15: 'salario_trab_form', 16: 'prop_extr_pobre', 17: 'prop_pobre',
    18: 'prop_vuln_pobre', 19: 'taxa_analfab_15mais', 20: 'ideb_inicias',
    21: 'ideb_finais', 22: 'perc_pop_agua_enc', 23: 'perc_pop_coleta_lixo',
    24: 'perc_pop_eletricidade', 25: 'esg_sanit_adequado', 26: 'perc_pop_esg_inadequado',
    27: 'perc_urban_vias_public', 28: 'pib_pc', 29: 'receitas', 30: 'despesas',
    31: 'pop_ativa_18mais', 32: 'ocup_agropecuario', 33: 'ocup_comercio',
    34: 'ocup_construcao', 35: 'ocup_mineral', 36: 'ocup_industria_utilpub',
    37: 'ocup_industria_transf', 38: 'ocup_servic', 39: 'ocup_grau_form',
    40: 'ocup_fundamental', 41: 'ocup_medio', 42: 'ocup_superior'
}

d_variaveis_calc = {
    'soma' : [1, 2, 3, 29, 30, 31],
    'proporcao': [11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41],
    'idhm': [7, 8, 9, 10],
    'ideb': [20, 21],
    'pib_pc': 28,
    # 11, 12 e 13 expectativa de vida, probabildiade de 60 anos e expc de estudo
    # 15 salario trabalhador formal
    #
}

# nome da chave estrangeira do id da cidade no bd
cid_id = 'cidade_id'

# tupla p/ usar limitar o choices do modelo
t_tipos_tx = (
    (1, 'TAH'),
    (2, 'CFEM'),
)

# tupla p/ usar limitar o choices do modelo
t_atv_min = (
    (0, '-------'),
    (1, 'Água Mineral/Potável'),
    (2, 'Calcário'),
    (3, 'Calcário Calcítico'),
    (4, 'Calcário Dolomítico'),
    (5, 'Água Termal'),
    (6, 'Granito/Brita'),
    (7, 'Minério de Manganês'),
    (8, 'Minério de Ouro/Ouro'),
    (9, 'Gema/Diamantes'),
    (10, 'Argila'),
    (11, 'Areia'),
)

# tupla p/ usar limitar o choices do modelo
# t_atv_ec = (
#     (1, 'Indústrias de transformação'),
#     (2, 'Indústrias extrativas'),
#     (3, 'Construção'),
#     (4, 'Agricultura, inclusive apoio à agricultura e a pós colheita'),
#     (5, 'Administração, educação, saúde, pesquisa e desenvolvimento públicas, defesa, seguridade social'),
#     (6, 'Comércio e reparação de veículos automotores e motocicletas'),
#     (7, 'Produção florestal, pesca e aquicultura'),
#     (8, 'Pecuária, inclusive apoio à pecuária'),
#     (9, 'Eletricidade e gás, água, esgoto, atividades de gestão de resíduos e descontaminação'),
#     (10, 'Demais serviços'),
# )

t_atv_ec = (
    (0, 'Sem registro'),
    (1, 'Administração, defesa, educação e saúde públicas e seguridade social'),
    (2, 'Agricultura, inclusive apoio à agricultura e a pós colheita'),
    (3, 'Comércio e reparação de veículos automotores e motocicletas'),
    (4, 'Construção'),
    (5, 'Demais serviços'),
    (6, 'Eletricidade e gás, água, esgoto, atividades de gestão de resíduos e descontaminação'),
    (7, 'Indústrias de transformação'),
    (8, 'Indústrias extrativas'),
    (9, 'Pecuária, inclusive apoio à pecuária'),
    (10, 'Produção florestal, pesca e aquicultura')
)

t_meses = (
    (1, 'janeiro'),
    (2, 'fevereiro'),
    (3, 'março'),
    (4, 'abril'),
    (5, 'maio'),
    (6, 'junho'),
    (7, 'julho'),
    (8, 'agosto'),
    (9, 'setembro'),
    (10, 'outubro'),
    (11, 'novembro'),
    (12, 'dezembro'),
)

cols = {
    'UF': '',
    'Codmun7': 'cod_mun',
    'ESPVIDA': 'expc_vida',
    'SOBRE60': 'prob_60anos',
    'E_ANOSESTUDO': 'expc_anos_estudo18',
    'T_ANALF15M': 'taxa_analfab_15mais',
    'PIND': 'prop_extr_pobre',
    'PMPOB': 'prop_pobre',
    'PPOBCRI': 'prop_vuln_pobre',
    'P_AGRO': 'ocup_agropecuario',
    'P_COM': 'ocup_comercio',
    'P_CONSTR': 'ocup_construcao',
    'P_EXTR': 'ocup_mineral',
    'P_FORMAL': 'ocup_grau_form',
    'P_FUND': 'ocup_fundamental',
    'P_MED': 'ocup_medio',
    'P_SUPER': 'ocup_superior',
    'P_SERV': 'ocup_servic',
    'P_SIUP': 'ocup_industria_utilpub',
    'P_TRANSF': 'ocup_industria_transf',
    'T_AGUA': 'perc_pop_agua_enc',
    'T_BANAGUA': 'esg_sanit_adequado',
    'T_LIXO': 'perc_pop_coleta_lixo',
    'T_LUZ': 'perc_pop_eletricidade',
    'AGUA_ESGOTO': 'perc_pop_esg_inadequado',
    'IDHM': 'idhm',
    'IDHM_E': 'idhm_educacao',
    'IDHM_R': 'idhm_renda',
    'IDHM_L': 'idhm_longevidade',
    'pesourb': 'populacao_urbana',
    'pesoRUR': 'populacao_rural',
    'pesotot': 'populacao_total',
    'PEA18M': 'pop_ativa_18mais',
    'RDPC': 'renda_pc',
    'ANO': 'ano'
}

VIS_MESORREGIAO = 0
VIS_MICRORREGIAO = 1
VIS_PROVINCIA = 2
VIS_MUNICIPIOS = 3


# cria tupla dos anos
def ano_chs():
    return ((r,r) for r in range(datetime.date.today().year, 1969, -1))


# retorna ano atual
def ano_atual():
    return datetime.date.today().year
