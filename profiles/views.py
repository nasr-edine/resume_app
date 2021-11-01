from django.views.generic import TemplateView
# from certificates.models import Certificate
# from portfolio.models import Portfolio


class HomePageView(TemplateView):
    template_name = "profiles/index.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    # testimonials = Testimonial.objects.filter(is_active=True)
    # certificates = Certificate.objects.filter(is_active=True)
    # blogs = Blog.objects.filter(is_active=True)
    # portfolio = Portfolio.objects.filter(is_active=True)

    # context["testimonials"] = testimonials
    # context["certificates"] = certificates
    # context["blogs"] = blogs
    # context["portfolio"] = portfolio
    # return context
