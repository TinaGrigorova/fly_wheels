from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            raw_password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=raw_password)

            if user is not None:
                login(request, user)
                next_url = request.POST.get("next") or request.GET.get("next") or "shop"
                return redirect(next_url)

            messages.error(request, "Signed up, but couldn’t log you in automatically. Please sign in.")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})
