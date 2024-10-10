from django.urls import include, path
from . import views
from rest_framework.routers import SimpleRouter


# Definindo o router para possíveis futuras rotas baseadas em ViewSets
router = SimpleRouter()

urlpatterns = [
    # Definindo as rotas para Categoria
    path("categorias/", views.CategoriaList.as_view(), name=views.CategoriaList.name),
    path(
        "categorias/<int:pk>/", views.CategoriaDetail.as_view(), name=views.CategoriaDetail.name
    ),

    # Definindo as rotas para Autor
    path("autores/", views.AutorList.as_view(), name=views.AutorList.name),
    path("autores/<int:pk>/", views.AutorDetail.as_view(), name=views.AutorDetail.name),

    # Definindo as rotas para Livro
    path("livros/", views.LivrosList.as_view(), name=views.LivrosList.name),
    path("livros/<int:pk>/", views.LivrosDetail.as_view(), name=views.LivrosDetail.name),

    # Incluindo as rotas do router, se houver
    path("", include(router.urls)),

    # Definindo a rota principal da API
    path("", views.ApiRoot.as_view(), name=views.ApiRoot.name),
]

