# Generated by Django 2.1.7 on 2022-12-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0008_auto_20221107_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='premium',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='company_description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='job',
            name='website',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]