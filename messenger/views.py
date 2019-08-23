# Yuren "Rock" Pang
# COMP346 Homework 5
# Professor Shilad Sen
# Collaborated with Daniel Lim

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .messageInfo import messageInfo
from .models import Message


@login_required
def home(request):
    messages = Message.objects.filter(sender=request.user)
    return render(request, 'messenger/home.html', {'messages': messages})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'messenger/signup.html', {'form': form})

def message_draft(request):
    user_str = request.user.username
    current_user = User.objects.get(username=user_str)
    message_list = Message.objects.filter(sender=current_user, draft=True).order_by("date")

    return render(request, 'messenger/draft.html', {'message_list': message_list})

def message_received(request):
    user_str = request.user.username
    current_user = User.objects.get(username=user_str)
    message_list = Message.objects.filter(receiver=current_user, draft=False).order_by("date")

    return render(request, 'messenger/history_message.html', {'message_list': message_list})

def message_sent(request):
    user_str = request.user.username
    current_user = User.objects.get(username=user_str)
    message_list = Message.objects.filter(sender=current_user, draft=False).order_by("date")

    return render(request, 'messenger/history_message.html', {'message_list': message_list})


def edit(request, pk):
    message = get_object_or_404(Message, pk=pk)

    if request.method == 'POST':
        form = messageInfo(request.POST, instance=message)
        if form.is_valid():
            user_str = request.user.username
            message = form.save(commit=False)
            message.sender = User.objects.get(username=user_str)
            message.save()
            if message.draft:
                return redirect('message_draft')
            else:
                return redirect('message_sent')
    else:
        form = messageInfo(instance=message)
    return render(request, "messenger/write.html", {'form': form})

def message_write(request):
    if request.method == 'POST':
        form = messageInfo(request.POST)
        if form.is_valid():
            user_str = request.user.username
            message = form.save(commit=False)
            message.sender = User.objects.get(username=user_str)
            message.save()
            if message.draft:
                return redirect('message_draft')
            else:
                return redirect('message_sent')
    else:
        form = messageInfo()
    return render(request, "messenger/write.html", {'form': form})