from django.shortcuts import render

def game(request):
    images1 = [f"{k}_de.png" for k in [1,2,3,4,5,6,1,2,3]]
    images2 = [f"{k}_de.png" for k in [1,2,3,4,5,6,1,2,3]]
    
    context = {"images1": images1, "images2": images2}
    return render(request, "game.html",context=context)

