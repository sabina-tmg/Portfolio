from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .forms import ContactForm
from .models import ContactMessage

def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                number=form.cleaned_data['number'],
                content=form.cleaned_data['content'],
            )

            messages.success(request, "Your message has been sent!")

            # Email to the user
            subject_user = "Thank you for your message"
            from_email = "syangtansabina8@gmail.com"
            to_user = [contact_message.email]

            html_message_user = render_to_string("app/msg.html", {'name': contact_message.name})
            text_message_user = (
                f"Hello {contact_message.name},\n"
                "Thank you for reaching out! We have received your message and will get back to you shortly.\n\n"
                "Best regards,\nSabina Tamang"
            )

            email_user = EmailMultiAlternatives(subject_user, text_message_user, from_email, to_user)
            email_user.attach_alternative(html_message_user, "text/html")
            email_user.send(fail_silently=False)

            # Email notification to admin
            subject_admin = f"New message from {contact_message.name}"
            admin_email = ["syangtansabina8@gmail.com"]  # Admin email(s)

            text_message_admin = (
                f"New contact message received:\n\n"
                f"Name: {contact_message.name}\n"
                f"Email: {contact_message.email}\n"
                f"Number: {contact_message.number}\n"
                f"Message:\n{contact_message.content}"
            )

            email_admin = EmailMultiAlternatives(subject_admin, text_message_admin, from_email, admin_email)
            email_admin.send(fail_silently=False)

            return redirect("home")  # avoid resubmission on refresh
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, "app/home.html", {"form": form})

def about(request):
    return render(request, "app/about.html")

def projects(request):
    return render(request, "app/project.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                number=form.cleaned_data['number'],
                content=form.cleaned_data['content'],
            )

            messages.success(request, 'Your message has been sent successfully!')

            # Email to the user
            subject_user = "Thank you for your message"
            from_email = "syangtansabina8@gmail.com"
            to_user = [contact_message.email]

            html_message_user = render_to_string("app/msg.html", {'name': contact_message.name})
            text_message_user = (
                f"Hello {contact_message.name},\n"
                "Thank you for reaching out! We have received your message and will get back to you shortly.\n\n"
                "Best regards,\nSabina Tamang"
            )

            email_user = EmailMultiAlternatives(subject_user, text_message_user, from_email, to_user)
            email_user.attach_alternative(html_message_user, "text/html")
            email_user.send(fail_silently=False)

            # Email notification to admin
            subject_admin = f"New message from {contact_message.name}"
            admin_email = ["syangtansabina8@gmail.com"]  # Admin email(s)

            text_message_admin = (
                f"New contact message received:\n\n"
                f"Name: {contact_message.name}\n"
                f"Email: {contact_message.email}\n"
                f"Number: {contact_message.number}\n"
                f"Message:\n{contact_message.content}"
            )

            email_admin = EmailMultiAlternatives(subject_admin, text_message_admin, from_email, admin_email)
            email_admin.send(fail_silently=False)

            return redirect('contact')  # Adjust URL name if different
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'app/contact.html', {'form': form})
