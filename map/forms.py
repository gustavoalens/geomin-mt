# -*- coding: utf-8 -*-
from django import forms
from .models import cidades, microrregioes, demografico, economia, \
    socioeconomico, arrecadacao, titulos_minerarios
from . import constantes as ct

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Div, Field, Row


class FormConsulta(forms.Form):

    # Campos de escolha para Demográfico
    dm = forms.BooleanField(label='Demográfico', required=False)
    # dm_todos = forms.BooleanField(label='Todos', required=False)
    dm_pop_total = forms.BooleanField(label='População total', required=False)
    dm_pop_urb = forms.BooleanField(label='População urbana', required=False)
    dm_pop_ru = forms.BooleanField(label='População rural', required=False)

    # Campos de escolha para Econômico
    ec = forms.BooleanField(label='Econômico', required=False)
    ec_todos = forms.BooleanField(label='Todos', required=False)
    ec_pib_pc = forms.BooleanField(label='PIB per capita', required=False)
    ec_receitas_fontext = forms.BooleanField(label='Receitas de Fonte Externa', required=False)
    ec_receitas = forms.BooleanField(label='Receitas', required=False)
    ec_despesas = forms.BooleanField(label='Despesas', required=False)
    ec_pop_ativa_18mais = forms.BooleanField(label='População ativa maior de 18 anos (%)', required=False)
    ec_ocup_agropecuario = forms.BooleanField(label='População ocupada no setor agropecuario (%)', required=False)
    ec_ocup_comercio = forms.BooleanField(label='População ocupada no setor comercial (%)', required=False)
    ec_ocup_construcao = forms.BooleanField(label='População ocupada no setor de construção (%)', required=False)
    ec_ocup_mineral = forms.BooleanField(label='População ocupada no setor extrativo mineral (%)', required=False)
    ec_ocup_industria_utilpub = forms.BooleanField(label='População ocupada no setor de serviços ind. de util. pub. (%)', required=False)
    ec_ocup_servic = forms.BooleanField(label='População ocupada no setor de serviços (%)', required=False)
    ec_ocup_industria_transf = forms.BooleanField(label='População ocupada na indústria de transf. (%)', required=False)
    ec_ocup_grau_form = forms.BooleanField(label='Grau de formalização do trabalho', required=False)
    ec_ocup_fundamental = forms.BooleanField(label='Ocupados com ens. fundamental completo (%)', required=False)
    ec_ocup_medio = forms.BooleanField(label='Ocupados com ens. médio completo (%)', required=False)
    ec_ocup_superior = forms.BooleanField(label='Ocupados com ens. superior completo (%)', required=False)
    ec_atv_1maior_valor = forms.BooleanField(label='Atividade com segundo maior valor adicionado bruto', required=False)
    ec_atv_2maior_valor = forms.BooleanField(label='Atividade com segundo maior valor adicionado bruto', required=False)
    ec_atv_3maior_valor = forms.BooleanField(label='Atividade com terceiro maior valor adicionado bruto', required=False)

    # Campos de escolha para Socioeconômico
    sc = forms.BooleanField(label='Socioeconômico', required=False)
    sc_todos = forms.BooleanField(label='Todos', required=False)
    sc_pop_ocupada = forms.BooleanField(label='População ocupada (%)', required=False)
    sc_idhm = forms.BooleanField(label='IDHM', required=False)
    sc_idhm_renda = forms.BooleanField(label='IDHM-Renda', required=False)
    sc_idhm_longevidade = forms.BooleanField(label='IDHM-Longevidade', required=False)
    sc_idhm_educacao = forms.BooleanField(label='IDHM-Educação', required=False)
    sc_expc_vida = forms.BooleanField(label='Esperança de vida ao nascer', required=False)
    sc_prob_60anos = forms.BooleanField(label='Probabilidade de sobrevivência até 60 anos', required=False)
    sc_expc_anos_estudo18 = forms.BooleanField(label='Expectativa de anos de estudo aos 18 anos de idade', required=False)
    sc_renda_pc = forms.BooleanField(label='Renda Per capita', required=False)
    sc_salario_trab_form = forms.BooleanField(label='Salário médio mensal dos trabalhadores formais', required=False)
    sc_prop_extr_pobre = forms.BooleanField(label='Proporção de extremamente pobres', required=False)
    sc_prop_pobre = forms.BooleanField(label='Proporção de pobres', required=False)
    sc_prop_vuln_pobre = forms.BooleanField(label='Proporção de vulneráveis à pobreza', required=False)
    sc_taxa_analfab_15mais = forms.BooleanField(label='Taxa de analfabetismo da população de 15 anos ou mais de idade (%)', required=False)
    sc_ideb_inicias = forms.BooleanField(label='IDEB – Anos iniciais do ensino fundamental', required=False)
    sc_ideb_finais = forms.BooleanField(label='IDEB – Anos finais do ensino fundamental', required=False)
    sc_perc_pop_agua_enc = forms.BooleanField(label='Percentual da população que vive em domicílios com água encanada', required=False)
    sc_perc_pop_coleta_lixo = forms.BooleanField(label='Percentual da população que vive em domicílios urbanos com serviço de coleta de lixo', required=False)
    sc_perc_pop_eletricidade = forms.BooleanField(label='Percentual da população que vive em domicílios com energia elétrica', required=False)
    sc_esg_sanit_adequado = forms.BooleanField(label='Esgotamento sanitário adequado (%)', required=False)
    sc_perc_pop_esg_inadequado = forms.BooleanField(label='Pessoas em domicílios com abastecimento de água e esgotamento sanitário inadequados (%)', required=False)
    sc_perc_urban_vias_public = forms.BooleanField(label='Urbanização de vias públicas (%)', required=False)

    # Campos de escolha para Arrecadação
    ar = forms.BooleanField(label='Arrecadação', required=False)
    ar_subs = forms.ChoiceField(label='Substrato', choices=ct.t_subs)

    # Campos para filtragem dos anos na busca
    ano_i = forms.ChoiceField(label='Ano inicial', choices=ct.ano_chs())
    ano_f = forms.ChoiceField(label='Ano final', choices=ct.ano_chs())

