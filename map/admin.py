from django.contrib import admin
from map.models import mesorregioes, microrregioes, cidades, titulos_minerarios,\
socioeconomico, economia, demografico, arrecadacao, pessoa_juridica, pessoa_fisica, operacao_empresa

# Register your models here.

admin.site.register(mesorregioes)
admin.site.register(microrregioes)
admin.site.register(cidades)
admin.site.register(titulos_minerarios)
admin.site.register(socioeconomico)
admin.site.register(economia)
admin.site.register(demografico)
admin.site.register(arrecadacao)
admin.site.register(pessoa_juridica)
admin.site.register(pessoa_fisica)
admin.site.register(operacao_empresa)
