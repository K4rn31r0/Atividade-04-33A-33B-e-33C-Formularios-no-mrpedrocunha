from django.shortcuts import render, redirect
from .models import Tips, Recipe
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    tipsList = Tips.objects.all()
    stepsList = Recipe.objects.all()
    return render(request,
                  "homepage.html",
                  context={
                      "Receita": stepsList,
                      "Dicas": tipsList
                  })

@login_required
def forms_tips(request):
    if request.method == "POST":
        Tips.objects.create(title=request.POST["title"],
                            tipType=request.POST["tipType"],
                            importance=request.POST["importance"],
                            warning=request.POST["warning"])
        return redirect("home")
    return render(request,
                  "forms_tips.html",
                  context={"formtype": "Adicionar"})


@login_required
def forms_steps(request):
    if request.method == "POST":
        Recipe.objects.create(title=request.POST["title"],
                              stepNum=request.POST["stepNum"],
                              utensils=request.POST["utensils"],
                              ingredients=request.POST["ingredients"])
        return redirect("home")
    return render(request, "forms_steps.html")

@login_required
def forms_tips_update(request, id):
    tip = Tips.objects.get(id=id)
    if request.method == "POST":
        tip.title = request.POST["title"]
        tip.tipType = request.POST["tipType"]
        tip.importance = request.POST["importance"]
        tip.warning = request.POST["warning"]
        tip.save()
        return redirect("home")
    return render(request,
                  "forms_tips.html",
                  context={
                      "formtype": "Atualizar",
                      "tip": tip
                  })

@login_required
def forms_steps_update(request, id):
    step = Recipe.objects.get(id=id)
    if request.method == "POST":
        step.title = request.POST["title"]
        step.stepNum = request.POST["stepNum"]
        step.utensils = request.POST["utensils"]
        step.ingredients = request.POST["ingredients"]
        step.save()
        return redirect("home")
    return render(request,
                  "forms_steps.html",
                  context={
                      "formtype": "Atualizar",
                      "step": step
                  })

@login_required
def forms_tips_delete(request, id):
    tip = Tips.objects.get(id=id)
    if "confirm" in request.POST:
        tip.delete()
        return redirect("home")
    elif "deny" in request.POST:
        return redirect("home")
    return render(request, "areyousure.html", context={"tip": tip})

@login_required
def forms_steps_delete(request, id):
    step = Recipe.objects.get(id=id)
    if "confirm" in request.POST:
        step.delete()
        return redirect("home")
    elif "deny" in request.POST:
        return redirect("home")
    return render(request, "areyousure.html", context={"step": step})


def create_user(request):
    if request.method == "POST":
        user = User.objects.create_user(
            request.POST["username"],
            request.POST["email"],
            request.POST["password"]
        )
        user.save()
        return redirect("home")
    return render(request, "register.html", context={"action":"Registrar novo"})


def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg":"Erro: O usuário não existe"})
      
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg":"Erro: O usuário não pôde ser logado."})
  return render(request, "login.html")


def logout_user(request):
  logout(request)
  return redirect("login")