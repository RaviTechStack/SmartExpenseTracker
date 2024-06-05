# Generated by Django 4.1.5 on 2023-04-12 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_futureexpense_exp_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionHist',
            fields=[
                ('trans_id', models.AutoField(primary_key=True, serialize=False)),
                ('trans_amt', models.IntegerField()),
                ('trans_desc', models.CharField(max_length=500)),
                ('trans_type', models.CharField(max_length=15)),
                ('is_withdrwal', models.BooleanField()),
                ('trans_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
