# Generated by Django 2.2 on 2020-05-14 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
