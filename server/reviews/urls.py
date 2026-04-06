from django.urls import path
from . import views

urlpatterns = [
    path('<int:dealer_id>/', views.dealer_reviews, name='dealer-reviews'),
    path('<int:dealer_id>/create/', views.ReviewListCreateView.as_view(), name='review-create'),
    path('fetchReviews/dealer/<int:dealer_id>/', views.fetch_dealer_reviews, name='fetch-dealer-reviews'),
]