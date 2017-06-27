from django.shortcuts import render, redirect

from utils import message
from .models import Message
from .forms import MessageForm
from secret_key import keys


def sms_send(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            content = form.cleaned_data['content']
            results = message.send_message(recipient, content)
            Message.objects.create(
                sender=keys.api_phone_number,
                recipient=recipient,
                content=content
            )
            context = {
                'form': MessageForm(),
                'results': results
            }
    else:
        context = {
            'form': MessageForm(),
        }
    return render(request, 'message/send.html', context=context)
