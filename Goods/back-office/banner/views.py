from django.shortcuts import render
from Goods import models

def createBanner(request):
    if request.method == 'POST':
        models.Banner.objects.create(
            title = request.POST['title'],
            sub_title = request.POST['sub_title'],
            img = request.FILES['images']
        )
    return render(request, 'back-office/banner/create.html')
