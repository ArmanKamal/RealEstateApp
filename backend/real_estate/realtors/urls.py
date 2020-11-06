from django.urls import path
from .views import RealtorListView,SingleRealtorView,TopSellerView

urlpatterns = [
    path('',RealtorListView.as_view()),
    path('topseller',TopSellerView.as_view()),
    path('<pk>',SingleRealtorView.as_view())
]
