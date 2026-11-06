from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from .models import Perfil


def login_sige(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            perfil = Perfil.objects.get(
                usuario=user
            )

            if perfil.tipo == 'admin':
                return redirect('/')

            elif perfil.tipo == 'professor':
                return redirect('/professor/')

            elif perfil.tipo == 'secretaria':
                return redirect('/secretaria/')

            elif perfil.tipo == 'responsavel':
                return redirect('/familia/')

    return render(
        request,
        'login.html'
    )