from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]
    

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        jobs = Job.objects.all()
        print(jobs)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def perform_create(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'title': request.data.get('title'), 
            'company': request.data.get('company'),
            'job_type': request.data.get('job_type'),
            'experience_level': request.data.get('experience_level'), 
            'description': request.data.get('description'), 
            'location': request.data.get('location'), 
            'salary_min': request.data.get('salary_min'), 
            'salary_max': request.data.get('salary_max'), 
            'posted_date': request.data.get('posted_date'), 
            'application_deadline': request.data.get('application_deadline'), 
            'company_website': request.data.get('company_website'), 
            'contact_email': request.data.get('contact_email'),
            'is_active': request.data.get('is_active'), 
        }
        serializer = JobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)