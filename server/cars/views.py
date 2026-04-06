from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CarMake, CarModel
from .serializers import CarMakeSerializer, CarModelSerializer

class CarMakeListView(generics.ListAPIView):
    """API view to retrieve all car makes with their models"""
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer

@api_view(['GET'])
def all_car_makes_models(request):
    """API view to retrieve all car makes and models"""
    makes = CarMake.objects.prefetch_related('models').all()
    serializer = CarMakeSerializer(makes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_cars(request):
    """API view to get car makes and models in required format"""
    car_data = [
        {"CarMake": "Toyota", "CarModel": "Camry"},
        {"CarMake": "Toyota", "CarModel": "RAV4"},
        {"CarMake": "Toyota", "CarModel": "Prius"},
        {"CarMake": "Honda", "CarModel": "Accord"},
        {"CarMake": "Honda", "CarModel": "CR-V"},
        {"CarMake": "Honda", "CarModel": "Civic"},
        {"CarMake": "Ford", "CarModel": "F-150"},
        {"CarMake": "Ford", "CarModel": "Mustang"},
        {"CarMake": "Ford", "CarModel": "Explorer"},
        {"CarMake": "Chevrolet", "CarModel": "Silverado"},
        {"CarMake": "Chevrolet", "CarModel": "Equinox"},
        {"CarMake": "BMW", "CarModel": "3 Series"},
        {"CarMake": "BMW", "CarModel": "X5"},
        {"CarMake": "Mercedes-Benz", "CarModel": "C-Class"},
        {"CarMake": "Mercedes-Benz", "CarModel": "GLE"},
    ]
    
    return Response({"CarModels": car_data})