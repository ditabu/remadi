# Generated by Django 3.2.8 on 2021-10-27 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_auto_20211025_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='date',
            name='category',
        ),
        migrations.RemoveField(
            model_name='date',
            name='dates',
        ),
        migrations.RemoveField(
            model_name='date',
            name='description',
        ),
        migrations.RemoveField(
            model_name='date',
            name='location',
        ),
        migrations.RemoveField(
            model_name='date',
            name='name',
        ),
        migrations.RemoveField(
            model_name='date',
            name='price',
        ),
        migrations.RemoveField(
            model_name='date',
            name='time',
        ),
        migrations.RemoveField(
            model_name='date',
            name='user',
        ),
        migrations.AddField(
            model_name='date',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AddField(
            model_name='mydates',
            name='date_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.date'),
        ),
        migrations.AddField(
            model_name='mydates',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
