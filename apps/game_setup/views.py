from django.shortcuts import render, HttpResponse, redirect
    # the index function is called when root is visited
def player_selection(request):
    request.session.clear()
    return render(request, "game_setup/player_selection.html")

def rules(request):
    return render(request, "game_setup/rules.html")

def player_registration(request):
    if request.method == "POST":
        request.session['stable'] = True
        print(request.POST)
        # print(request.session['single_player_flag'])
        if 'single_player_flag' in request.POST:
            print("its in post")
            request.session['single_player_flag'] = True
        if 'three_plus_flag' in request.POST:
            if int(request.POST['player_count']) > 2 and int(request.POST['player_count']) < 7:
                count = int(request.POST['player_count']) + 1
                context = {
                "player_count" : range(1,count),
                }
                return render(request, "game_setup/player_registration.html", context)
            else:
                return redirect("/")  
        else:
            count = int(request.POST['player_count']) + 1
            context = {
            "player_count" : range(1,count),
            }
            return render(request, "game_setup/player_registration.html", context)
    else:
        return redirect("/")

def register_players(request):
    if request.method == "POST":
        if 'stable' not in request.session:
            redirect('/')
        print(request.POST)
        player_count = 0
        for key, value in request.POST.items():
            if key[0] == "p":
                player_count += 1
                request.session[key] = value
                # print(request.session[key])
        request.session['player_count'] = player_count
        # print(player_count)
        return redirect("/game_runner/start")
    else:
        return redirect("/")