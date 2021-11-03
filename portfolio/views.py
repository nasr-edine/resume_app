from django.views.generic import ListView, DetailView
from .models import Portfolio


class PortfolioList(ListView):
    model = Portfolio
    template_name = "portfolio/portfolio.html"


class PortfolioDetail(DetailView):
    model = Portfolio
    template_name = "portfolio/portfolio-detail.html"
