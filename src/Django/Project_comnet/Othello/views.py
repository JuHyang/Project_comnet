from Othello.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render

ingame = [[0 for i in range(8)] for i in range(8)]
player_turn = list()
room = list()
dir_list = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
room_num = 0
play_num = 1


def turn(x, y, p, sets):
    d_list = []
    change = []
    x -= 1
    y -= 1

    if sets[x][y] != 0:
        return 1

    if p == 1:
        for i in range(8):
            d_x = x + dir_list[i][0]
            d_y = y + dir_list[i][1]

            if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                continue

            if sets[d_x][d_y] == 2:
                d_list.append(dir_list[i])
            else:
                continue

        if len(d_list) == 0:
            return 1

        for i in range(len(d_list)):
            stack = []
            d_x = x + d_list[i][0]
            d_y = y + d_list[i][1]

            if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                continue

            while 1:
                stack.append((d_x, d_y))
                d_x += d_list[i][0]
                d_y += d_list[i][1]

                if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                    break

                if sets[d_x][d_y] == 1:
                    change = change + stack
                    break
                elif sets[d_x][d_y] == 0:
                    stack = []
                    break

        if len(change) == 0:
            return 1

        while len(change) != 0:
            (a, b) = change.pop()
            sets[a][b] = 1
            if len(change) == 0:
                sets[x][y] = 1

    else:
        change = []

        for i in range(8):
            d_x = x + dir_list[i][0]
            d_y = y + dir_list[i][1]

            if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                continue

            if sets[d_x][d_y] == 1:
                d_list.append(dir_list[i])
            else:
                continue

        if len(d_list) == 0:
            return 1

        for i in range(len(d_list)):
            stack = []
            d_x = x + d_list[i][0]
            d_y = y + d_list[i][1]

            if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                continue

            while 1:
                stack.append((d_x, d_y))
                d_x += d_list[i][0]
                d_y += d_list[i][1]

                if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                    break

                if sets[d_x][d_y] == 2:
                    change = change + stack
                    break
                elif sets[d_x][d_y] == 0:
                    stack = []
                    break

        if len(change) == 0:
            return 1

        while len(change) != 0:
            (a, b) = change.pop()
            sets[a][b] = 2
            if len(change) == 0:
                sets[x][y] = 2
    return 0


def determine(p, sets):
    stack = []

    for i in range(8):
        for j in range(8):

            if sets[i][j] == 0:
                for k in range(8):
                    d_x = i + dir_list[k][0]
                    d_y = j + dir_list[k][1]

                    if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                        continue

                    if sets[d_x][d_y] != p and sets[d_x][d_y] != 0:
                        stack.append((d_x, d_y))

    if len(stack) == 0:
        return 1
    return 0


def finish(sets):
    p_1 = 0
    p_2 = 0

    for i in range(8):
        for j in range(8):
            if sets[i][j] == 1:
                p_1 += 1
            elif sets[i][j] == 2:
                p_2 += 1

    if determine(1, sets) == 1 and determine(2, sets) == 1:
        if p_1 > p_2 :
            return 1
        elif p_2 > p_1 :
            return 2

    if p_1 + p_2 > 63 :
        if p_1 > p_2:
            return 1
        elif p_2 > p_1 :
            return 2
    return 0


@csrf_protect
def register(request):  # 회원가입 요청일때, 일어나는 함수 임.
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )


def register_success(request):
    return render_to_response(
        'registration/success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    return render_to_response(
        'home.html',
        {'user': request.user}
    )


@csrf_exempt
def game(request):
    context = {'sets': ingame}
    return render(request, 'gamerooms.html', context)


def game_enter(request, user_id):
    global room_num
    global play_num
    global room
    global player_turn
    if request.method == 'GET':

        player = User.objects.get(username=user_id)
        player.player_num = play_num
        player.room_num = room_num + 1
        player.save()
        if player.player_num == 1:
            room_num += 1
            room.append(ingame)
            player_turn.append(1)
            room[room_num - 1][3][3] = 1
            room[room_num - 1][3][4] = 2
            room[room_num - 1][4][3] = 2
            room[room_num - 1][4][4] = 1
            play_num = 2
        elif player.player_num == 2:
            play_num = 1

        context = {'sets': room[room_num - 1], 'room_num': room_num, 'player_num': player.player_num,
                   'text': player_turn[room_num - 1]}
        return render(request, 'gamerooms.html', context)
    else:
        message = "잠시만 기다려주세요"
        text = 0
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        room_num_pre = int(request.POST['room_num'])
        player_num_pre = int(request.POST['player_num'])
        if player_num_pre == player_turn[room_num_pre - 1]:
            sign_det = determine(player_num_pre, room[room_num_pre - 1])
            if sign_det == 0:
                sign_turn = turn(y, x, player_num_pre, room[room_num_pre - 1])

                if sign_turn == 1:
                    player_turn[room_num_pre - 1] = player_num_pre
                else:
                    if player_num_pre == 1:
                        player_turn[room_num_pre - 1] = 2
                    elif player_num_pre == 2:
                        player_turn[room_num_pre - 1] = 1
                sign_finish = finish(room[room_num_pre-1])
                if sign_finish == 1 :
                    message = "Player1 is Win !!"
                elif sign_finish == 2:
                    message = "Player2 is Win !!"
                else :
                    message = ""
            elif sign_det == 1:
                if player_num_pre == 1:
                    player_turn[room_num_pre - 1] = 2
                elif player_num_pre == 2:
                    player_turn[room_num_pre - 1] = 1

        text = player_turn[room_num_pre - 1]

        context = {'sets': room[room_num_pre - 1], 'room_num': room_num_pre, 'player_num': player_num_pre, 'text': text, 'message' : message}
        return render(request, 'gamerooms.html', context)
