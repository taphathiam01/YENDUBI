from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsClientUser
from .serializers import ClientProfileSerializer

class MeAPIView(APIView):
    permission_classes = [IsAuthenticated, IsClientUser]

    def get(self, request):
        serializer = ClientProfileSerializer(request.user)
        return Response(serializer.data)
