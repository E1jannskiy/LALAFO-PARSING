from django.shortcuts import render
from .models import Car, Apartmentsforrent, Saleofapartments


def Car(request):
    
    return render(request, 'index.html')


def Apartmentsforrent(request):
    my_port_list = Apartmentsforrent.objects.all()
    print(my_port_list)
    data = {
        'apartmentsforrent': my_port_list,
    }
    return render(request, 'apartmentsforrent.html', data)


def Saleofapartments(request):
    my_port_list = Saleofapartments.objects.all()
    print(my_port_list)
    data = {
        'saleofapartments': my_port_list,
    }
    return render(request, 'saleofapartments.html', data)
