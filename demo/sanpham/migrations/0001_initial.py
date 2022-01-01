# Generated by Django 3.2.10 on 2021-12-29 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sanpham',
            fields=[
                ('sanpham_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('danhmucsanpham_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.danhmucsanpham')),
            ],
        ),
    ]
