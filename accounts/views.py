from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MobileUsersSerializer
from .models import Token


class MyView(APIView):
    def get(self, request):
        bearer_token = request.META.get('HTTP_AUTHORIZATION', None)
        print(bearer_token)
        key = bearer_token.split()[1]
        token = Token.objects.get(key=key)
        users = token.user.related.all()
        serializer = MobileUsersSerializer(users, many=True)
        return Response(serializer.data)
