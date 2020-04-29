# Generated by Django 2.1.15 on 2020-04-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merge_date', models.DateField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FulfilmentDD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_file_id', models.CharField(max_length=50, null=True)),
                ('import_date', models.DateField(null=True)),
                ('charity_urn', models.IntegerField(null=True)),
                ('donor_charity_urn', models.CharField(max_length=15, null=True)),
                ('call_date', models.DateField(null=True)),
                ('title', models.CharField(max_length=10, null=True)),
                ('surname', models.CharField(max_length=20, null=True)),
                ('forename', models.CharField(max_length=20, null=True)),
                ('initials', models.CharField(max_length=5, null=True)),
                ('address1', models.CharField(max_length=50, null=True)),
                ('address2', models.CharField(max_length=50, null=True)),
                ('address3', models.CharField(max_length=50, null=True)),
                ('town', models.CharField(max_length=50, null=True)),
                ('county', models.CharField(max_length=50, null=True)),
                ('postcode', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('email_address', models.EmailField(max_length=254, null=True)),
                ('gift_aid', models.CharField(max_length=2, null=True)),
                ('source_code', models.CharField(max_length=10, null=True)),
                ('fund_code', models.CharField(max_length=10, null=True)),
                ('fund_title', models.CharField(max_length=10, null=True)),
                ('email_comms_pref', models.CharField(max_length=2, null=True)),
                ('mail_comms_pref', models.CharField(max_length=2, null=True)),
                ('telephone_comms_pref', models.CharField(max_length=2, null=True)),
                ('sms_comms_pref', models.CharField(max_length=2, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('frequency', models.CharField(max_length=10, null=True)),
                ('collection_date', models.DateField(null=True)),
                ('card_holders_name', models.CharField(max_length=50, null=True)),
                ('bank_name', models.CharField(max_length=50, null=True)),
                ('bank_account_number', models.IntegerField(null=True)),
                ('bank_sort_code', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=50)),
                ('file_path', models.FileField(upload_to='fourpaws/letters')),
            ],
        ),
    ]