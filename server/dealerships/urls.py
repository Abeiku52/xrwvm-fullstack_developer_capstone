from django.urls import path
from . import views

urlpatterns = [
    path('', views.DealerListView.as_view(), name='dealer-list'),
    path('<int:pk>/', views.DealerDetailView.as_view(), name='dealer-detail'),
    path('state/<str:state>/', views.dealers_by_state, name='dealers-by-state'),
    path('fetchDealer/<int:dealer_id>/', views.fetch_dealer_by_id, name='fetch-dealer-by-id'),
]