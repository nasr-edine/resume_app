# from django.contrib.auth.models import User
from profiles.models import CustomUser


def project_context(request):
    if request.LANGUAGE_CODE == 'fr':
        context = {
            'me': CustomUser.objects.last(),
        }
    else:
        context = {
            'me': CustomUser.objects.first(),
        }
    return context
