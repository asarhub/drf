from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from background_task import background


@background(schedule=60)
def email_function(request):
    subject = "Test Subject"
    message = "<h1>Hello world</h1>"
    from_email = "from-user@gmail.com"
    to_email = "to-user@gmail.com"
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [to_email, ])
        except:
            print("error sending in mail")
# To make above code work, we need to install mailcachar and then check
