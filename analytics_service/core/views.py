from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def track_event(request):
    return Response({'message': 'Analytics event tracked!'})

