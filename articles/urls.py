from django.urls import path
from .views import (
    ArticlesListView,
    ArticlesCreateView,
    ArticlesDeleteView,
    ArticlesDetailView,
    ArticlesUpdateView,
)


urlpatterns = [
    path('<int:pk>/', ArticlesDetailView.as_view(), name='articles_detail'),
    path('new/', ArticlesCreateView.as_view(), name='articles_new'),
    path('<int:pk>/update/', ArticlesUpdateView.as_view(), name='articles_update'),
    path('<int:pk>/delete/', ArticlesDeleteView.as_view(), name='articles_delete'),
    path('', ArticlesListView.as_view(), name='articles_list'),
]
