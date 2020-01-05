from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=20, blank=False)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(product=self)
        return len(ratings)



    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(product=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'product'),)
        index_together = (('user', 'product'),)




