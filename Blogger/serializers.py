from rest_framework import serializers
from .models import  Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
       # fields = ('post_id','post_name')
        fields = '__all__'
