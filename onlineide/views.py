
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import User, Submissions
from .serializers import UserSerializer, SubmissionSerializer
from .utils import create_code_file, execute_file 

def hello_world(request):
    return HttpResponse("Welcome to online ide")

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class SubmissionsViewSet(ModelViewSet):
    serializer_class = SubmissionSerializer
    queryset = Submissions.objects.all()
    
    def create(self, request, *args, **kwargs):
        request.data["status"]="P"
        file_name=create_code_file(request.data.get("language"),
                                   request.data.get("code"))
        output = execute_file(file_name, request.data.get("language"))
        request.data["output"] = str(output)                        
        return super().create(request,args,kwargs)
    
     
# Create your views here.
