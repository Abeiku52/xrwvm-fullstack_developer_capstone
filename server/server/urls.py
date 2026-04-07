"""
URL configuration for car dealership project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Add Django auth URLs
    path('login/', views.login_page, name='login'),
    path('djangoapp/logout/', views.api_logout_get, name='djangoapp-logout'),
    path('api/auth/login/', views.api_login, name='api_login'),
    path('api/auth/logout/', views.api_logout_get, name='api_logout'),
    path('api/auth/register/', views.api_register, name='api_register'),
    path('api/dealers/', include('dealerships.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/cars/', include('cars.urls')),
    path('djangoapp/get_cars/', views.get_cars_direct, name='get-cars-direct'),
    path('analyze/<str:text>/', views.analyze_sentiment_get, name='analyze-sentiment-get'),
    path('', views.home_page, name='home'),
    path('about/', TemplateView.as_view(template_name='static/About.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='static/Contact.html'), name='contact'),
    path('dealers/state/', TemplateView.as_view(template_name='static/dealers_by_state.html'), name='dealers-by-state'),
    path('dealer/<int:dealer_id>/', TemplateView.as_view(template_name='static/dealer_details.html'), name='dealer-details'),
    path('dealer/<int:dealer_id>/review/', TemplateView.as_view(template_name='static/post_review.html'), name='post-review'),
    path('dealer/<int:dealer_id>/review/success/', TemplateView.as_view(template_name='static/review_success.html'), name='review-success'),
    # Deployed versions for screenshots
    path('deployed/', TemplateView.as_view(template_name='static/index_logged_in.html'), name='deployed-home'),
    path('dealer/<int:dealer_id>/deployed/', TemplateView.as_view(template_name='static/dealer_details_deployed.html'), name='deployed-dealer-details'),
    path('deployed/review/display/', TemplateView.as_view(template_name='static/deployed_review_display.html'), name='deployed-review-display'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)