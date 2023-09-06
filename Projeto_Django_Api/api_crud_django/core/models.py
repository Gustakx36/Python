from django.db import models

# class Logins(models.Model):
#     id = models.AutoField(primary_key=True)
#     login = models.TextField(max_length=255)
#     senha = models.TextField(max_length=255)

# class Cliente(models.Model):
#     id = models.AutoField(primary_key=True)
#     nome = models.TextField(max_length=255)
#     idade = models.IntegerField()
#     id_login = models.ForeignKey(Logins, related_name='logins', on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return 'nome : ' + self.nome + ' -> idade : ' + str(self.idade)

