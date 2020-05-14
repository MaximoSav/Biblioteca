# Generated by Django 2.2 on 2020-05-14 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibl', '0003_ejemplar_usuarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejemplar',
            name='codLibro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bibl.Libro'),
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='localizacion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='direccion',
            field=models.CharField(max_length=50, null=True),
        ),
    ]