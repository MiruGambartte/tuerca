# Generated by Django 4.2.1 on 2023-06-13 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_detarticulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='n',
        ),
    ]