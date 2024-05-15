from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.db.models import Q

from datetime import datetime

from . import helpers
from . import models
from . import forms



# Create your views here.

# members views
# index

# def index(request):
#     if not request.user.is_authenticated:
#         return helpers.not_auth_redirect()
    

#     filter_gender = request.GET.get("gender")
#     filter_module = request.GET.get("module")
#     filter_position = request.GET.get("position")
#     filter_publish_fotos = request.GET.get("publish_fotos")

#     order = request.GET.get("order")
#     order_dir = request.GET.get("order_dir")

#     order_dir_str = ""

#     search = request.GET.get("search")

#     default_filter_values = {
#         "gender": {
#             "value": "all",
#             "title": "Alle"
#         },
#         "module": {
#             "value": "all",
#             "title": "Alle"
#         },
#         "position": {
#             "value": "all",
#             "title": "Alle"
#         },
#         "publish_fotos": {
#             "value": False
#         },
#         "search": {
#             "value": ""
#         },
#         "order": {
#             "value": "default",
#             "title": "Standard"
#         },
#         "order_dir": {
#             "value": "default",
#             "title": "Standard"
#         }

#     }

     
#     members = models.Member.objects.filter(is_active=True).order_by("-id")
#     genders = models.Gender.objects.all()
#     modules = models.Module.objects.all()
#     positions = models.Position.objects.all()

#     if filter_gender != None and filter_gender != "all":
#         try:
#             members = members.filter(gender__id=int(filter_gender))
#             default_filter_values["gender"]["value"] = int(filter_gender)
#             default_filter_values["gender"]["title"] = genders.get(id=int(filter_gender)).name
#         except:
#             url = reverse("members-index")
#             HttpResponseRedirect(url)
        
#     if filter_module != None and filter_module != "all":
#         try:
#             members = members.filter(modules__id=int(filter_module))
#             default_filter_values["module"]["value"] = int(filter_module)
#             default_filter_values["module"]["title"] = modules.get(id=int(filter_module)).name
#         except:
#             url = reverse("members-index")
#             HttpResponseRedirect(url)

#     if filter_position != None and filter_position != "all":
#         try:
#             members = members.filter(positions__id=int(filter_position))
#             default_filter_values["module"]["value"] = int(filter_position)
#             default_filter_values["module"]["title"] = positions.get(id=int(filter_position)).name
#         except:
#             url = reverse("members-index")
#             HttpResponseRedirect(url)


#     if filter_publish_fotos != None:
#         try:
#             members = members.filter(publish_fotos=True)
#             default_filter_values["publish_fotos"]["value"] = True
#         except:
#             url = reverse("members-index")
#             HttpResponseRedirect(url)

#     if search != "" and search != None:
#         try:
#             members = members.filter(Q(firstname__icontains=search) | Q(lastname__icontains=search)).distinct()
#             default_filter_values["search"]["value"] = search
#         except:
#             url = reverse("members-index")
#             HttpResponseRedirect(url)


#     if order_dir != "default":
#         if order_dir == "up":
#             order_dir_str = ""
#             default_filter_values["order_dir"]["value"] = "up"
#             default_filter_values["order_dir"]["title"] = "Aufsteigend"

#         elif order_dir == "down":
#             order_dir_str = "-"
#             default_filter_values["order_dir"]["value"] = "down"
#             default_filter_values["order_dir"]["title"] = "Absteigend"



#     if order != "default":
#         if order == "firstname":
#             members = members.order_by(f"{order_dir_str}{order}")
#             default_filter_values["order"]["value"] = order
#             default_filter_values["order"]["title"] = "Vorname"
#             print(f"{order_dir_str}{order}")
#         elif order == "lastname":
#             members = members.order_by(f"{order_dir_str}{order}")
#             default_filter_values["order"]["value"] = order
#             default_filter_values["order"]["title"] = "Nachname"
#         elif order == "birthday":
#             members = members.order_by(f"{order_dir_str}{order}")
#             default_filter_values["order"]["value"] = order
#             default_filter_values["order"]["title"] = "Geburtstag"
#         elif order == "id":
#             members = members.order_by(f"{order_dir_str}{order}")
#             default_filter_values["order"]["value"] = order
#             default_filter_values["order"]["title"] = "ID"

#     return render(request, "members/index.html", {
#         "title": "Mitglieder Liste", 
#         "members": members, 
#         "genders": genders,
#         "modules": modules,
#         "positions": positions,
#         "filter_defaults": default_filter_values
#     })


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
        

    



# module views
def module_index(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    return render(request, "members/module_index.html", {
        "title": "module index"
    })


# position views
def position_index(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    return render(request, "members/position_index.html", {
        "title": "positions index"
    })