from django.shortcuts import render
from . import models

def main(request):
    banners = models.Banner.objects.filter(is_active = True)[:5]
    info = models.Info.objects.last()
    context = {'banners':banners,
               'info': info}
    return render(request, 'index.html', context)
