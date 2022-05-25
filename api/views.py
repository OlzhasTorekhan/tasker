from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProjectSerializer
# Create your views here.
class ProjectView(APIView):
    def get(self,request):
        user = request.user
        projects = user.select_related('ProjectModel')
        response = ProjectSerializer(projects,many=True)
        return Response({'projects':response})