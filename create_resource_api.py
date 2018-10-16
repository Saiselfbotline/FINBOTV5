import urllib.request, urllib.parse
import ssl
import json
import sys
import base64

base_url = 'https://192.168.0.50/'
username = 'vic'
password = 'P4sswOrd!'
admin_domain_name = 'Main'
resource_uid = 'stgdb.example.com'
resource_name = 'Staging DB'
auth = base64.b64encode(bytes(username + ':' + password, "utf-8")).decode("ascii")

# Allow untrusted SSL certificate (ok for testing)
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# Get admin domain
# Basic Authentication header has to be sent pre-emptively
req = urllib.request.Request(
    base_url + 'ispim/rest/organizationcontainers/admindomains?filter=(ou=%s)' % urllib.parse.quote(admin_domain_name),
    headers={
        'Authorization': 'Basic %s' % auth
    }
)

response = urllib.request.urlopen(req)
response_json = json.loads(response.read().decode('utf-8'))

if len(response_json) > 0:
    admin_domain_uri = response_json[0]['_links']['self']['href']
else:
    print('Error: Admin domain not found, please enter a valid admin domain.')
    sys.exit(1)

# Create Resource
request_json = {
    'createList': [
        {
		'_links': {
			'container': {
				'href': admin_domain_uri
			}
		},
		'_attributes': {
			'uid': [resource_uid],
			'name': [resource_name]
		}
	}
    ]
}

data = json.dumps(request_json).encode('utf-8')

# Note: Basic authentication header has to be sent in every request

request = urllib.request.Request(base_url + 'ispim/rest/resources',
    data,
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-HTTP-Method-Override': 'SUBMIT-IN-BATCH',
        'Authorization': 'Basic %s' % auth
    }
)

try:
    response = urllib.request.urlopen(request)

    if response.code == 200:
        print('The request to create Resource "' + resource_name + '" is successful')
    else:
        response_json = json.loads(response.read().decode('utf-8'))
        print('Bad request: "' + response_json + '"')
except urllib.request.URLError as e:
    print(e.code)
    print(e.read())
