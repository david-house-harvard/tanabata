from tempmail import TempMail
import json


# generate temporary email
def temporary_email_generate():
    tm = TempMail()
    email = tm.get_email_address()
    print('Your email is: ', email)

    return email

# check the inbox


def get_mails(email_address):
    tm = TempMail()

    inbox = tm.get_mailbox(email_address.encode('utf-8'))
    dumped = json.dumps(inbox)
    text = dumped.split()

    if text[0] == '{"error":':
        print('the inbox is empty')
    else:
        print('inbox isn\'t empty')

    return inbox

# upload json to python and split string


def get_link(mails):
    data = json.dumps(mails)
    # data_string = str(mails)
    split_email = data.split()

    return split_email

# cut string and extract the link


def get_clear_link(split_email):
    link = []
    str(split_email)
    for i in split_email:
        if i.startswith('https:'):
            link.append(i)
            break

    return link[0][0:97]
