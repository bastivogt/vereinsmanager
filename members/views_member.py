from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.db.models import Q


from . import helpers
from . import models
from . import forms






def index(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    

    filter_gender = request.GET.get("gender")
    filter_module = request.GET.get("module")
    filter_position = request.GET.get("position")
    filter_publish_fotos = request.GET.get("publish_fotos")

    order = request.GET.get("order")
    order_dir = request.GET.get("order_dir")

    order_dir_str = ""

    search = request.GET.get("search")

    show_adult_with_child_rate = request.GET.get("show_adult_with_child_rate")

    print(f"sawcr: {show_adult_with_child_rate}")
 
    members = models.Member.objects.filter(is_active=True).order_by("-id")
    genders = models.Gender.objects.all()
    modules = models.Module.objects.all()
    positions = models.Position.objects.all()

    if filter_gender != None and filter_gender != "all":
        try:
            members = members.filter(gender__id=int(filter_gender))
        except:
            url = reverse("members-index")
            HttpResponseRedirect(url)
        
    if filter_module != None and filter_module != "all":
        try:
            members = members.filter(modules__id=int(filter_module))
        except:
            url = reverse("members-index")
            HttpResponseRedirect(url)

    if filter_position != None and filter_position != "all":
        try:
            members = members.filter(positions__id=int(filter_position))
        except:
            url = reverse("members-index")
            HttpResponseRedirect(url)


    if filter_publish_fotos != None:
        try:
            members = members.filter(publish_fotos=True)
        except:
            url = reverse("members-index")
            HttpResponseRedirect(url)

    if search != "" and search != None:
        try:
            members = members.filter(Q(firstname__icontains=search) | Q(lastname__icontains=search)).distinct()
        except:
            url = reverse("members-index")
            HttpResponseRedirect(url)


    if order_dir != "default":
        if order_dir == "up":
            order_dir_str = ""

        elif order_dir == "down":
            order_dir_str = "-"



    if order != "default":
        if order == "firstname":
            members = members.order_by(f"{order_dir_str}{order}")
            print(f"{order_dir_str}{order}")
        elif order == "lastname":
            members = members.order_by(f"{order_dir_str}{order}")
        elif order == "birthday":
            members = members.order_by(f"{order_dir_str}{order}")
        elif order == "id":
            members = members.order_by(f"{order_dir_str}{order}")



    if show_adult_with_child_rate != None:

        members = members.filter(rate__name="Kind")
        members = [member for member in members if member.get_age() > 18]



    return render(request, "members/index.html", {
        "title": "Mitglieder Liste", 
        "members": members, 
        "genders": genders,
        "modules": modules,
        "positions": positions,
    })





# member_detail
def member_detail(request, id):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    member = get_object_or_404(models.Member, id=id)
    return render(request, "members/member_detail.html", {
        "title": "Mitglied Detail",
        "id": id,
        "member": member
    })


#new
def member_new(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    if request.method == "POST":
        form = forms.MemberForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse("members-index")
            return HttpResponseRedirect(url)
    else:
        form = forms.MemberForm()


    
    return render(request, "members/member_new.html", {
        "title": "Mitglied erstellen",
        "form": form
    })


#change
def member_update(request, id):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    member = get_object_or_404(models.Member, id=id)
    
    if request.method == "POST":
        form = forms.MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            url = reverse("members-member-detail", args=[id])
            return HttpResponseRedirect(url)
    else:
        form = forms.MemberForm(instance=member)


    
    return render(request, "members/member_update.html", {
        "title": member.get_fullname(),
        "form": form, 
        "id": id
    })


def member_delete(request, id):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    member = get_object_or_404(models.Member, id=id)
    
    if request.method == "POST":
        print("DELETE")
        member.delete()
        url = reverse("members-index")
        return HttpResponseRedirect(url)
    
    return render(request, "members/member_delete.html", {
        "member": member
    })