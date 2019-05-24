from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = Post
        fields = ['id','username','message']