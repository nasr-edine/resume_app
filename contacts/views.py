from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm


class ContactCreateView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('home:index')
    success_message = 'Thank you for your message'
    template_name = 'contacts/contact.html'
