from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from API_App.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from API_App.models import Post
from rest_framework.permissions import IsAuthenticated
from API_App.permissions import isPostPossesor
from rest_framework import filters


# Create your views here.
class APIAppView(APIView):

    def get(self,request):
        return Response({'message':'Whatsupp bro'})


class PostView(ModelViewSet):
    permission_classes=[IsAuthenticated, isPostPossesor]
    serializer_class=PostSerializer    
    filter_backends=[filters.SearchFilter]
    search_fields=['title','content']

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)