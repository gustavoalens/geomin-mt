# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.gis.db import models
from . import constantes as ct


# Create your models here.


class rodovias(models.Model):
    codigo = models.CharField(max_length=12, null=True)
    geom = models.MultiLineStringField(srid=4326)
    tipo_pavimento = models.CharField(max_length=50, null=True, default=None)

class ferrovias(models.Model):
    geom = models.MultiLineStringField(srid=4326)
    situacao = models.CharField(max_length=80, null=True, default=None)

class hidrovias(models.Model):
    geom = models.MultiLineStringField(srid=4326)
    situacao = models.CharField(max_length=50, null=True, default=None)

class aerodromos(models.Model):
    geom = models.MultiPointField(srid=4326)
    pavimento = models.CharField(max_length=25, null=True, default=None)

class mesorregioes(models.Model):
    nome = models.CharField(max_length=100)
    geom = models.GeometryField(srid=4326)

    def __str__(self):
        return self.nome


class microrregioes(models.Model):
    nome = models.CharField(max_length=100)
    geom = models.GeometryField(srid=4326)

    def __str__(self):
        return self.nome


class cidades(models.Model):
    nome = models.CharField(max_length=60)
    geom = models.GeometryField(srid=4326)

    def __str__(self):
        return self.nome.title()


class socioeconomico(models.Model):
    # remover pop_ocupada
    pop_ocupada = models.FloatField(null=True)
    idhm = models.FloatField(null=True)
    idhm_renda = models.FloatField(null=True)
    idhm_longevidade = models.FloatField(null=True)
    idhm_educacao = models.FloatField(null=True)
    expc_vida = models.FloatField(null=True)
    prob_60anos = models.FloatField(null=True)
    expc_anos_estudo18 = models.FloatField(null=True)
    renda_pc = models.FloatField(null=True)
    salario_trab_form = models.FloatField(null=True)
    prop_extr_pobre = models.FloatField(null=True)
    prop_pobre = models.FloatField(null=True)
    prop_vuln_pobre = models.FloatField(null=True)
    taxa_analfab_15mais = models.FloatField(null=True)
    # criar uma nova tabelap ro ideb?
    ideb_inicias = models.FloatField(null=True)
    ideb_finais = models.FloatField(null=True)

    perc_pop_agua_enc = models.FloatField(null=True)
    perc_pop_coleta_lixo = models.FloatField(null=True)
    perc_pop_eletricidade = models.FloatField(null=True)
    # padronizar o nome
    esg_sanit_adequado = models.FloatField(null=True)
    # remover perc_pop_esg_inadequado
    perc_pop_esg_inadequado = models.FloatField(null=True)
    perc_urban_vias_public = models.FloatField(null=True)
    ano = models.IntegerField(choices=ct.ano_chs(), default=ct.ano_atual())
    cidade = models.ForeignKey(cidades, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.cidade} : {self.ano}'

# mudar o nome pra economico
class economia(models.Model):

    # adicionar pib
    pib_pc = models.FloatField(null=True)
    receitas_fontext = models.FloatField(null=True)
    receitas = models.FloatField(null=True)
    despesas = models.FloatField(null=True)
    # utilizar pop_ativa como referencia pra achar total inteiro dos ocupados
    pop_ativa_18mais = models.IntegerField(null=True)
    # remover pop_ocupada
    # pop_ocupada = models.IntegerField(null=True) # calculada a partir da pop_ocupada da socioeconomico
    ocup_agropecuario = models.FloatField(null=True)
    ocup_comercio = models.FloatField(null=True)
    ocup_construcao = models.FloatField(null=True)
    ocup_mineral = models.FloatField(null=True)
    ocup_industria_utilpub = models.FloatField(null=True)
    ocup_servic = models.FloatField(null=True)
    ocup_industria_transf = models.FloatField(null=True)
    ocup_grau_form = models.FloatField(null=True)
    ocup_fundamental = models.FloatField(null=True)
    ocup_medio = models.FloatField(null=True)
    ocup_superior = models.FloatField(null=True)
    atv_1maior_valor = models.IntegerField(null=True, choices=ct.t_atv_ec)
    atv_2maior_valor = models.IntegerField(null=True, choices=ct.t_atv_ec)
    atv_3maior_valor = models.IntegerField(null=True, choices=ct.t_atv_ec)
    ano = models.IntegerField(choices=ct.ano_chs(), default=ct.ano_atual())
    cidade = models.ForeignKey(cidades, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.cidade} : {self.ano}'


