from django.shortcuts import render
from django.http import HttpResponse
from ESP8266_Control.models import Device
from ESP8266Server.Server import Logic
from ESP8266Server.Server import Data
import pprint

pp = pprint.PrettyPrinter(indent=4)


def index(request, device_id="0"):
    output = '{}'.format(device_id)
    return HttpResponse(output)


def command(request, device_id, command):
    myDataSource = Data.DataSource()
    myDevice = myDataSource.node_lookup_by_id(device_id)
    deviceId = [item[0] for item in myDevice][0]
    name = [item[1] for item in myDevice][0]
    mac_address = [item[2] for item in myDevice][0]
    last_connected = [item[3] for item in myDevice][0]
    ip_address = [item[4] for item in myDevice][0]
    connected = [item[5] for item in myDevice][0]
    status = [item[6] for item in myDevice][0]
    led_status = [item[7] for item in myDevice][0]
    output = "COMMAND: {}() being sent to ID{}: {} - MAC:{} Last Connected:{} | IP:{} Connected:{} Status:{} LED:{}".format(command, deviceId, name, mac_address, last_connected, ip_address, connected, status, led_status)
    port = 9998
    # Logic.send_command_to_node(request, ip_address, port, command)
    return HttpResponse(output)


def command_params(request, device_id, command, params):
    myDataSource = Data.DataSource()
    myDevice = myDataSource.node_lookup_by_id(device_id)
    deviceId = [item[0] for item in myDevice][0]
    name = [item[1] for item in myDevice][0]
    mac_address = [item[2] for item in myDevice][0]
    last_connected = [item[3] for item in myDevice][0]
    ip_address = [item[4] for item in myDevice][0]
    connected = [item[5] for item in myDevice][0]
    status = [item[6] for item in myDevice][0]
    led_status = [item[7] for item in myDevice][0]
    output = "COMMAND:{}({}) being sent to ID{}: {} - MAC:{} Last Connected:{} | IP:{} Connected:{} Status:{} LED:{}".format(command, params, deviceId, name, mac_address, last_connected, ip_address, connected, status, led_status)
    port = 9998
    # Logic.send_command_to_node(request, ip_address, port, command, params)
    return HttpResponse(output)
