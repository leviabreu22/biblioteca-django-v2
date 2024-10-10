from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ("name",)
        
    def _str_(self):
        return self.name

class Autor(models.Model):
    MALE = "M"
    FEMALE = "F"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )
    name = models.CharField(max_length=100, blank=False, default="")
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

class Livros(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, related_name="livros", on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name="livros", on_delete=models.CASCADE)
    publicado_em = models.DateTimeField()

    class Meta:
        ordering = ("titulo",)

    def __str__(self):
        return self.titulo