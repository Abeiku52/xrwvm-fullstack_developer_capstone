from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from dealerships.models import Dealer
from .models import Review
from .serializers import ReviewSerializer
import requests

class ReviewListCreateView(generics.ListCreateAPIView):
    """API view to list and create reviews"""
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        dealer_id = self.kwargs.get('dealer_id')
        return Review.objects.filter(dealer_id=dealer_id)
    
    def perform_create(self, serializer):
        dealer_id = self.kwargs.get('dealer_id')
        dealer = get_object_or_404(Dealer, id=dealer_id)
        
        # Get sentiment analysis
        review_text = serializer.validated_data.get('review_text', '')
        sentiment = self.analyze_sentiment(review_text)
        
        serializer.save(
            user=self.request.user,
            dealer=dealer,
            sentiment=sentiment
        )
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of review text"""
        try:
            # Call sentiment analysis service
            response = requests.post(
                'http://localhost:5000/analyze',
                json={'text': text},
                timeout=5
            )
            if response.status_code == 200:
                return response.json().get('sentiment', 'neutral')
        except:
            pass
        return 'neutral'

@api_view(['GET'])
def dealer_reviews(request, dealer_id):
    """Get all reviews for a specific dealer"""
    reviews = Review.objects.filter(dealer_id=dealer_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def submit_review(request, dealer_id):
    """Submit a new review for a dealer"""
    try:
        dealer = get_object_or_404(Dealer, id=dealer_id)
        
        # Get or create a default user for demo purposes
        user, created = User.objects.get_or_create(
            username='demo_user',
            defaults={
                'first_name': 'Demo',
                'last_name': 'User',
                'email': 'demo@example.com'
            }
        )
        
        # Get review data
        data = request.data
        review_text = data.get('review_text', '')
        rating = int(data.get('rating', 5))
        car_make = data.get('car_make', '')
        car_model = data.get('car_model', '')
        car_year = data.get('car_year')
        reviewer_name = data.get('reviewer_name', 'Anonymous')
        
        # Analyze sentiment
        sentiment = analyze_sentiment_simple(review_text)
        
        # Delete existing review from demo_user to avoid unique constraint
        Review.objects.filter(dealer=dealer, user=user).delete()
        
        # Create review
        review = Review.objects.create(
            dealer=dealer,
            user=user,
            rating=rating,
            review_text=review_text,
            car_make=car_make,
            car_model=car_model,
            car_year=int(car_year) if car_year else None,
            sentiment=sentiment
        )
        
        serializer = ReviewSerializer(review)
        return Response({
            'status': 'success',
            'message': 'Review submitted successfully',
            'review': serializer.data
        }, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fetch_dealer_reviews(request, dealer_id):
    """Get all reviews for a specific dealer with required format"""
    reviews = Review.objects.filter(dealer_id=dealer_id)
    
    formatted_reviews = []
    for review in reviews:
        formatted_review = {
            'id': review.id,
            'name': review.user.get_full_name() or review.user.username,
            'dealership': review.dealer.name,
            'review': review.review_text,
            'purchase': True if review.car_make else False,
            'purchase_date': review.purchase_date.isoformat() if review.purchase_date else None,
            'car_make': review.car_make,
            'car_model': review.car_model,
            'car_year': review.car_year,
            'sentiment': review.sentiment,
            'rating': review.rating
        }
        formatted_reviews.append(formatted_review)
    
    return Response(formatted_reviews)