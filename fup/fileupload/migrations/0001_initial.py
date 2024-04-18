# Generated by Django 5.0.4 on 2024-04-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('postfix', models.CharField(blank=True, max_length=20, null=True)),
                ('register_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('postfix', models.CharField(blank=True, max_length=20, null=True)),
                ('register_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(default='path/images/nophoto.png', upload_to='path/images')),
            ],
        ),
    ]