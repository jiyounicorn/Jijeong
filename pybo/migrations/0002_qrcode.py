# Generated by Django 3.2.4 on 2022-11-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qrname', models.CharField(blank=True, max_length=6)),
                ('code', models.ImageField(blank=True, null=True, upload_to='qr')),
            ],
            options={
                'verbose_name_plural': 'QR CODES',
            },
        ),
    ]
