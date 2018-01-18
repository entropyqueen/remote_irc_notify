# remote_irc_notify
Simple, secure, lightweight notification system using MQTT over TLSv1.2 to forward hilight notifications from remote IRC client (weechat) to local notifier daemon.

Using TLSv1.2 for encryption and authentication of subscribers and publisher.

## STILL A WORK IN PROGRESS
 * The proof of concept is functionnal.
 * Weechat plugin should be working.
 * MQTT server configuration is good

### TODO
 * Add deploy script
 * Provide proper code and cmdline for local notifier
 * Update plugin for better management (commands and settings must be added)

## USAGE

In order to use this you will have to install a few requirements:

### Server side

 * generate the CA keys and certificate
 * generate the server certificate, signed by the CA

 * install mosquitto server
 * copy ca.crt, server.crt, server.key on the mosquitto_conf directory
 * launch mosquitto using `mosquitto -c mosquitto.conf`
 
 * generate a client certificate signed with the CA
 * load the MqttNotifier.py file in weechat

### Client side

 * Generate client certificate, signed with the CA
 * launch the client
 
For each HL or PM, the plugin will make a MQTT publish request to the server, which will then be forwarded to the subscribers 
