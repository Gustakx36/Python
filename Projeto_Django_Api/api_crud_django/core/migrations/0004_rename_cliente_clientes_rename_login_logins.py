# Generated by Django 4.1.10 on 2023-08-23 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_login_cliente_ativo_cliente_id_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliente',
            new_name='Clientes',
        ),
        migrations.RenameModel(
            old_name='Login',
            new_name='Logins',
        ),
    ]