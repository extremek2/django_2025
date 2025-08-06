from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post
from example.serializers import PostSerializer


@api_view(['GET'])
def helloAPI(request):
    return Response('hello world')

@api_view(['GET'])
def hiAPI(request):
    return Response('hi world')

# map 테스트용
def examplemap(request):
    return render(request, 'example/example_map.html')

def example(request):
    return render(request, template_name='example/example.html')

@api_view(['GET','DELETE','PUT'])
def postAPI(request,pk):
    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        postSerializer = PostSerializer(post)
        return Response(postSerializer.data)
    elif request.method == 'DELETE':
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(data="Completed", status=status.HTTP_204_NO_CONTENT)
    else:
        # request.method == 'PUT'
        # post = Post.objects.get(pk=pk)
        post = get_object_or_404(pk=pk, klass=Post)
        postSerializer = PostSerializer(post, data=request.data)
        if postSerializer.is_valid():
            postSerializer.save()
            return Response(postSerializer.data, status=status.HTTP_200_OK)
    return Response(postSerializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST'])
def blogAPI(request):
    if request.method == 'GET':
        # post 글 전체 리스트
        posts = Post.objects.all()
        postSerializer = PostSerializer(posts, many=True)
        return Response(postSerializer.data, status=status.HTTP_200_OK)
    else:
        # 새로운 글 create (화면에서 작성 -> json -> django 서버의 db에 orm 객체로 전달)
        postSerializer=PostSerializer(data=request.data)  # data= 을 정의하여 json 자료인 것을 명시
        if postSerializer.is_valid():
            postSerializer.save()
            return Response(postSerializer.data, status=status.HTTP_201_CREATED)

    return Response(postSerializer.errors, status=status.HTTP_400_BAD_REQUEST)



