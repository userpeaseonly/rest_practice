from rest_framework import serializers

from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        depth = 1
        extra_kwargs = {
            'updated_at': {'write_only': True},
            'title': {'min_length': 100, 'required': True},
        }
