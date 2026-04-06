from django.urls import path
from . import views

urlpatterns = [
    path('<int:dealer_id>/', views.dealer_reviews, name='dealer-reviews'),
    path('<int:dealer_id>/create/', views.ReviewListCreateView.as_view(), name='review-create'),
    path('<int:dealer_id>/submit/', views.submit_review, name='review-submit'),
]