# Generated by Django 2.1.5 on 2019-02-01 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("edc_lab", "0017_auto_20181108_0353")]

    operations = [
        migrations.AlterField(
            model_name="historicalaliquot",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbox",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AlterField(
            model_name="historicalmanifest",
            name="consignee",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_lab.Consignee",
                verbose_name="Consignee",
            ),
        ),
        migrations.AlterField(
            model_name="historicalmanifest",
            name="shipper",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_lab.Shipper",
                verbose_name="Shipper/Exporter",
            ),
        ),
        migrations.AlterField(
            model_name="historicalmanifest",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AlterField(
            model_name="historicalorder",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AlterField(
            model_name="historicalresult",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AlterField(
            model_name="historicalresultitem",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        ),
    ]
