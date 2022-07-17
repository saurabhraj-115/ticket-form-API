from urllib import response
from bottle import route, template, run, static_file, request, response
import json
import requests


@route('/create_ticket', method=['GET', 'POST'])
def handle_form():
    status = ''
    if request.POST:
        # Get the form data
        name=request.forms.get('name')
        subject = request.forms.get('subject')
        description = request.forms.get('description')
        email = request.forms.get('email')
        # Package the data for the API
        data = {'request': {"requester": {"name": name, "email": email}, 'subject': subject, 'comment': {'body': description}}}
        ticket = json.dumps(data)
        # Make the API request
        url = 'https://ronnyslounge.zendesk.com/api/v2/requests.json'
        headers = {'content-type': 'application/json'}
        r = requests.post(
        url,
        data=ticket,
        headers=headers
        )
        #If everything went well
        if r.status_code == 201:
            status = 'Ticket was created.'   
        else:
            status = 'Problem with the request. Status ' + str(r.status_code)
        
    return template('ticket_form', feedback = status)
    


@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')
run(host='localhost', port=8080, debug=True)
