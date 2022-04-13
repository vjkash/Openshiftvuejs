from django.shortcuts import render,get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from .serializers import ProductItemSerializer, BaseballStatSerializer
from .models import ProductItem, BaseballStat

# Create your views here.
class ProductItemViews(APIView):
    def post(self, request):
        serializer = ProductItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    #@method_decorator(cache_page(60*15))
    def get(self, request, id=None):
        if id:
            item = ProductItem.objects.get(id=id)
            serializer = ProductItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        dbhits = 1
        if 'productdbhits' in cache:
            print("Found product db hit metric in Cache")
            dbhits = cache.get('productdbhits')
            dbhits = dbhits + 1
            cache.set('productdbhits', dbhits, timeout=None)
        else:
        # store data in cache
            print("Setting Product DB Hit Metrics Cache")
            #set this to not expire
            cache.set('productdbhits', 1, timeout=None)
        items = ProductItem.objects.all()
        
        serializer = ProductItemSerializer(items, many=True)
        data = {
            'items': serializer.data,
            'hits': dbhits
        }
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)
    def patch(self, request, id=None):
        item = ProductItem.objects.get(id=id)
        serializer = ProductItemSerializer(item, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    def delete(self, request, id=None):
        item = get_object_or_404(ProductItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

class BaseballStatViews(APIView):
    def post(self, request):
        serializer = BaseballStatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*1))
    def get(self, request, id=None):
        
        if id:
            item = BaseballStat.objects.get(id=id)
            serializer = BaseballStatSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        dbhits = 1
        if 'baseballdbhits' in cache:
            print("Found baseball db hit metric in Cache")
            dbhits = cache.get('baseballdbhits')
            dbhits = dbhits + 1
            cache.set('baseballdbhits', dbhits, timeout=None)
        else:
        # store data in cache
            print("Setting Baseball DB Hit Metric Cache")
            #set this to not expire
            cache.set('baseballdbhits', 1, timeout=None)
        items = BaseballStat.objects.all()
        serializer = BaseballStatSerializer(items, many=True)
        data = {
            'items': serializer.data,
            'hits': dbhits
        }
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)
    