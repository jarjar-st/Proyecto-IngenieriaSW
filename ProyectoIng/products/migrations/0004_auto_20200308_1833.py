# Generated by Django 2.0.2 on 2020-03-09 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200308_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desription',
            new_name='description',
        ),
    ]
