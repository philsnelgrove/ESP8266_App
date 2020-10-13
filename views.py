# from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from ESP8266_Control.models import Device
from ESP8266Server.Server import Logic
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    ip = ""
    port = 9999
    command = "toggle_led"
    data = ""
    # Logic.Handler.send_command_to_node(request, ip, port, command, data)

    device_list = Device.objects.order_by('-id')
    template = loader.get_template('ESP8266_App/index.html')
    context = {
        'command': command,
        'device_list': device_list,
    }
    return HttpResponse(template.render(context, request))
