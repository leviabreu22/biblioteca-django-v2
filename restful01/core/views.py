from rest_framework import generics
from core.models import Livros
from core.models import Categoria
from core.models import Autor
from core.serializers import LivrosSerializer
from core.serializers import CategoriaSerializer
from core.serializers import AutorSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from core.filters import LivrosFilter
from core.filters import CategoriaFilter



class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializes_class = CategoriaSerializer
    name = "categoria-list"
    filterset_class = CategoriaFilter
    search_fields = ("^name",)
    ordering_fields = ['nome']

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-list"
    filterset_fields = (
        "gender",
        "races_count",
    )
    search_fields = ("^name",)
    ordering_fields = ("name", "races_count")
    
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"

class LivrosList(generics.ListCreateAPIView):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
    name = "livros-list"
    filterset_class = LivrosFilter
    search_fields = ("^titulo",)
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']

    
    
class LivrosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
    name = "livros-detail"    


# Ajustando Roteamento
class ApiRoot(generics.GenericAPIView):
    name = "api-root"
    
    def get(self, request, *arg, **kwargs):
        return Response(
            {
                "categoria":reverse("categoria-list", request=request),
                "autor":reverse(AutorList.name,request=request),
                "livros":reverse(LivrosList.name, request=request),
            }
        )
        


