
from rest_framework import viewsets,status
from .models import Product
from .models import Rating
from .serializer import ProductSerializer, RatingSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
#from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        serializer = UserSerializer(User.objects, many=True)
        response = {'message': 'User retrieve', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
   # permission_classes = (AllowAny,)

    def list(self, request):
        serializer = ProductSerializer(Product.objects, many=True)
        response = {'message': 'Product retrieve', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)


    @action(detail=True, methods=['POST'])
    def rate_product(self, request, pk=None):
        if 'stars' in request.data:
            product = Product.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            try:
                rating = Rating.objects.get(user=user.id, product=product.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                # new rating created
                rating = Rating.objects.create(user=user, product=product, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
    #permission_classes = (AllowAny,)

    # overwriting this method
    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # overwriting this method
    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

