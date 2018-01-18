#!/usr/bin/env python
# -*- coding: utf-8 -*-

SCRIPT_NAME    = "MqttNotifier"
SCRIPT_AUTHOR  = "ark <quentrg@gmail.com>"
SCRIPT_VERSION = "0.0.1"
SCRIPT_LICENSE = "MIT"
SCRIPT_DESC    = "Sends HL and PM to MQTT server using TLS encrytption and certificate authentication"
SCRIPT_COMMAND = "mqtt_notifier"

try:
    import weechat
except:
    print("This script must be run under WeeChat.")
    print("Get WeeChat now at: http://www.weechat.org/")
    quit()

import paho.mqtt.client as mqtt

weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", "")


def notify(data, bufferp, uber_empty, tagsn, isdisplayed, ishilight, prefix, message):
    if int(ishilight) == 1 and bufferp != weechat.current_buffer():
        client = mqtt.Client()
        client.tls_set("/home/ark/projects/weechat-mqtt-notify/pub/ca.crt"
                       "/home/ark/projects/weechat-mqtt-notify/pub/client.crt",
                       "/home/ark/projects/weechat-mqtt-notify/pub/client.key")
        client.connect("4rk.fr", 8883, 60)
        client.publish("mqtt_irc_hl", "%s: %s" % (prefix, message))
        client.disconnect()
    return weechat.WEECHAT_RC_OK

hook = weechat.hook_print("", "irc_privmsg", "", 1, "notify", "")
