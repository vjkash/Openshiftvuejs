from django.urls import path
from .views import ProductItemViews,BaseballStatViews

urlpatterns = [
    path('product-items/', ProductItemViews.as_view()),
    path('product-items/<int:id>', ProductItemViews.as_view()),
    path('bball-stats/', BaseballStatViews.as_view()),
    path('bball-stats/<int:id>', BaseballStatViews.as_view())
]