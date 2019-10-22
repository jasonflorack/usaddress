import json
import usaddress

while True:
    input_addr = raw_input()
    print json.dumps(usaddress.tag(input_addr))
