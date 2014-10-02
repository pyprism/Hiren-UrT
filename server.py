#!/usr/bin/env python
from twilio.rest import TwilioRestClient
import socket, time


class Hiren:
    def __init__(self, account_sid, auth_token, from_, to):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_ = from_
        self.to = to

    def get_server_details(self, host, port):
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

    def send_sms(self, host, port):
        result = self.get_server_details(host, port)
        while True:
            if len(result['players']) >=3:
                info = "Player:" + str(len(result['players'])) + ", " + "Map: " + result['server_configs']['mapname']
                client = TwilioRestClient(self.account_sid, self.auth_token)
                client.messages.create(to=self.to, from_=self.from_, body=info)
                print "Yo The Hiren!"
                time.sleep(360)



urt = Hiren()
urt.send_sms('116.251.216.132', '1111')
