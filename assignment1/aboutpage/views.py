from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    context = {
        'name': 'Kate Trisha Mae F. Ayuste',
        'student_id': '2023-02721',
    }
    return render(request, 'about.html', context)
