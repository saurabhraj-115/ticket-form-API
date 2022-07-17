from urllib import response
from bottle import route, template, run, static_file, request, response
import json
import requests


@route('/create_ticket', method=['GET', 'POST'])
def handle_form():
    # if 'verified_email' in request.cookies:
    #     ask_email = False
    # else:
    #     ask_email = True
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
        # user = email + '/RaXrqXT0cOZjzIhSUP50JCFjohLecBRhGt36Ihc9'
        # api_token = 'RaXrqXT0cOZjzIhSUP50JCFjohLecBRhGt36Ihc9'
        url = 'https://ronnyslounge.zendesk.com/api/v2/requests.json'
        headers = {'content-type': 'application/json'}
        r = requests.post(
        url,
        data=ticket,
        # auth=(user, api_token),
        headers=headers
        )
        #If everything went well
        if r.status_code == 201:
            status = 'Ticket was created.'   
        else:
            status = 'Problem with the request. Status ' + str(r.status_code)
        #For Email Authentication Failiure
        # if r.status_code != 201:
        #     if r.status_code == 401 or 422:
        #         status = 'Could not authenticate you. Check your email address or register.'
        #     else:
        #         status = 'Problem with the request. Status ' + str(r.status_code)
            
        # else:
        #     status = 'Ticket was created.'
            # if 'verified_email' not in request.cookies:
            #     response.set_cookie('verified_email', email, max_age=364*24*3600)
            #     ask_email = False
    return template('ticket_form', feedback = status)
    # return template('ticket_form')

# @route('/newpage', method=['GET', 'POST'])  
# def newpage():
#     return template('newpage')



@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')
run(host='localhost', port=8080, debug=True)
