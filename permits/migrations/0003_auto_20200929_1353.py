# Generated by Django 2.2.13 on 2020-09-29 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0002_historicalpermitrequest_historicalpermitrequestgeotime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permitrequest',
            options={'permissions': [('amend_permit_request', 'Traiter les demandes de permis'), ('validate_permit_request', 'Valider les demandes de permis'), ('classify_permit_request', 'Classer les demandes de permis'), ('modify_permit_request', 'Modifier les demandes de permis')], 'verbose_name': '3.1 Consultation de la demande', 'verbose_name_plural': '3.1 Consultation des demandes'},
        ),
        migrations.AlterField(
            model_name='permitrequest',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Brouillon'), (1, 'Envoyée, en attente de traitement'), (4, 'Demande de compléments'), (3, 'En traitement'), (5, 'En validation'), (2, 'Approuvée'), (6, 'Refusée'), (7, 'Annonce réceptionnée'), (8, 'Annonce modifiée')], default=0, verbose_name='état'),
        ),
        migrations.AlterField(
            model_name='permitworkflowstatus',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Brouillon'), (1, 'Envoyée, en attente de traitement'), (4, 'Demande de compléments'), (3, 'En traitement'), (5, 'En validation'), (2, 'Approuvée'), (6, 'Refusée'), (7, 'Annonce réceptionnée'), (8, 'Annonce modifiée')], verbose_name='statut'),
        ),
    ]
