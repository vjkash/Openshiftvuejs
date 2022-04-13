from django.db import models

# Create your models here.
class ProductItem(models.Model):
    
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()
    product_type = models.CharField(max_length=50,default='Home')
    product_priority = models.CharField(max_length=10,default='Low')
    product_date_created = models.DateField(auto_now=True)

class BaseballStat(models.Model):
    
    player_name = models.TextField()
    team_name = models.TextField()
    position = models.TextField()
    player_age = models.PositiveIntegerField()
    games_played = models.PositiveIntegerField()
    at_bats = models.PositiveIntegerField()
    runs = models.PositiveIntegerField()
    home_runs = models.PositiveIntegerField()
    rbi = models.PositiveIntegerField()
    