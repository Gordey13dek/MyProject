from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html', {
        'page_title': 'Головна'
    })


def about(request):
    return render(request, 'home/about.html', {
        'page_title': 'Про нас'
    })


def blog(request):
    return render(request, 'home/blog.html', {
        'page_title': 'Блог'
    })


def contact(request):
    return render(request, 'home/contact.html', {
        'page_title': 'Контакти'
    })


