from django.shortcuts import render

from .forms import MessageForm


def sms_send(request):
    if request.method == 'POST':
        pass
    else:
        form = MessageForm()
        context = {
            'form': form,
        }
        return render(request, 'message/send.html', context=context)