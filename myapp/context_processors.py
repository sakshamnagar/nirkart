from myapp.models import MainCategory


def maincat(request):
    maincat = MainCategory.objects.all().order_by('pk')
    return {'maincat': maincat}