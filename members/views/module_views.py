from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from members import helpers

from members import models
from members import forms

# index
def module_index(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    modules = models.Module.objects.all().order_by("name")
    
    return render(request, "members/module/module_index.html", {
        "title": "Modul Liste", 
        "modules": modules
    })


# detail
def module_detail(request, id):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    module = get_object_or_404(models.Module, id=id)
    
    return render(request, "members/module/module_detail.html", {
        "title": "Modul Detail",
        "id": id,
        "module": module
    })


# update
def module_update(request, id):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    module = get_object_or_404(models.Module, id=id)

    if request.method == "POST":
        form = forms.ModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            url = reverse("members-module-detail", args=[id])
            return HttpResponseRedirect(url)
    else:
        form = forms.ModuleForm(instance=module)
    
    return render(request, "members/module/module_update.html", {
        "title": module.name, 
        "form": form
    })


# new
def module_new(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    if request.method == "POST":
        form = forms.ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse("members-module-index")
            return HttpResponseRedirect(url)
    else:
        form = forms.ModuleForm()
    
    return render(request, "members/module/module_new.html", {
        "title": "Modul erstellen", 
        "form": form
    })


# delete
def module_delete(request, id):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    module = get_object_or_404(models.Module, id=id)
    
    if request.method == "POST":   
        module.delete()
        url = reverse("members-module-index")
        return HttpResponseRedirect(url)
    
    return render(request, "members/module/module_delete.html", {
        "module": module
    })
