from django.urls import path
from .views import PortfolioList, PortfolioDetail

app_name = 'portfolio'
urlpatterns = [
    path('', PortfolioList.as_view(), name="portfolios"),
    path('<slug:slug>', PortfolioDetail.as_view(), name="portfolio"),

]
