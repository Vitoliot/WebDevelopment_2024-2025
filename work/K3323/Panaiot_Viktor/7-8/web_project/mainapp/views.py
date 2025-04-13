from django.shortcuts import render, redirect
from .forms import FeedbackForm

def index(request):
    return render(request, 'mainapp/index.html')

def about(request):
    return render(request, 'mainapp/about.html')

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранит в модель Feedback
            return redirect('index')  # Или другую страницу, например "Спасибо"
    else:
        form = FeedbackForm()

    return render(request, 'mainapp/contact.html', {'form': form, 'title': 'Обратная связь'})


def map_page(request):
    return render(request, 'mainapp/map.html')
