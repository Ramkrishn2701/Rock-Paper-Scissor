from django.shortcuts import render
from home.models import Player

def index(request):
    return render(request, 'index.html')
def Players(request):
    if request.method == 'POST':
        player1_name = str(request.POST['player1'])
        player2_name = str(request.POST['player2'])
        message=""
        if player1_name and player2_name:
            if player1_name != player2_name:
                player1 = Player.objects.create(name=player1_name)
                player1.save()

                player2 = Player.objects.create(name=player2_name)
                player2.save()
                
                return render(request, 'play.html',{'player1':player1,'player2':player2})
            else:
                message = "Name Already Taken Choose Anothr Name"
                return render(request, 'index.html', {'message': message})
        else:
            message = "Please enter both player names."
            return render(request, 'index.html', {'message': message})
def reset(request,value1,value2):
        player1 = Player.objects.get(pk=value1)
        player2 = Player.objects.get(pk=value2)

        player1.score = 0
        player1.attempts = 6
        player2.score = 0
        player2.attempts = 6
        round =0
        player1.save()
        player2.save()

        message = "Game Reset Successfully" 
        return render(request,'play.html',{'player1':player1,'player2':player2,'message':message,'round':round})

def play(request,value1,value2):
    if request.method =='POST':

        pl_1 = str(request.POST['pl-1'])
        pl_2 = str(request.POST['pl-2'])
        
        player1 = Player.objects.get(pk=value1)
        player2 = Player.objects.get(pk=value2)

        
        while(player1.attempts>0):
                round = 6 - (player1.attempts-1)
                if pl_1 == pl_2:
                    player1.attempts-=1
                elif(pl_1=="rock" and pl_2=="paper"):
                   
                        player2.score+=1
                        player1.attempts-=1
                   
                elif(pl_1=="rock" and pl_2=="scissor"):
                    
                        player1.score+=1
                        player1.attempts-=1
                   
                elif(pl_1=="paper" and pl_2=="scissor"):
                   
                        player2.score+=1
                        player1.attempts-=1
                   
                elif(pl_1=="paper" and pl_2=="rock"):
                    
                        player1.score+=1
                        player1.attempts-=1
                    
                elif(pl_1=="scissor" and pl_2=="rock"):
                  
                        player2.score+=1
                        player1.attempts-=1
                    
                elif(pl_1=="scissor" and pl_2=="paper"):
                        player1.score+=1
                        player1.attempts-=1
               
                
                
                if (player2.score<player1.score):
                    message =f"{player1.name} Wins"
                    player1.wins+=1
                    player2.loss+=1
                    
                elif(player1.score<player2.score):
                    message = f"{player2.name} Wins"
                    player2.wins+=1
                    player1.loss+=1
                    
                elif(player1.score == player2.score):
                    player1.draw+=1
                    player2.draw+=1
                    message = "It's a Draw"
                player1.save()
                player2.save()

                return render(request,'play.html',{'player1':player1,'player2':player2,'message':message,'round':round})
                
def game_data(request,value1,value2):
    player1Data = Player.objects.get(pk=value1)
    player2Data = Player.objects.get(pk=value2)
    return render(request,'gameData.html',{'Data1':player1Data,'Data2':player2Data})