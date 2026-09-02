from django.db import models

class Album(models.Model):
    titulo = models.CharField(max_length=200)
    ano_lancamento = models.IntegerField()

    def __str__(self):
        return self.titulo


class Musica(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=150)
    duracao_segundos = models.IntegerField()
    favorita = models.BooleanField(default=False) 
    album = models.ForeignKey(
        Album,
        related_name = 'musicas',
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )

    def __str__(self):
        return self.titulo