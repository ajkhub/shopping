from . models import category
def menulink(request):
    link=category.objects.all()
    return dict(link=link)