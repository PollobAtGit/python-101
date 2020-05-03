from django.shortcuts import render


def show_all_pages(request):
    return render(request, 'website/home.html')
