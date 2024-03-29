# Generated by Django 4.2.6 on 2023-10-22 06:05

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_myimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_description', tinymce.models.HTMLField()),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('indiamart_link', models.URLField(blank=True, null=True)),
                ('other_social_links', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
