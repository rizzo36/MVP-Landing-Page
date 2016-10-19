from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm, SignUpForm
from django.core.mail import send_mail


def home(request):
    title = 'Welcome'
    # if request.user.is_authenticated():
    #     title = "My title %s" % (request.user)
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New Full Name"
        instance.full_name = full_name
        instance.save()

        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)


def contact(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_full_name = form.cleaned_data.get("full_name")
        form_message = form.cleaned_data.get("message")
        # print(email, full_name, message)

        subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, "yourotheremail@blabla.com"]
        contact_message = "%s: %s via %s" % (form_full_name, form_message, form_email)

        send_mail(subject, contact_message, from_email, to_email, fail_silently=False)

    context = {
        "form": form,
        "title": title,
    }
    return render(request, "forms.html", context)


def about(request):
    return render(request, "about.html", {})
