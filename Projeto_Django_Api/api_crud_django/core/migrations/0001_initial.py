# Generated by Django 4.1.10 on 2023-08-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('idade', models.TextField(max_length=255)),
                ('endereco', models.IntegerField()),
            ],
        ),
    ]