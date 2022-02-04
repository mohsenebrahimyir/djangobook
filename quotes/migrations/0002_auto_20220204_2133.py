# Generated by Django 3.2 on 2022-02-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='describetion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='quotedata',
            new_name='quotedate',
        ),
        migrations.AlterField(
            model_name='quote',
            name='jobfile',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
