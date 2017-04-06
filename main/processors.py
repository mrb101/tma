from .models import Branding


def logo(request):
    logo = Branding.objects.latest('updated')
    return {'logo': logo}