class FormSubs(forms.Form):
    subs = forms.ChoiceField(label='Tipo de substrato', choices=ct.t_subs[1:], required=False)


FormsetSubs = forms.formset_factory(FormSubs, extra=0)


class FormUsos(forms.Form):
    usos = forms.ChoiceField(label='Tipo de uso', choices=ct.t_uso_tm[2:], required=False)

FormsetUsos = forms.formset_factory(FormUsos, extra=0)

# }
# formset_subs = FormsetSubs(data)

class FormTitulo(forms.ModelForm):
    # cpf = forms.CharField(label='CPF', max_length=11, required=False)
    # cnpj = forms.CharField(label='CNPJ', max_length=14, required=False)

    # t_subs = titulos_minerarios.objects.values('subs')
    # print(t_subs)
    # numero = forms.IntegerField(label='Número do processo', required=False)
    # ano = forms.ChoiceField(label='Ano do processo', choices=ct.ano_chs(), required=False)
    # subs = forms.ChoiceField(label='Tipo de substrato', choices=ct.t_subs_tm, required=False)
    # uso = forms.ChoiceField(label='Tipo de uso', choices=ct.t_uso_tm, required=False)


    class Meta:
        model = titulos_minerarios
        fields = [
            'numero', 'ano',
            'subs', 'uso', 'pessoa_fisica',
            'pessoa_juridica'
        ]

        labels = {
            'numero': 'Número do processo',
            'ano': 'Ano do processo',
            'subs': 'Tipo de substrato',
            'uso': 'Tipo de uso',
            'pessoa_fisica': 'Pessoa Fisica',
            'pessoa_juridica': 'Pessoa Jurídica'
        }

    # pf = forms.BooleanField(label='Pessoa Física', required=False)
    # pj = forms.BooleanField(label='Pessoa Jurídica', required=False)


    form_subs = FormsetSubs(prefix='fsubs') # check
    form_usos = FormsetUsos(prefix='fusos')

    pesq_num_ano = forms.BooleanField(label='Pesquisar por Número/Ano', required=False)
    pesq_pf_pj = forms.BooleanField(label='Pesquisar por Pessoa Física/Jurídica', required=False)
    pes_c = (
        (1, 'Pessoa Física'),
        (2, 'Pessoa Jurídica'),
        )
    pes = forms.ChoiceField(label= '', widget=forms.RadioSelect, choices=pes_c, required=False)

    def __init__(self, *args, **kwargs):
        super(FormTitulo, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].required = False

        # ToDo: checar como deixar vazio o campo de IntegerField
        # ToDo: checar o que fazer com o ano do processo


