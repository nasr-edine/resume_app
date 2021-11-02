# from django.contrib.auth.models import User
from profiles.models import CustomUser


def project_context(request):
    user = CustomUser.objects.first()

    print(user.avatar.url)
    context = {
        'me': CustomUser.objects.first(),

    }

    return context
