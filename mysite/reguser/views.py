from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from .task import send_welcome_email


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    
    def create(self, request):
        if request.method == 'POST':
            email = request.data.get('email')
            
            print(email)
            send_welcome_email.delay(email)
            
            serialized_data = UserSerializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(serialized_data.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)