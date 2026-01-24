import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .fortunes import random_fortune
from .models import Author, Topic, Poem
from .serializers import (
    PoemSerializer, PoemTitleSerializer,
    AuthorSerializer, TopicSerializer
)

class FortuneView(APIView):
    def get(self, request):
        return Response({"fortune": random_fortune()})


class RandomIntView(APIView):
    def get(self, request):
        value = random.randint(0, 100)
        return Response({"value": value})

class RandomRangeView(APIView):
    def get(self, request):
        try:
            mn = int(request.query_params.get("min", "0"))
            mx = int(request.query_params.get("max", "100"))
        except ValueError:
            return Response({"error": "min/max must be integers"}, status=status.HTTP_400_BAD_REQUEST)

        if mn > mx:
            return Response({"error": "min must be <= max"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"min": mn, "max": mx, "value": random.randint(mn, mx)})

class RandomSetView(APIView):
    def get(self, request):
        try:
            count = int(request.query_params.get("count", "5"))
            mn = int(request.query_params.get("min", "0"))
            mx = int(request.query_params.get("max", "100"))
        except ValueError:
            return Response({"error": "count/min/max must be integers"}, status=status.HTTP_400_BAD_REQUEST)

        unique = request.query_params.get("unique", "false").lower() in ("1", "true", "yes")

        if count <= 0:
            return Response({"error": "count must be > 0"}, status=status.HTTP_400_BAD_REQUEST)
        if mn > mx:
            return Response({"error": "min must be <= max"}, status=status.HTTP_400_BAD_REQUEST)

        if unique:
            size = (mx - mn + 1)
            if count > size:
                return Response({"error": "count is too large for unique set in this range"}, status=status.HTTP_400_BAD_REQUEST)
            values = random.sample(range(mn, mx + 1), k=count)
        else:
            values = [random.randint(mn, mx) for _ in range(count)]

        return Response({"count": count, "min": mn, "max": mx, "unique": unique, "values": values})

def _random_poem_queryset(qs):
    ids = list(qs.values_list("id", flat=True))
    if not ids:
        return None
    return qs.get(id=random.choice(ids))

class RandomPoemView(APIView):
    def get(self, request):
        poem = _random_poem_queryset(Poem.objects.select_related("author", "topic").all())
        if poem is None:
            return Response({"error": "No poems in database"}, status=status.HTTP_404_NOT_FOUND)
        return Response(PoemSerializer(poem).data)

class RandomPoemByAuthorView(APIView):
    def get(self, request, author_name: str):
        qs = Poem.objects.select_related("author", "topic").filter(author__name__iexact=author_name)
        poem = _random_poem_queryset(qs)
        if poem is None:
            return Response({"error": f"No poems for author '{author_name}'"}, status=status.HTTP_404_NOT_FOUND)
        return Response(PoemSerializer(poem).data)

class RandomPoemByTopicView(APIView):
    def get(self, request, topic_name: str):
        qs = Poem.objects.select_related("author", "topic").filter(topic__name__iexact=topic_name)
        poem = _random_poem_queryset(qs)
        if poem is None:
            return Response({"error": f"No poems for topic '{topic_name}'"}, status=status.HTTP_404_NOT_FOUND)
        return Response(PoemSerializer(poem).data)

class AuthorsListView(APIView):
    def get(self, request):
        authors = Author.objects.order_by("name")
        return Response(AuthorSerializer(authors, many=True).data)

class TopicsListView(APIView):
    def get(self, request):
        topics = Topic.objects.order_by("name")
        return Response(TopicSerializer(topics, many=True).data)

class PoemTitlesByAuthorView(APIView):
    def get(self, request, author_name: str):
        poems = Poem.objects.filter(author__name__iexact=author_name).order_by("title")
        if not poems.exists():
            return Response({"error": f"No poems for author '{author_name}'"}, status=status.HTTP_404_NOT_FOUND)
        return Response(PoemTitleSerializer(poems, many=True).data)

class PoemTitlesByTopicView(APIView):
    def get(self, request, topic_name: str):
        poems = Poem.objects.filter(topic__name__iexact=topic_name).order_by("title")
        if not poems.exists():
            return Response({"error": f"No poems for topic '{topic_name}'"}, status=status.HTTP_404_NOT_FOUND)
        return Response(PoemTitleSerializer(poems, many=True).data)
