from email.policy import default
from rest_framework import serializers
from .models import ProductItem,BaseballStat

class ProductItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)
    product_type = serializers.CharField(max_length=50,default='Home')
    product_priority = serializers.CharField(max_length=10,default='Low')
    product_date_created = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = ProductItem
        fields = ('__all__')

class BaseballStatSerializer(serializers.ModelSerializer):
    player_name = serializers.CharField(max_length=100)
    team_name = serializers.CharField(max_length=10)
    position = serializers.CharField(max_length=10)
    player_age = serializers.IntegerField()
    games_played = serializers.IntegerField()
    at_bats = serializers.IntegerField()
    runs = serializers.IntegerField()
    home_runs = serializers.IntegerField()
    rbi = serializers.IntegerField()

    class Meta:
        model = BaseballStat
        fields = ('__all__')