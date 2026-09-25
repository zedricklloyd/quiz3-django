from django.shortcuts import render

# Create your views here.
def student_profile(request):
    student = [
        {"name": "Jose Jorquia", "age": 20, "course": "BSIT"},
        {"name": "Mark Llanora", "age": 22, "course": "BSA"},
        {"name": "Zedrick Lacuesta", "age": 20, "course": "BSE"},
        {"name": "Jonel Pronton", "age": 19, "course": "BSBA"},
        {"name": "Mark Deguzman", "age": 23, "course": "BSAIS"},
        {"name": "Jhonas San Agustin", "age": 21, "course": "BSPA"},
    ]
    return render(request, "main/home.html", {"student": student})