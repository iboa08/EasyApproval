# Generated by Django 2.1.3 on 2019-12-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0007_merge_20191211_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='caracter',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='curso',
            name='infraestructura',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='media/constancias/'),
        ),
    ]
