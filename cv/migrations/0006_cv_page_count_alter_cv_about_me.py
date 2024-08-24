# Generated by Django 5.1 on 2024-08-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_alter_education_cv_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='page_count',
            field=models.PositiveSmallIntegerField(default=1, help_text='If the content of your CV does not fit on one page, the content will be automatically split into multiple pages. Set the expected number of pages here to apply the first page styling across all pages.', verbose_name='page count'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='about_me',
            field=models.TextField(blank=True, verbose_name='about me'),
        ),
    ]