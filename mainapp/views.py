from django.shortcuts import render


def mainpage(request):
    return render(request, template_name='mainapp/mainpage.html')

def videorec_page(request, sname):
    return render(request, 'mainapp/videorec_page.html', context={'name': sname})