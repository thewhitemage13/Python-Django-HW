from django.urls import path
from .views import (
    FortuneView,
    RandomIntView, RandomRangeView, RandomSetView,
    RandomPoemView, RandomPoemByAuthorView, RandomPoemByTopicView,
    AuthorsListView, TopicsListView, PoemTitlesByAuthorView, PoemTitlesByTopicView
)

urlpatterns = [
    path("fortune/", FortuneView.as_view()),
    path("random/int/", RandomIntView.as_view()),
    path("random/range/", RandomRangeView.as_view()),
    path("random/set/", RandomSetView.as_view()),
    path("poems/random/", RandomPoemView.as_view()),
    path("poems/random/author/<str:author_name>/", RandomPoemByAuthorView.as_view()),
    path("poems/random/topic/<str:topic_name>/", RandomPoemByTopicView.as_view()),
    path("poems/authors/", AuthorsListView.as_view()),
    path("poems/topics/", TopicsListView.as_view()),
    path("poems/titles/author/<str:author_name>/", PoemTitlesByAuthorView.as_view()),
    path("poems/titles/topic/<str:topic_name>/", PoemTitlesByTopicView.as_view()),
]
