from django.shortcuts import render

def show_main(request):
    context = {
        'application_name' : 'SHOP GO',
        'student_name' : 'Nevin Thang',
        'npm' : '2306203204',
        'class' : 'PBP B',
    }

    return render(request, "main.html", context)
