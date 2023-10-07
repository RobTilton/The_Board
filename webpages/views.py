from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . import models


# Create your views here.


def Home(request):
    if request.user.is_authenticated:
        try:
            user_profile = models.UserProfile.objects.get(user=request.user)
            messages = models.Message.objects.filter(board=user_profile.board)
            return render(request, 'home.html', {'messages': messages})
        except models.UserProfile.DoesNotExist:
            return redirect('login')
    else:
        return redirect('login')


def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            waiting_board = models.Board.objects.get(name='Waiting Board')
            models.UserProfile.objects.create(user=user, board=waiting_board)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



def Boards(request):
    return render(request, 'boards.html')


def Messages(request):
    return render(request, 'messages.html')


def Post_Message(request):
    if request.method == 'POST':
        message_content = request.POST['message']
        if message_content:
            models.Message.objects.create(
                board=request.user.boardmember.board,
                author=request.user,
                content=message_content
            )
    return redirect('home')


def BoardMember(request):
    return render(request, 'board_members.html')