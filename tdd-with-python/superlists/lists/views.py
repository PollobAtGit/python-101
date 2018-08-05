from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home_page(request):
    if request.method == "POST":
        return render(request, 'lists/home_page.html', {
            'new_item_text': request.POST.get('new_item_name')
        })

    return render(request, 'lists/home_page.html')
