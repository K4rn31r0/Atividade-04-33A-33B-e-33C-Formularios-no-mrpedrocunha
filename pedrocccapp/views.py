from django.shortcuts import render, redirect
from .models import Tips, Recipe


def homepage(request):
    tipsList = Tips.objects.all()
    stepsList = Recipe.objects.all()
    return render(request, "homepage.html", context={ "Receita":stepsList, "Dicas":tipsList})

def forms_tips(request):
  if request.method == "POST":
    Tips.objects.create(
      title = request.POST["title"],
      tipType = request.POST["tipType"],
      importance = request.POST["importance"],
      warning = request.POST["warning"]
    )
    return redirect("home")
  return render(request, "forms_tips.html", context={"formtype":"Adicionar"})

def forms_steps(request):
  if request.method == "POST":
    Recipe.objects.create(
      title = request.POST["title"],
      stepNum = request.POST["stepNum"],
      utensils = request.POST["utensils"],
      ingredients = request.POST["ingredients"]
    )
    return redirect("home")
  return render(request, "forms_steps.html")

def forms_tips_update(request, id):
  tip = Tips.objects.get(id = id)
  if request.method == "POST":
    tip.title = request.POST["title"]
    tip.tipType = request.POST["tipType"]
    tip.importance = request.POST["importance"]
    tip.warning = request.POST["warning"]
    tip.save()
    return redirect("home")
  return render(request, "forms_tips.html", context={"formtype":"Atualizar","tip":tip})

def forms_steps_update(request, id):
  step = Recipe.objects.get(id = id)
  if request.method == "POST":
    step.title = request.POST["title"]
    step.stepNum = request.POST["stepNum"]
    step.utensils = request.POST["utensils"]
    step.ingredients = request.POST["ingredients"]
    step.save()
    return redirect("home")
  return render(request, "forms_steps.html", context={"formtype":"Atualizar","step":step})

def forms_tips_delete(request, id):
  tip = Tips.objects.get(id = id)
  if "confirm" in request.POST:
    tip.delete()
    return redirect("home")
  elif "deny" in request.POST:
    return redirect("home")
  return render(request, "areyousure.html", context={"tip":tip})

def forms_steps_delete(request, id):
  step = Recipe.objects.get(id = id)
  if "confirm" in request.POST:
    step.delete()
    return redirect("home")
  elif "deny" in request.POST:
    return redirect("home")
  return render(request, "areyousure.html", context={"step":step})