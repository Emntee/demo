# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BleachingRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('length', models.FloatField(verbose_name='长度', default=0)),
                ('price', models.FloatField(verbose_name='单价', default=0)),
                ('sum_price', models.FloatField(verbose_name='金额', default=0)),
                ('created_at', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('design_drawing_price', models.FloatField(verbose_name='打样费')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='客户', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveringRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('delivery_date', models.DateField(verbose_name='发货日期')),
                ('length', models.FloatField(verbose_name='发货长度')),
                ('roll_count', models.IntegerField(verbose_name='发货卷数')),
                ('roll_id', models.TextField(verbose_name='卷号')),
                ('sum_price', models.FloatField(verbose_name='运费')),
                ('price', models.FloatField(verbose_name='运输单价')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveringSummury',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('roll_sum', models.IntegerField(verbose_name='发货卷数', default=0)),
                ('length', models.FloatField(verbose_name='发货总长度', default=0)),
                ('sum_price', models.FloatField(verbose_name='运费总额', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('texture', models.CharField(verbose_name='花号', max_length=32, unique=True)),
                ('order_date', models.DateField(verbose_name='接单日期', blank=True, null=True)),
                ('contract_date', models.DateField(verbose_name='合同定期', blank=True, null=True)),
                ('specification', models.CharField(verbose_name='规格', max_length=20, blank=True, null=True)),
                ('client', models.CharField(verbose_name='客户', max_length=40, blank=True, null=True)),
                ('order_price', models.FloatField(verbose_name='接单单价', blank=True, null=True)),
                ('ends_per_inch', models.FloatField(verbose_name='经密', blank=True, null=True)),
                ('picks_per_inch', models.FloatField(verbose_name='纬密', blank=True, null=True)),
                ('order_quantity', models.IntegerField(verbose_name='合同数量', blank=True, null=True)),
                ('in_production', models.IntegerField(verbose_name='投产数量', blank=True, null=True)),
                ('proc_calc_length', models.FloatField(verbose_name='经长', blank=True, null=True)),
                ('yarn_csm_per_meter', models.FloatField(verbose_name='每米接单用纱量(kg)', blank=True, null=True)),
                ('greige_yarn_price', models.FloatField(verbose_name='接单原纱单价', blank=True, null=True)),
                ('painting_price', models.FloatField(verbose_name='接单染色单价', blank=True, null=True)),
                ('winding_price', models.FloatField(verbose_name='接单出轴单价', blank=True, null=True)),
                ('weaving_price', models.FloatField(verbose_name='接单织造单价', blank=True, null=True)),
                ('post_proc_price', models.FloatField(verbose_name='接单整理单价', blank=True, null=True)),
                ('delivering_price', models.FloatField(verbose_name='接单运费单价', blank=True, null=True)),
                ('last_updated', models.DateField(verbose_name='上次改动时间', auto_now=True)),
                ('firstly_created', models.BooleanField(default=True)),
                ('delivering_summury', models.OneToOneField(blank=True, to='mainapp.DeliveringSummury')),
            ],
            options={
                'verbose_name': '花色条目',
                'verbose_name_plural': '花色条目列表',
            },
        ),
        migrations.CreateModel(
            name='GreignYarnRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('length', models.FloatField(verbose_name='长度', default=0)),
                ('price', models.FloatField(verbose_name='单价', default=0)),
                ('sum_price', models.FloatField(verbose_name='金额', default=0)),
                ('created_at', models.DateField(verbose_name='创建时间', auto_now_add=True)),
            ],
            options={
                'verbose_name': '原纱记录',
                'verbose_name_plural': '花色原纱记录列表',
            },
        ),
        migrations.CreateModel(
            name='PaintingRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('length', models.FloatField(verbose_name='长度', default=0)),
                ('price', models.FloatField(verbose_name='单价', default=0)),
                ('sum_price', models.FloatField(verbose_name='金额', default=0)),
                ('created_at', models.DateField(verbose_name='创建时间', auto_now_add=True)),
            ],
            options={
                'verbose_name': '染色记录',
                'verbose_name_plural': '花色染色记录列表',
            },
        ),
        migrations.CreateModel(
            name='PostProcessingRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('length', models.FloatField(verbose_name='长度', default=0)),
                ('price', models.FloatField(verbose_name='单价', default=0)),
                ('sum_price', models.FloatField(verbose_name='金额', default=0)),
                ('created_at', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('method', models.CharField(verbose_name='整理方式', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrintingRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('length', models.FloatField(verbose_name='长度', default=0)),
                ('price', models.FloatField(verbose_name='单价', default=0)),
                ('sum_price', models.FloatField(verbose_name='金额', default=0)),
                ('created_at', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('machine_work_price', models.FloatField(verbose_name='上机费')),
                ('layout_price', models.FloatField(verbose_name='版费')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StoringRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('a_class_roll_count', models.IntegerField(verbose_name='A等品卷数')),
                ('a_class_length', models.FloatField(verbose_name='A等品长度')),
                ('b_class_roll_count', models.IntegerField(verbose_name='C等品卷数')),
                ('b_class_length', models.FloatField(verbose_name='C等品长度')),
                ('reason_degrade_2_B', models.TextField(verbose_name='降等至B级原因')),
                ('reason_degrade_2_C', models.TextField(verbose_name='降等至C级原因')),
                ('storing_date', models.DateField(verbose_name='入库时间')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoringSummury',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('a_class_roll_sum', models.IntegerField(verbose_name='A等品卷数', default=0)),
                ('a_class_length', models.FloatField(verbose_name='A等品长度', default=0)),
                ('b_class_roll_sum', models.IntegerField(verbose_name='C等品卷数', default=0)),
                ('b_class_length', models.FloatField(verbose_name='C等品长度', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SummuryBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('length', models.FloatField(verbose_name='总长', default=0)),
                ('sum_price', models.FloatField(verbose_name='总价', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='供应商', max_length=10)),
            ],
            options={
                'verbose_name': '供应商条目',
                'verbose_name_plural': '供应商列表',
            },
        ),
        migrations.CreateModel(
            name='WeavingRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('length', models.FloatField(verbose_name='长度', default=0)),
                ('price', models.FloatField(verbose_name='单价', default=0)),
                ('sum_price', models.FloatField(verbose_name='金额', default=0)),
                ('created_at', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('raw_price', models.FloatField(verbose_name='单价(元/纬)')),
                ('full_page_proof_price', models.FloatField(verbose_name='大样费', default=0)),
                ('supplier', models.ForeignKey(verbose_name='供应商', to='mainapp.Supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WindingRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('length', models.FloatField(verbose_name='长度', default=0)),
                ('price', models.FloatField(verbose_name='单价', default=0)),
                ('sum_price', models.FloatField(verbose_name='金额', default=0)),
                ('created_at', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('model', models.CharField(verbose_name='机型', max_length=40, null=True)),
                ('supplier', models.ForeignKey(verbose_name='供应商', to='mainapp.Supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BleachingSummury',
            fields=[
                ('summurybase_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='mainapp.SummuryBase')),
                ('design_drawing_sum', models.FloatField(verbose_name='打样费总额', default=0)),
            ],
            bases=('mainapp.summurybase',),
        ),
        migrations.CreateModel(
            name='GreignYarnSummury',
            fields=[
                ('summurybase_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='mainapp.SummuryBase')),
            ],
            options={
                'verbose_name': '原纱记录汇总',
                'verbose_name_plural': '原纱记录汇总项列表',
            },
            bases=('mainapp.summurybase',),
        ),
        migrations.CreateModel(
            name='PaintingSummury',
            fields=[
                ('summurybase_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='mainapp.SummuryBase')),
            ],
            options={
                'verbose_name': '染色记录汇总',
                'verbose_name_plural': '染色记录汇总项列表',
            },
            bases=('mainapp.summurybase',),
        ),
        migrations.CreateModel(
            name='PostProcessingSummury',
            fields=[
                ('summurybase_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='mainapp.SummuryBase')),
            ],
            bases=('mainapp.summurybase',),
        ),
        migrations.CreateModel(
            name='PrintingSummury',
            fields=[
                ('summurybase_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='mainapp.SummuryBase')),
                ('machine_work_sum', models.FloatField(verbose_name='上机费总额', default=0)),
                ('layout_sum', models.FloatField(verbose_name='版费总额', default=0)),
            ],
            bases=('mainapp.summurybase',),
        ),
        migrations.CreateModel(
            name='WeavingSummury',
            fields=[
                ('summurybase_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='mainapp.SummuryBase')),
                ('full_page_proof_sum', models.FloatField(verbose_name='大样费总额', default=0)),
            ],
            bases=('mainapp.summurybase',),
        ),
        migrations.CreateModel(
            name='WindingSummury',
            fields=[
                ('summurybase_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='mainapp.SummuryBase')),
            ],
            bases=('mainapp.summurybase',),
        ),
        migrations.AddField(
            model_name='storingrecord',
            name='summury',
            field=models.ForeignKey(related_name='records', to='mainapp.StoringSummury'),
        ),
        migrations.AddField(
            model_name='printingrecord',
            name='supplier',
            field=models.ForeignKey(verbose_name='供应商', to='mainapp.Supplier'),
        ),
        migrations.AddField(
            model_name='postprocessingrecord',
            name='supplier',
            field=models.ForeignKey(verbose_name='供应商', to='mainapp.Supplier'),
        ),
        migrations.AddField(
            model_name='paintingrecord',
            name='supplier',
            field=models.ForeignKey(verbose_name='供应商', to='mainapp.Supplier'),
        ),
        migrations.AddField(
            model_name='greignyarnrecord',
            name='supplier',
            field=models.ForeignKey(verbose_name='供应商', to='mainapp.Supplier'),
        ),
        migrations.AddField(
            model_name='entry',
            name='storing_summury',
            field=models.OneToOneField(blank=True, to='mainapp.StoringSummury'),
        ),
        migrations.AddField(
            model_name='deliveringrecord',
            name='summury',
            field=models.ForeignKey(related_name='records', to='mainapp.DeliveringSummury'),
        ),
        migrations.AddField(
            model_name='bleachingrecord',
            name='supplier',
            field=models.ForeignKey(verbose_name='供应商', to='mainapp.Supplier'),
        ),
        migrations.AddField(
            model_name='windingrecord',
            name='summury',
            field=models.ForeignKey(related_name='records', to='mainapp.WindingSummury'),
        ),
        migrations.AddField(
            model_name='weavingrecord',
            name='summury',
            field=models.ForeignKey(related_name='records', to='mainapp.WeavingSummury'),
        ),
        migrations.AddField(
            model_name='printingrecord',
            name='summury',
            field=models.ForeignKey(related_name='records', to='mainapp.PrintingSummury'),
        ),
        migrations.AddField(
            model_name='postprocessingrecord',
            name='summury',
            field=models.ForeignKey(related_name='records', to='mainapp.PostProcessingSummury'),
        ),
        migrations.AddField(
            model_name='paintingrecord',
            name='summury',
            field=models.ForeignKey(related_name='records', to='mainapp.PaintingSummury'),
        ),
        migrations.AddField(
            model_name='greignyarnrecord',
            name='summury',
            field=models.ForeignKey(related_name='records', to='mainapp.GreignYarnSummury'),
        ),
        migrations.AddField(
            model_name='entry',
            name='bleaching_summury',
            field=models.OneToOneField(blank=True, to='mainapp.BleachingSummury'),
        ),
        migrations.AddField(
            model_name='entry',
            name='greign_yarn_summury',
            field=models.OneToOneField(blank=True, to='mainapp.GreignYarnSummury'),
        ),
        migrations.AddField(
            model_name='entry',
            name='painting_summury',
            field=models.OneToOneField(blank=True, to='mainapp.PaintingSummury'),
        ),
        migrations.AddField(
            model_name='entry',
            name='post_processing_summury',
            field=models.OneToOneField(blank=True, to='mainapp.PostProcessingSummury'),
        ),
        migrations.AddField(
            model_name='entry',
            name='printing_summury',
            field=models.OneToOneField(blank=True, to='mainapp.PrintingSummury'),
        ),
        migrations.AddField(
            model_name='entry',
            name='weaving_summury',
            field=models.OneToOneField(blank=True, to='mainapp.WeavingSummury'),
        ),
        migrations.AddField(
            model_name='entry',
            name='winding_summury',
            field=models.OneToOneField(blank=True, to='mainapp.WindingSummury'),
        ),
        migrations.AddField(
            model_name='bleachingrecord',
            name='summury',
            field=models.ForeignKey(related_name='records', to='mainapp.BleachingSummury'),
        ),
    ]
