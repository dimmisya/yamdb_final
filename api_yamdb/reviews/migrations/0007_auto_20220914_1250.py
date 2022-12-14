# Generated by Django 2.2.16 on 2022-09-14 09:50

import django.db.models.deletion
import reviews.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20220912_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmation_code',
            field=models.TextField(blank=True, verbose_name='Код подтверждения'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.SmallIntegerField(validators=[reviews.validators.validate_year], verbose_name='Year'),
        ),
    ]
