from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.db.models import Count
from .forms import ContactsForm
from .models import Product, Zipper, Slider, Waistbelt, Beltbuckle, Lace, Button, Contact, Teammember
from multiselectfield import MultiSelectField
#from apt.models import Appointment
from itertools import count
import operator


# Create your views here.

def index(request):
    #contact us
    form = ContactsForm(request.POST or None)
    team = Teammember.objects.all()
    if form.is_valid():
        newcontact = form.save(commit=False)
        newcontact.save()
        return render(request, 'home/index.html', {
            'newcontact': newcontact,
            'form': form,
        })
    contacts = Contact.objects.all()
    return render(request, 'home/index.html', {
        'contacts': contacts,
        'form': form,
        'team': team,
    })

def products_index(request):
    product_list = Product.objects.values('product_name').annotate(Count('product_name'))
    return render(request, 'home/productsalt.html', {'product_list': product_list})

#beltbuckles
def beltbuckles_index(request):
    #beltbuckles = Beltbuckle.objects.values('category').annotate(Count('category'))
    beltbuckles = sorted(Beltbuckle.objects.annotate(Count('category')), key=operator.attrgetter("category"))
    return render(request, 'home/beltbuckles.html', {'beltbuckles': beltbuckles})
'''
def pinbuckle_index(request):
    pinbuckle_buckles = Beltbuckle.objects.filter(category='Pin Buckle')
    return render(request, 'home/pinbucklebelts.html', {'pinbuckle_buckles': pinbuckle_buckles})
'''
#zippers
def zippers_index(request):
    #zippers = Zipper.objects.values('category').annotate(Count('category'))
    zippers = sorted(Zipper.objects.annotate(Count('category')), key=operator.attrgetter("category"))
    #zippers = Zipper.objects.all()
    return render(request, 'home/zippersalt.html', {'zippers': zippers})
'''
def metalz_index(request):
    metalz = Zipper.objects.filter(category='Metal')
    return render(request, 'home/metalz.html', {'metalz': metalz})

'''
#laces
def laces_index(request):
    #laces = Lace.objects.values('category').annotate(Count('category'))
    laces = sorted(Lace.objects.annotate(Count('category')), key=operator.attrgetter("category"))
    return render(request, 'home/laces.html', {'laces': laces})
'''
def chest_index(request):
    chestlaces = Lace.objects.filter(category='Chest')
    return render(request, 'home/lacefolder/chestlaces.html', {'chestlaces': chestlaces})

'''
#waistbelts
def waistbelts_index(request):
    #waistbelts = Waistbelt.objects.values('category').annotate(Count('category'))
    waistbelts = sorted(Waistbelt.objects.annotate(Count('category')), key=operator.attrgetter("category"))
    return render(request, 'home/waistbelts.html', {'waistbelts': waistbelts})

#sliders
def sliders_index(request):
    #sliders = Slider.objects.values('category').annotate(Count('category'))
    sliders = sorted(Slider.objects.annotate(Count('category')), key=operator.attrgetter("category"))
    return render(request, 'home/slidersalt.html', {'sliders': sliders})
'''
def metals_index(request):
    metals = Slider.objects.filter(category='Metal')
    return render(request, 'home/metals.html', {'metals': metals})

'''
#buttons
def buttonsc_index(request):
    #btnbycat = Button.objects.values('category').annotate(Count('category'))
    btnbycat = sorted(Button.objects.annotate(Count('category')), key=operator.attrgetter("category"))
    return render(request, 'home/buttonsc.html', {'btnbycat': btnbycat})
'''
def bonehorn_index(request):
    bonehornbtn = Button.objects.filter(category='Bone Horn')
    return render(request, 'home/btnfolder/bonehorn.html', {'bonehornbtn': bonehornbtn})
'''
def buttonss_index(request):
    #btnbystyle = Button.objects.values('style').annotate(Count('style'))
    btnbystyle = Button.objects.annotate(Count('style'))
    return render(request, 'home/buttonss.html', {'btnbystyle': btnbystyle})
'''
def twohole_index(request):
    twoholebtn = Button.objects.filter(style__icontains='Two Hole')
    return render(request, 'home/btnfolder/twohole.html', {'twoholebtn': twoholebtn})

'''
