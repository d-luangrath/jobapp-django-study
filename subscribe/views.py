from django.shortcuts import render

# Create your views here.
def subscribe(request):
    email_error_empty = ""
    if request.POST:
        email = request.POST['email']
        print(f"\033[36m█▓▒░ {__name__} | POST REQUEST: {email}\033[0m")
        if email == "":
            email_error_empty = "No email entered."
    context={"email_error_empty": email_error_empty}
    return render(request, 'subscribe/subscribe.html', context)