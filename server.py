#!/usr/bin/env python
from twilio.rest import TwilioRestClient
import socket

account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)

def get_server_details(host, port):
    # Data Place Holders
    urt_server_details = {}

    # Socket Request Message
    MESSAGE = "\377\377\377\377getstatus"

    # Get response from server
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)
    sock.connect((host, int(port)))
    sock.send(MESSAGE)
    response, addr = sock.recvfrom(1024)
    sock.close()
    response_lines = response.split("\n")

    # Retrieve the server settings
    config_string_parts = response_lines[1].split("\\")
    urt_server_details['server_configs'] = {}
    for i in range(1, len(config_string_parts), 2):
        urt_server_details['server_configs'][config_string_parts[i].strip()] = config_string_parts[i + 1].strip()

    urt_server_details['players'] = []
    for x in range(2, (len(response_lines) - 1)):
        player_data = response_lines[x].split(" ",2)
        player_dictionary = {"ping": player_data[1], "kills": player_data[0], "name": player_data[2][1:-1]}
        urt_server_details['players'].append(player_dictionary)

    return urt_server_details

def get_server_info(id, host, port):
	# response = {
	# 'id' : id,
	# 'data' : {},
	# 'status' : 'ok'
	# }

	#try:
	#	response['data'] = get_server_details('209.190.50.170', '27960')
    #    print 2

		#The angular controller only use mapname so dont send the whole config list
		#response['data']['server_configs'] = { 'mapname' : response['data']['server_configs']['mapname']}

	#except Exception, e:
	#	response['status'] = str(e)

	#return response
    pass
a = get_server_details('209.190.50.170', '27960')
print len(a['players'])
print a['server_configs']['mapname']

info = "Player:" + str(len(a['players'])) + ", " + "Map: " + a['server_configs']['mapname']


message = client.messages.create(to="", from_="",body=info)