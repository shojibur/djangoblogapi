from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Post
from  .serializers import PostSerializer
# Create your views here.
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
    # Comma is important at the end, 
    # This is app level permission, commenting since we set project level permission
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer