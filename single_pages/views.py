from django.shortcuts import render

# Create your views here.

# 함수 생성
def landing(request):
    return render(request,
                  template_name='single_pages/landing.html',
                  context={
                      'title': 'Landing',
                      'name': '송준영'
                  })

def about_me(request):
    return render(request,
                  template_name='single_pages/aboutme.html',
                  context={
                      'title': 'about_Me',
                      'name': 'about_Me'
                  })
