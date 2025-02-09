from django.core.management.base import BaseCommand
from core.models import Categoria, Autor, Livros


class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        categoria_misterio = Categoria.objects.create(name="Mistério")
        categoria_ficcao = Categoria.objects.create(name="Ficção")
        categoria_fantasia = Categoria.objects.create(name="Fantasia")
        categoria_romance = Categoria.objects.create(name="Romance")

        autor_agatha_christie = Autor.objects.create(name="Agatha Christie")
        autor_arthur_c_clarke = Autor.objects.create(name="Arthur C. Clarke")
        autor_arthur_conan_doyle = Autor.objects.create(name="Arthur Conan Doyle")
        autor_cs_lewis = Autor.objects.create(name="C.S. Lewis")
        autor_emily_bronte = Autor.objects.create(name="Emily Brontë")
        autor_george_rr_martin = Autor.objects.create(name="George R.R. Martin")
        autor_isaac_asimov = Autor.objects.create(name="Isaac Asimov")
        autor_jrr_tolkien = Autor.objects.create(name="J.R.R. Tolkien")

        Livros.objects.create(
            titulo="Assassinato no Expresso do Oriente",
            autor=autor_agatha_christie,
            categoria=categoria_misterio,
            publicado_em="1934-01-01",
        )
        Livros.objects.create(
            titulo="Morte no Nilo",
            autor=autor_agatha_christie,
            categoria=categoria_misterio,
            publicado_em="1937-11-01",
        )
        Livros.objects.create(
            titulo="2001: Uma Odisseia no Espaço",
            autor=autor_arthur_c_clarke,
            categoria=categoria_ficcao,
            publicado_em="1968-06-16",
        )
        Livros.objects.create(
            titulo="Encontro com Rama",
            autor=autor_arthur_c_clarke,
            categoria=categoria_ficcao,
            publicado_em="1973-06-01",
        )
        Livros.objects.create(
            titulo="O Cão dos Baskervilles",
            autor=autor_arthur_conan_doyle,
            categoria=categoria_misterio,
            publicado_em="1902-04-01",
        )
        Livros.objects.create(
            titulo="Um Estudo em Vermelho",
            autor=autor_arthur_conan_doyle,
            categoria=categoria_misterio,
            publicado_em="1887-11-01",
        )
        Livros.objects.create(
            titulo="As Crônicas de Nárnia",
            autor=autor_cs_lewis,
            categoria=categoria_fantasia,
            publicado_em="1950-10-16",
        )
        Livros.objects.create(
            titulo="O Leão, a Feiticeira e o Guarda-Roupa",
            autor=autor_cs_lewis,
            categoria=categoria_fantasia,
            publicado_em="1950-10-16",
        )
        Livros.objects.create(
            titulo="O Morro dos Ventos Uivantes",
            autor=autor_emily_bronte,
            categoria=categoria_romance,
            publicado_em="1847-12-01",
        )
        Livros.objects.create(
            titulo="A Guerra dos Tronos",
            autor=autor_george_rr_martin,
            categoria=categoria_fantasia,
            publicado_em="1996-08-06",
        )
        Livros.objects.create(
            titulo="A Fúria dos Reis",
            autor=autor_george_rr_martin,
            categoria=categoria_fantasia,
            publicado_em="1998-11-16",
        )
        Livros.objects.create(
            titulo="Fundação",
            autor=autor_isaac_asimov,
            categoria=categoria_ficcao,
            publicado_em="1951-06-01",
        )
        Livros.objects.create(
            titulo="Eu, Robô",
            autor=autor_isaac_asimov,
            categoria=categoria_ficcao,
            publicado_em="1950-12-02",
        )
        Livros.objects.create(
            titulo="O Senhor dos Anéis",
            autor=autor_jrr_tolkien,
            categoria=categoria_fantasia,
            publicado_em="1954-07-29",
        )
        Livros.objects.create(
            titulo="O Hobbit",
            autor=autor_jrr_tolkien,
            categoria=categoria_fantasia,
            publicado_em="1937-09-21",
        )