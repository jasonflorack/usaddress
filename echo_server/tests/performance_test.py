import usaddress
import json

addr='123 Main St. Suite 100 Chicago, IL, 12345-2540'

for i in range(0, 1000):
	print json.dumps(usaddress.tag(str(i)+addr))

