from django.shortcuts import render
from subscribe.models import Subscribe

def subscribe(request):
    email_error_empty = ""
    if request.POST:
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        print(f"\033[36m█▓▒░ {__name__} | POST REQUEST: {email}\033[0m")
        if email == "":
            email_error_empty = "No email entered"

        subscribe = Subscribe(
                            first_name=first_name,
                            last_name=last_name,
                            email=email
                        )    
        subscribe.save()
    context={"email_error_empty": email_error_empty}
    return render(request, 'subscribe/subscribe.html', context)