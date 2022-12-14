# Generated by Django 4.1.3 on 2022-11-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=30)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descricao', models.TextField()),
                ('capa', models.CharField(max_length=200)),
                ('insert', models.DateTimeField()),
                ('update', models.DateTimeField()),
            ],
        ),
    ]
