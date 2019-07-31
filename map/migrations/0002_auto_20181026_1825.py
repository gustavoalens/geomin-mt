# Generated by Django 2.1.1 on 2018-10-26 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrecadacao',
            name='ano',
            field=models.IntegerField(choices=[(2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991)], default=2018),
        ),
        migrations.AlterField(
            model_name='demografico',
            name='ano',
            field=models.IntegerField(choices=[(2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991)], default=2018),
        ),
        migrations.AlterField(
            model_name='economia',
            name='ano',
            field=models.IntegerField(choices=[(2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991)], default=2018),
        ),
        migrations.AlterField(
            model_name='economia',
            name='atv_1maior_valor',
            field=models.IntegerField(choices=[(1, 'Indústrias de transformação'), (2, 'Indústrias extrativas'), (3, 'Construção'), (4, 'Agricultura, inclusive apoio à agricultura e a pós colheita'), (5, 'Administração, educação, saúde, pesquisa e desenvolvimento públicas, defesa, seguridade social'), (6, 'Comércio e reparação de veículos automotores e motocicletas'), (7, 'Produção florestal, pesca e aquicultura'), (8, 'Pecuária, inclusive apoio à pecuária'), (9, 'Eletricidade e gás, água, esgoto, atividades de gestão de resíduos e descontaminação'), (10, 'Demais serviços')], null=True),
        ),
        migrations.AlterField(
            model_name='economia',
            name='atv_2maior_valor',
            field=models.IntegerField(choices=[(1, 'Indústrias de transformação'), (2, 'Indústrias extrativas'), (3, 'Construção'), (4, 'Agricultura, inclusive apoio à agricultura e a pós colheita'), (5, 'Administração, educação, saúde, pesquisa e desenvolvimento públicas, defesa, seguridade social'), (6, 'Comércio e reparação de veículos automotores e motocicletas'), (7, 'Produção florestal, pesca e aquicultura'), (8, 'Pecuária, inclusive apoio à pecuária'), (9, 'Eletricidade e gás, água, esgoto, atividades de gestão de resíduos e descontaminação'), (10, 'Demais serviços')], null=True),
        ),
        migrations.AlterField(
            model_name='economia',
            name='atv_3maior_valor',
            field=models.IntegerField(choices=[(1, 'Indústrias de transformação'), (2, 'Indústrias extrativas'), (3, 'Construção'), (4, 'Agricultura, inclusive apoio à agricultura e a pós colheita'), (5, 'Administração, educação, saúde, pesquisa e desenvolvimento públicas, defesa, seguridade social'), (6, 'Comércio e reparação de veículos automotores e motocicletas'), (7, 'Produção florestal, pesca e aquicultura'), (8, 'Pecuária, inclusive apoio à pecuária'), (9, 'Eletricidade e gás, água, esgoto, atividades de gestão de resíduos e descontaminação'), (10, 'Demais serviços')], null=True),
        ),
        migrations.AlterField(
            model_name='operacao_empresa',
            name='ano',
            field=models.IntegerField(choices=[(2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991)], default=2018),
        ),
        migrations.AlterField(
            model_name='pessoa_fisica',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='pessoa_juridica',
            name='atividade_mineradora',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pessoa_juridica',
            name='cidades_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='map.cidades'),
        ),
        migrations.AlterField(
            model_name='pessoa_juridica',
            name='cnpj',
            field=models.CharField(max_length=18, unique=True),
        ),
        migrations.AlterField(
            model_name='pessoa_juridica',
            name='cooperativa',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pessoa_juridica',
            name='nomefantasia',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='socioeconomico',
            name='ano',
            field=models.IntegerField(choices=[(2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991)], default=2018),
        ),
        migrations.AlterField(
            model_name='titulos_minerarios',
            name='ano',
            field=models.IntegerField(choices=[(2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991)], default=2018),
        ),
        migrations.AlterField(
            model_name='titulos_minerarios',
            name='subs',
            field=models.IntegerField(choices=[(0, 'DADO NÃO CADASTRADO'), (1, 'AMETISTA'), (2, 'AREIA'), (3, 'AREIA LAVADA'), (4, 'ARENITO'), (5, 'ARGILA'), (6, 'BASALTO'), (7, 'BRITA DE GRANITO'), (8, 'CALCEDÔNIA'), (9, 'CALCÁRIO'), (10, 'CALCÁRIO CALCÍTICO'), (11, 'CALCÁRIO DOLOMÍTICO'), (12, 'CALCÁRIO INDUSTRIAL'), (13, 'CASCALHO'), (14, 'CASCALHO DIAMANTÍFERO'), (15, 'CASSITERITA'), (16, 'CAULIM'), (17, 'CHUMBO'), (18, 'COBRE'), (19, 'COLUMBITA'), (20, 'CONGLOMERADO'), (21, 'DIAMANTE'), (22, 'DIAMANTE INDUSTRIAL'), (23, 'DOLOMITO'), (24, 'ESTANHO'), (25, 'FELDSPATO'), (26, 'FILITO'), (27, 'FOSFATO'), (28, 'GABRO'), (29, 'GALENA'), (30, 'GRANITO'), (31, 'GRANITO ORNAMENTAL'), (32, 'HEMATITA'), (33, 'ILMENITA'), (34, 'LATERITA'), (35, 'MAGNETITA'), (36, 'MANGANÊS'), (37, 'MINÉRIO DE CHUMBO'), (38, 'MINÉRIO DE COBRE'), (39, 'MINÉRIO DE ESTANHO'), (40, 'MINÉRIO DE FERRO'), (41, 'MINÉRIO DE MANGANÊS'), (42, 'MINÉRIO DE NIÓBIO'), (43, 'MINÉRIO DE NÍQUEL'), (44, 'MINÉRIO DE OURO'), (45, 'MINÉRIO DE TITÂNIO'), (46, 'MINÉRIO DE VANDIO'), (47, 'MINÉRIO DE ZINCO'), (48, 'MÁRMORE'), (49, 'NÍQUEL'), (50, 'OURO'), (51, 'QUARTZITO'), (52, 'QUARTZO'), (53, 'SAIBRO'), (54, 'SIENITO'), (55, 'TANTALITA'), (56, 'TITÂNIO'), (57, 'TURFA'), (58, 'TURMALINA'), (59, 'TÂNTALO'), (60, 'ZINCO'), (61, 'ÁGUA MINERAL'), (62, 'ÁGUA POTÁVEL DE MESA'), (63, 'ÁGUAS TERMAIS')]),
        ),
        migrations.AlterField(
            model_name='titulos_minerarios',
            name='uso',
            field=models.IntegerField(choices=[(0, 'DADO NÃO CADASTRADO'), (1, 'Artesanato  mineral'), (2, 'Balneoterapia'), (3, 'Brita'), (4, 'Cerâmica vermelha'), (5, 'Construção civil'), (6, 'Corretivo de solo'), (7, 'Energético'), (8, 'Engarrafamento'), (9, 'Fabricação de cal'), (10, 'Fabricação de cimento'), (11, 'Fertilizantes'), (12, 'Gema'), (13, 'Industrial'), (14, 'Insumo agrícola'), (15, 'Metalurgia'), (16, 'Não informado'), (17, 'Ourivesaria'), (18, 'Pedra de coleção'), (19, 'Pedra decorativa'), (20, 'Revestimento')]),
        ),
    ]
