# Generated by Django 3.0.3 on 2020-02-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='img/ahiface.png', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(),
        ),
    ]
