# Generated by Django 4.2.6 on 2023-10-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_mycontact_serial_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='myImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_created=True)),
                ('image', models.ImageField(upload_to='product_myImages/')),
            ],
        ),
    ]
