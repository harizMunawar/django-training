# Generated by Django 2.2.5 on 2020-02-20 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200220_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='img/ahiface.png', upload_to='uploads/%Y/%M/%D'),
        ),
    ]