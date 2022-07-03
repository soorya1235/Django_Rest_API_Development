from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

class PostList(APIView):
    def get(self,request):
        model = Post.objects.all()
        serializer = PostSerializer(model,many=True)
        return Response(serializer.data)

    # def post(self,request):
    #    # model = Post.objects.all()
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PostList1(APIView):

    def post(self,request):
       # model = Post.objects.all()
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PostDetails(APIView):

    def get_user(self,post_id):
        try:
            model = Post.objects.get(id=post_id)
            return model
        except:
            return

    def get(self,request,post_id):
        if not self.get_user(post_id):
            return Response(f"User with post id - {post_id} not found",status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(self.get_user(post_id))
        return Response(serializer.data)

    def put(self,request,post_id):
        serializer = PostSerializer(self.get_user(post_id),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,post_id):
        if not self.get_user(post_id):
            return Response(f"User with post id does not exists",status.HTTP_400_BAD_REQUEST)
        model = self.get_user(post_id)
        model.delete()
        return Response(f"User with post_id - {post_id} deleted",status.HTTP_204_NO_CONTENT)