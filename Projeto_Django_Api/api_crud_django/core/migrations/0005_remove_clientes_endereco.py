# Generated by Django 4.1.10 on 2023-08-23 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_cliente_clientes_rename_login_logins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='endereco',
        ),
    ]