# FormsetTitulo = forms.formset_factory(FormTitulo, formset=BaseSubs, can_delete=True)

class FormVars(forms.Form):

    t_rep = (
        (0, 'Linha'),
        (1, 'Barra'),
    )

    t_vars = ct.t_variaveis_pesq
    t_vars = tuple(filter(lambda x: x if x[0] != 3 else None, t_vars))
    vars = forms.ChoiceField(label='Variável', choices=t_vars, required=False)
    rep = forms.ChoiceField(label='Tipo', choices=t_rep, required=False)

    def __init__(self, *args, **kwargs):
        super(FormVars, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Field('vars', wrapper_class='col-md-7', style='margin-right: 0'),
                Field('rep', wrapper_class='col-md-4', style='margin-left: 0; margin-right: 0'),
                id='teste', name='teste'
            )
        )

    # vars.widget.attrs.update({'class': 'col-md-4 select form-control'})
    # rep.widget.attrs.update({'class': 'col-md-2 select form-control'})

FormsetVars = forms.formset_factory(FormVars, extra=0)


class FormAnalisar(forms.Form):
    dados_c = (
        (1, 'Demográfico'),
        (2, 'Econômico'),
        (3, 'Socioeconômico'),
        # (4, 'Arrecadação'),
        )

    t_tipo_analise = (
        (1, 'Substratos por região'),
        (2, 'Cruzar dados por substrato'),
        (3, 'Apresentar dado no mapa'),
        (4, 'Temporal'),
    )

    t_opc_arr = (
        (1, 'Total'),
        (2, 'Por substrato'),
    )

    tipo_analise = forms.ChoiceField(label='', widget=forms.RadioSelect, choices=t_tipo_analise, required=False)
    # all_subs = forms.BooleanField(label='Substratos x Região', required=False)
    # cruzar = forms.BooleanField(label='Cruzar dados por substrato', required=False)
    subs_cr = forms.ChoiceField(label='Tipo de substrato', choices=ct.t_subs, required=False)
    dados = forms.ChoiceField(label='Cruzar com:', widget=forms.RadioSelect, choices=dados_c, required=False)
    ano_i = forms.ChoiceField(label='Ano inicial', choices=ct.ano_chs(), required=False)
    ano_f = forms.ChoiceField(label='Ano final', choices=ct.ano_chs(), required=False)

    ano_i_t = forms.ChoiceField(label='Ano inicial', choices=ct.ano_chs(), required=False)
    ano_f_t = forms.ChoiceField(label='Ano final', choices=ct.ano_chs(), required=False)
    # apresentar = forms.BooleanField(label='Apresentar dado no mapa', required=False)
    variavel = forms.ChoiceField(label='Variável', choices=ct.t_variaveis_pesq, required=False)
    opc_arr = forms.ChoiceField(label='', widget=forms.RadioSelect, choices=t_opc_arr, required=False)
    subs_ap = forms.ChoiceField(label='Tipo de substrato', choices=ct.t_subs, required=False)
    ano_v = forms.ChoiceField(label='Ano', choices=ct.ano_chs(), required=False)
    ano = forms.ChoiceField(label='Ano', choices=ct.ano_chs(), required=False)

    form_vars = FormsetVars(prefix='fvars')
