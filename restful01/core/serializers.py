from rest_framework import serializers
from core.models import Categoria, Livros, Autor


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    livros = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="livros-detail")
    
    class Meta:
        model: Categoria
        fields = ("url", "id", "name", "livros")
        
class AutorSerializer(serializers.HyperlinkedModelSerializer):
    livros = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="livros-detail")
    gender = serializers.ChoiceField(choices=Autor.GENDER_CHOICES)
    gender_descricao = serializers.CharField(
        source="get_gender_display", read_only=True
    )
    
    class Meta:
        model = Autor
        fields = (
            "url",
            "id",
            "name",
            "gender",
            "gender_descricao",
            "livros",
        )

class LivrosSerializer(serializers.HyperlinkedModelSerializer):
    autor = serializers.SlugRelatedField(
        queryset=Autor.objects.all(), slug_field="name"
    )
    categoria = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(), slug_field="name"
    )
    
    class Meta:
        model = Livros
        fields = (
            "url",
            "id",
            "titulo",
            "autor",
            "categoria",
            "publicado_em",
        )
        