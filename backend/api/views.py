from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello(request):
    return Response({"message": "Bonjour depuis Django API!"})


class TransactionCreateView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            client = serializer.validated_data['client']
            montant = serializer.validated_data['montant']

            if client.solde < montant:
                return Response({'error': 'Solde insuffisant'}, status=400)

            client.solde -= montant
            client.save()
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# après serializer.save()
channel_layer = get_channel_layer()
async_to_sync(channel_layer.group_send)(
    "notifications",
    {
        "type": "send_notification",
        "content": {"message": "Nouvelle consommation", "client": client.id, "montant": str(montant)},
    }
)