from rest_framework import serializers
from .models import Author, Topic, Poem

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["id", "name"]

class PoemSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    topic = TopicSerializer(allow_null=True)

    class Meta:
        model = Poem
        fields = ["id", "title", "text", "author", "topic"]

class PoemTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ["id", "title"]
