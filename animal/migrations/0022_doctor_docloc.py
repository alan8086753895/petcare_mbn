# Generated by Django 4.0.5 on 2022-06-30 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0021_alter_animal_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='docloc',
            field=models.TextField(default='https://www.google.com/search?q=kodikkunnu+map%5Bs&oq=kodikkunnu+map%5Bs&aqs=chrome..69i57.17319j0j7&sourceid=chrome&ie=UTF-8#', max_length=1000),
            preserve_default=False,
        ),
    ]
