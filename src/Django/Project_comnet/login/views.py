from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render

dir_list = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]


@csrf_protect
def register(request):  # 회원가입 요청일때, 일어나는 함수 임.
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )


def register_success(request):
    return render_to_response(
        'registration/success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    return render_to_response(
        'home.html',
        {'user': request.user}
    )


@csrf_exempt
def game(request):
    sets = [[0 for i in range(8)] for i in range(8)]
    if request.method == 'POST':
        context = {'sets': sets}
        return render(request, 'gamerooms.html', context)
    else:
        sets[3][3] = 1
        sets[3][4] = 2
        sets[4][3] = 2
        sets[4][4] = 1
        context = {'sets': sets}
        return render(request, 'gamerooms.html', context)
