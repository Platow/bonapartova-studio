# Generated by Django 3.1.7 on 2021-03-27 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='appointments.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='reserved_at',
            field=models.DateTimeField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='appointments.service', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Мастер'),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=64, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=64, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=16, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='service',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активность'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость'),
        ),
    ]
