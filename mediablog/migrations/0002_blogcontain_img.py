# Generated by Django 4.2.1 on 2023-07-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediablog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcontain',
            name='img',
            field=models.ImageField(default='default_product.png', upload_to='images/'),
        ),
    ]