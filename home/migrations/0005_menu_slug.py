# Generated by Django 3.0.3 on 2020-02-20 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200220_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]