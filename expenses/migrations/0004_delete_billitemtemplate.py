# Generated by Django 2.1.1 on 2018-10-02 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_shorten_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billitemtemplate',
            name='user',
        ),
        migrations.DeleteModel(
            name='BillItemTemplate',
        ),
    ]