class demografico(models.Model):
    populacao_urbana = models.IntegerField(null=True)
    populacao_rural = models.IntegerField(null=True)
    populacao_total = models.IntegerField()
    ano = models.IntegerField(choices=ct.ano_chs(), default=ct.ano_atual())
    cidade = models.ForeignKey(cidades, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.cidade} : {self.ano}'


# classe não mais utilizada
class arrecadacao(models.Model):

    total = models.FloatField()
    tipo_taxa = models.IntegerField(choices=ct.t_tipos_tx, default=1)
    tipo_atv = models.IntegerField(choices=ct.t_atv_min, default=1)
    mes = models.IntegerField(choices=ct.t_meses, default=1)
    ano = models.IntegerField(choices=ct.ano_chs(), default=ct.ano_atual())
    cidade = models.ForeignKey(cidades, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.cidade} : {ct.t_atv_min[self.tipo_atv - 1][1]} : {self.ano}'


class pessoa_juridica(models.Model):
    cnpj = models.CharField(max_length=18, unique=True)
    razaosocial = models.CharField(max_length=150)
    nomefantasia = models.CharField(max_length=150, null=True)
    # atividade_mineradora = models.IntegerField(null=True)
    cooperativa = models.BooleanField(default=False)
    # cidade = models.ForeignKey(cidades, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.razaosocial


class pessoa_fisica(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome.title()


# por ora não está sendo utilizada
class operacao_empresa(models.Model):
    total = models.FloatField()
    ano = models.IntegerField(choices=ct.ano_chs(), default=ct.ano_atual())
    pessoa_juridica = models.ForeignKey(pessoa_juridica, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.pessoa_juridica}'


class titulos_minerarios(models.Model):
    # processo = models.CharField(max_length=11)
    numero = models.IntegerField(default=0)
    ano = models.IntegerField(choices=ct.ano_chs(), default=ct.ano_atual())
    fase = models.IntegerField(choices=ct.t_fase)
    ult_evento = models.CharField(max_length=254)
    nome_prop = models.CharField(max_length=254)
    subs = models.IntegerField(choices=ct.t_subs_tm)
    uso = models.IntegerField(choices=ct.t_uso_tm)
    geom = models.GeometryField(srid=4326)
    pessoa_fisica = models.ForeignKey(pessoa_fisica, null=True, on_delete=models.SET_NULL)
    pessoa_juridica = models.ForeignKey(pessoa_juridica, null=True, on_delete=models.SET_NULL)
    cidade = models.ForeignKey(cidades, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.numero}/{self.ano}'


class tah(models.Model):
    valorCobrado = models.FloatField()
    valorPago = models.FloatField()
    numProcesso = models.IntegerField()
    anoProcesso = models.IntegerField()
    pessoa_fisica = models.ForeignKey(pessoa_fisica, null=True, on_delete=models.SET_NULL)
    pessoa_juridica = models.ForeignKey(pessoa_juridica, null=True, on_delete=models.SET_NULL)
    titulos_minerarios = models.ForeignKey(titulos_minerarios, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        res = ''
        if self.pessoa_juridica:
            res = f'{self.pessoa_juridica}'
        elif self.pessoa_fisica:
            res = f'{self.pessoa_juridica}'

        res += f'{self.titulos_minerarios}'
        return res


class cfem(models.Model):
    unidade = models.IntegerField(choices=ct.t_un)
    quantidade = models.FloatField()
    valor = models.FloatField()
    subs = models.IntegerField(choices=ct.t_subs)
    num_proc = models.IntegerField()
    ano_proc = models.IntegerField()
    ano = models.IntegerField()
    pessoa_fisica = models.ForeignKey(pessoa_fisica, null=True, on_delete=models.SET_NULL)
    pessoa_juridica = models.ForeignKey(pessoa_juridica, null=True, on_delete=models.SET_NULL)
    titulos_minerarios = models.ForeignKey(titulos_minerarios, null=True, on_delete=models.SET_NULL)
    cidade = models.ForeignKey(cidades, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        res = ''
        if self.pessoa_juridica:
            res = f'{self.pessoa_juridica}'
        elif self.pessoa_fisica:
            res = f'{self.pessoa_juridica}'

        res += f'{self.titulos_minerarios}'
        return res
