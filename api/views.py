from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from rest_framework.permissions import AllowAny, IsAuthenticated
from pokedex.models import Pokemon
from .serializers import PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    authentication_classes = [OAuth2Authentication]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            # Para escritura, exige token con scope 'write'
            return [TokenHasReadWriteScope()]
        # Para GET, HEAD, OPTIONS, solo autenticación (o si quieres público, cambia a [AllowAny()])
        return [IsAuthenticated()]