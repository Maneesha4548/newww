# Generated by Django 3.0 on 2021-05-23 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FarMeKart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myorders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=300)),
                ('item_type', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('is_status', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True, null='True')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]