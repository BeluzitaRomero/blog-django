from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User as UserAuth

from .forms import UserCreationForm, UserEditForm
from .forms import AvatarForm, CustomAuthenticationForm
from .models import Avatar

def login_request(req):
    form = CustomAuthenticationForm()

    if req.method == 'POST':
        form = CustomAuthenticationForm(req, data = req.POST)

        if form.is_valid():
            user = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')

            user = authenticate(username = user, password = passw)

            if user is not None:
                login(req, user)
                return render(req, 'main.html', {'message': f'Bienvenido {user}'})

            else:
                return render(req, 'User/login.html', {'message': f'Error: el usaurio no existe', 'form': form})
        else:
            return render(req, 'User/login.html', {'message':f'Error, datos incorrectos', 'form':form})
    contexto = {'form': form}
    return render(req, 'User/login.html', contexto)


def register(req):
    if req.method == 'POST':

        # form = UserCreationForm(req.POST) este es el creado por django con textos
        #por defecto
        form = UserCreationForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(req, 'success.html', {'message': "Usuario creado"})

    else: 
        form = UserCreationForm()

    return render(req, 'User/register.html', {'form': form})


# ---------------------------------------------------------------------------- #
#                                  UPDATE USER                                 #
# ---------------------------------------------------------------------------- #

@login_required
def edit_profile(req):
    user = UserAuth.objects.get(id = req.user.id)

    if req.method == 'POST':
        my_form = UserEditForm(req.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            user.username = data['username']
            user.email = data['email']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            
            user.save()

            return redirect('all-posts')

    
    else:
        my_form = UserEditForm(initial = {
                                      'username': user.username,
                                      'email': user.email,
                                      'first_name': user.first_name,
                                      'last_name': user.last_name,
                                       })
    
    return render(req, 'User/edit-profile.html', {'my_form': my_form, 'user': user})


# ---------------------------------------------------------------------------- #
#                                    AVATAR                                    #
# ---------------------------------------------------------------------------- #
@login_required
def create_avatar(req):
    
    # my_form = AvatarForm(instance=avatar)
    


    if req.method == 'POST':
        my_form = AvatarForm(req.POST, req.FILES)
        if my_form.is_valid():
            try:
                old_avatar=Avatar.objects.get(user=req.user)
                if(old_avatar.image):
                    old_avatar.delete()
            except: pass
       
            
        avatar = Avatar(user=req.user, image=my_form.cleaned_data['image'])
        avatar.save()
        return redirect('all-posts')
    else:
        my_form  = AvatarForm()
        return render(req, 'User/edit-avatar.html', {'my_form': my_form})

