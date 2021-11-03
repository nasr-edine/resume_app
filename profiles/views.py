from django.views.generic import TemplateView
from certificates.models import Certificate
from portfolio.models import Portfolio


class HomePageView(TemplateView):
    template_name = "profiles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        certificates = Certificate.objects.filter(is_active=True)
        context["certificates"] = certificates

        portfolio = Portfolio.objects.filter(is_active=True)
        print(portfolio)
        context["portfolio"] = portfolio
        return context
