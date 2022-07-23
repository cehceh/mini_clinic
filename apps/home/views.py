from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib import messages
from django.conf import settings
import os, re, uuid
# from django.utils import translation
# from metclinic.utils import auth_required



# Create your views here.

# @auth_required
def frontpage(request):
    ''' Home page before user sign in '''
    # label = 'b8:76:3f:de:e2:e9'#os.environ.get('SERIAL')
    # # print (label) 
    # mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    # print (mac, label) 
    # if mac == label:
    #     messages.success(request, 'you are authorized')
    # else:
    #     messages.success(request, 'you are not authorized')
        
    # remote_address = request.META.get('REMOTE_ADDR')
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # print(remote_address)
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[-1].strip()
    #     # ip = x_forwarded_for.split(',')[0]
    #     # return ip
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    #     # return ip
    # context = {}
    # messages.success(request, remote_address)
    # print(x_forwarded_for)
    return redirect('patientdata:table_patient')
    # return render(request, 'home/frontpage.html', context)

def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# @auth_required
def dashboard(request):
    ''' Dashboard page main page means English'''
    # from xml.dom import minidom
    # # parse an xml file by name
    # mydoc = minidom.parse('myfile.xml')
    # items = mydoc.getElementsByTagName('item')
    # # num1 = items[0].firstChild.data          # access data
    # # attr1 = items[0].attributes['num'].value # access atribute name value
    # num2 = items[1].childNodes[0].data       # access data
    # # attr2 = items[1].attributes['num'].value # access atribute name value
    
    context = {
        # 'num2':num2,
    }
    return render(request, 'home/dashboard.html', context)

def contacts(request):
    '''  '''
    return render(request, 'home/contacts.html', {})


