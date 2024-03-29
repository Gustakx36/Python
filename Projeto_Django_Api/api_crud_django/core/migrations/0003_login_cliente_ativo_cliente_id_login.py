# Generated by Django 4.1.10 on 2023-08-23 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cliente_endereco_alter_cliente_idade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.TextField(max_length=255)),
                ('senha', models.TextField(max_length=255)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_login',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logins', to='core.login'),
        ),
    ]
