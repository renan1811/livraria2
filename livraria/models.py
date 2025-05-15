from django.db import models

# começandoooo


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.descricao

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Livro(models.Model):
    nome = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)


    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="editoras"
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )

    

    def __str__ (self):
        return f"{self.titulo} ({self.quantidade})"
    


