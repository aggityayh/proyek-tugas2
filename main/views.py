from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Aggitya Yosafat Hutabarat',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)