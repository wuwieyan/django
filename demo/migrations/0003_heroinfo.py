# Generated by Django 2.2.3 on 2019-08-03 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20190803_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=False)),
                ('hskills', models.CharField(max_length=20)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.BookInfo')),
            ],
        ),
    ]