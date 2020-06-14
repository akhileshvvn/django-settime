from django.shortcuts import render


def index(request):
    context = {
        'posts': ["Great"]
        if request.user.is_authenticated else []
    }

    return render(request, 'signin/index.html', context)