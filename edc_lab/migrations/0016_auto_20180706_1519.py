# Generated by Django 2.0.7 on 2018-07-06 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edc_lab', '0015_manifestitem_site'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalaliquot',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical aliquot'},
        ),
        migrations.AlterModelOptions(
            name='historicalbox',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical box'},
        ),
        migrations.AlterModelOptions(
            name='historicalboxitem',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical box item'},
        ),
        migrations.AlterModelOptions(
            name='historicalconsignee',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical consignee'},
        ),
        migrations.AlterModelOptions(
            name='historicalmanifest',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical manifest'},
        ),
        migrations.AlterModelOptions(
            name='historicalorder',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical order'},
        ),
        migrations.AlterModelOptions(
            name='historicalresult',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical result'},
        ),
        migrations.AlterModelOptions(
            name='historicalresultitem',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical result item'},
        ),
        migrations.AlterModelOptions(
            name='historicalshipper',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical shipper'},
        ),
    ]
