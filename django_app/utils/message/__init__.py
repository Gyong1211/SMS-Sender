from secret_key import keys

from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


def send_message(number, text):
    api_key = keys.api_key
    api_secret = keys.api_secret

    params = dict()
    params['type'] = 'sms'  # Message type ( sms, lms, mms, ata )
    params['to'] = number  # Recipients Number '01000000000,01000000001'
    params['from'] = keys.api_phone_number  # Sender number
    params['text'] = text  # Message

    cool = Message(api_key, api_secret)
    try:
        response = cool.send(params)
        result = [
            "Sender : {}".format(params['from']),
            "Recipients : {}".format(params['to']),
            "Success Count : {}".format(response['success_count']),
            "Group ID : {}".format(response['group_id']),
            "Error Count : {}".format(response['error_count'])
        ]

        if "error_list" in response:
            result.append("Error List : {}".format(response['error_list']))
        return result
    except CoolsmsException as e:
        print(type(e.msg))
        result = ["Error Code : {}".format(e.code)]
        return result
