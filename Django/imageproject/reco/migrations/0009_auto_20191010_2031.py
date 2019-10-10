# Generated by Django 2.2.5 on 2019-10-10 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0008_auto_20191010_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='text',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='reco.Feed'),
        ),
    ]
