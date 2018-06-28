from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from sharedcare.forms import SignUpForm
from sharedcare.models import UserProfile


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Saves the internal user

            user_profile = UserProfile()
            user_profile.birth_date = form.cleaned_data.get('birth_date')
            user_profile.cpf = form.cleaned_data.get('cpf')
            user_profile.user = user

            user.profile = user_profile

            user_profile.save()
            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # Send user back to the site's home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})
