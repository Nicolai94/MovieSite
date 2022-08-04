from django.contrib.flatpages.views import flatpage
from django.urls import path, re_path

from .views import MoviesView, MovieDetailView, AddReview, ActorView, FilterMoviesView, AddStarRating, \
    JsonFilterMoviesView, Search, profile, profile_update

urlpatterns = [
    path('', MoviesView.as_view(), name='basic'),
    path('filter/', FilterMoviesView.as_view(), name='filter'),
    path('search/', Search.as_view(), name='search'),
    path('add-rating/', AddStarRating.as_view(), name='add_rating'),
    path("json-filter/", JsonFilterMoviesView.as_view(), name='json_filter'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>', AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', ActorView.as_view(), name='actor_detail'),
    path('about/', flatpage, {'url': '/about-us/'}, name='about'),
    path('contacts/', flatpage, {'url': '/contacts/'}, name='contacts'),
    path('account/profile/', profile, name='profile'),
    path('account/profile/update/', profile_update, name='profile_update'),
]

