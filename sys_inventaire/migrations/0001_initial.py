# Generated by Django 3.0.8 on 2020-07-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dietetique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_article', models.CharField(max_length=100)),
                ('quantite', models.IntegerField()),
                ('prix', models.FloatField()),
                ('date_peremption', models.DateTimeField()),
                ('Numero_lot', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupe', models.CharField(blank=True, choices=[('liste 1', 'Produit toxique'), ('Liste 2', 'Produit dangereux'), ('Stupéfiant', 'Stupéfiants')], max_length=20)),
                ('dci', models.CharField(blank=True, max_length=100)),
                ('specialite', models.CharField(max_length=100)),
                ('quantite', models.IntegerField()),
                ('classe_therapeutic', models.TextField(blank=True)),
                ('prix', models.FloatField()),
                ('presentation', models.CharField(blank=True, choices=[('SUPPO & OVULE', 'Suppositoire et ovule'), ('GOUTTE NASALE', 'Goutte nasale'), ('GOUTTE NASALE', 'Goutte nasale'), ('AMPOULE BUVABLE', 'Ampoule buvable'), ('SACHET', 'Sachets'), ('SOLUTE', 'Solute'), ('COMPRIMÉ', 'Comprimé'), ('SIROP', 'Sirop'), ('POUDRE', 'Poudre')], max_length=20)),
                ('date_peremption', models.DateTimeField()),
                ('Numero_lot', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parapharmatie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_article', models.CharField(max_length=100)),
                ('quantite', models.IntegerField()),
                ('prix', models.FloatField()),
                ('date_peremption', models.DateTimeField()),
                ('Numero_lot', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Petit_matériel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_article', models.CharField(max_length=100)),
                ('quantite', models.IntegerField()),
                ('prix', models.FloatField()),
                ('date_peremption', models.DateTimeField()),
                ('Numero_lot', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
