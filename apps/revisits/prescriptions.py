import os, re, uuid, socket
from pathlib import Path
from django.core.exceptions import PermissionDenied 

# import sysconfig
# new_path = sysconfig.get_paths()['stdlib']
# from newpath.mypackage.myfile import auth_required



def auth_required(function):
    def wrap(request, *args, **kwargs):
        # joins elements of getnode() after each 2 digits. 
        # using regex expression 
        label = 'b8:76:3f:de:e2:e8'        #os.environ.get('SERIAL')
        var = os.environ.get('VARIABLE')
        # print (label) 
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        # print(sysconfig.get_paths()['purelib'])
        # print(sysconfig.get_paths()['stdlib'])

        # remote_address = request.META.get('REMOTE_ADDR')
        # my_addr = request.get_host()        #request._current_scheme_host
        # hostname = socket.gethostname() 
        # ip = socket.gethostbyname(hostname)
        # # my_ip = '127.0.0.1'
        # ip1 = '192' + '.' + '168' + '.' + '1' + '.' + '55' #remote_address
        # print('myaddress=', my_addr, ' my machine name=',hostname, ' ip=',ip, ' the_remote_ip',remote_address)

        # print (mac, label) 
        # print(function)
        if label == mac:
            # messages.success(request, 'you are authorized')
            return function(request, *args, **kwargs)
        else:
            # messages.success(request, 'you are not authorized')
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap