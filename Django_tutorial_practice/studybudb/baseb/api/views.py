from rest_framework.decorators import api_view
from rest_framework.response import Response
from baseb.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])  # We can ad 'PUT', 'POST'   but, now, we only wants to allow get data ...  and this  api_view gives us an visual for better experience ...
def getRoutes(request):
    routes = [
        # For Home page
        'GET /api'
        # Here, We creates an api for rooms  by which some one can display rooms in their sites ...
        'GET /api/rooms'
        # Info about single specific room ...
        'GET /api/rooms/:id'
    ]
    return Response(routes)

# For All Rooms
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    # Now, Serialze the rooms data for conveeting into Json data
    serializer = RoomSerializer(rooms, many=True)  # Here, many=True , means There will be multiple objects ... Like we have Room.objects.all()   so, many should True..
    return Response(serializer.data)

# For specific Room ...
@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    # Now, Serialze the rooms data for conveeting into Json data
    serializer = RoomSerializer(room, many=False)  # Here, many=False , Because there will be only single object of 1 room
    return Response(serializer.data)