# from django.contrib.auth.models import User
from profiles.models import CustomUser


def project_context(request):
    context = {
        'me': CustomUser.objects.first(),

    }

    return context
