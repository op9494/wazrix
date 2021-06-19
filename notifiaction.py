import requests
import json
def Send_notification_Android(msg):
    # mention url
    url = "https://www.fast2sms.com/dev/bulk"

    # create a dictionary
    my_data = {
        # Your default Sender ID
        'sender_id': 'FSTSMS',

        # Put your message here!
        'message': msg,

        'language': 'english',
        'route': 'p',

        # You can send sms to multiple numbers
        # separated by comma.
        'numbers': '9994699580,8883312662'
    }


# create a dictionary
    headers = {
        'authorization': 'dx91eUJC2q6pv7IHYoLQMzRVbraifBAu5POyWc3G0DNtnE8XhTfWnUJ4XVhHmuNwlSFY5O8eG3sLtRpv',
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST",
                                url,
                                data=my_data,
                                headers=headers)
#

    returned_msg = json.loads(response.text)


    # print the send message
    print(returned_msg['message'])

