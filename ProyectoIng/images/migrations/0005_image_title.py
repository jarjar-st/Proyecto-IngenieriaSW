# Generated by Django 3.0.3 on 2020-03-15 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20200311_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.TextField(default='url_imagen', max_length=10),
        ),
    ]