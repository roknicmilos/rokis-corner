# Generated by Django 5.1 on 2024-08-22 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='cv.cv', verbose_name='CV'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('role', models.CharField(max_length=100, verbose_name='role')),
                ('start', models.DateField(help_text="Day is not important. Select 1st if you don't know the exact start day.", verbose_name='start')),
                ('end', models.DateField(blank=True, help_text="Leave empty if you are currently working on this project. Day is not important. Select 1st if you don't know the exact end day.", null=True, verbose_name='end')),
                ('technologies', models.CharField(max_length=255, verbose_name='technologies')),
                ('description', models.TextField(default='', verbose_name='description')),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='cv.cv', verbose_name='CV')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]