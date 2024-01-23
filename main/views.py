from .serializers import ItemSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item


class ItemsPage(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class OrderAdd(APIView):
    def post(self, req):
        order = OrderSerializer(data=req.data)

        if order.is_valid():
            order.save()
            return Response({'result': 'Пару секунд...'})

        return Response({'result': 'Ошибка в форме'})

