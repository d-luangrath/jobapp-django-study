from django.shortcuts import redirect, render
from django.urls import reverse
from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            # print(f"\033[36m█▓▒░ {__name__} | valid form \033[0m")
            # print(f"\033[34m█▓▒░ {__name__} | {subscribe_form.cleaned_data} \033[0m")
            # email = subscribe_form.cleaned_data['email']
            # first_name = subscribe_form.cleaned_data['first_name'] 
            # last_name = subscribe_form.cleaned_data['last_name']
            # print(f"\033[35m█▓▒░ {__name__} | {email} \033[0m")
            # subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
            # subscribe.save()
            return redirect(reverse('thank_you'))
    context={"form": subscribe_form, "email_error_empty": email_error_empty}
    return render(request, 'subscribe/subscribe.html', context)

def thank_you(request):
    context = {}
    return render(request, 'subscribe/thank_you.html', context)