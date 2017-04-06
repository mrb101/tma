from .models import Base


def logo(request):
    if Base.objects.all().exists():
        base = Base.objects.latest('updated')
        return {'base': base}
    return {}
