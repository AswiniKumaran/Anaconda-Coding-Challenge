import json
import random

from django.shortcuts import render
from django.shortcuts import redirect, reverse

user_score = 0
computer_score = 0
name = ''


def play_game(request):
    global user_score, computer_score, name
    # import pdb
    # pdb.set_trace()
    context = {
        'player_choice': "None",
        'computer_choice': "None",
        'user_score': user_score,
        'computer_score': computer_score,
        'name': name
    }
    if request.POST:
        options = ['rock', 'paper', 'scissor']
        user_option = request.POST.get('choice')
        computer_option = random.choice(options)
        winning_combination = {
            'rock': 'scissor',
            'scissor': 'paper',
            'paper': 'rock'
        }
        if user_option == computer_option:
            outcome = 'tie'
        elif winning_combination[user_option] == computer_option:
            outcome = 'win'
            user_score += 1

        else:
            outcome = 'lose'
            computer_score += 1

        context = {
            'player_choice': user_option,
            'computer_choice': computer_option,
            'outcome': outcome,
            'user_score': user_score,
            'computer_score': computer_score,
            'name': name,

        }
    return render(request, 'play_game/python_post.html', context)

def intro(request):
    if request.GET:
        global name
        name = request.GET.get('name')
        return redirect(reverse("play"))
    else:
        return render(request, 'play_game/intro.html')
