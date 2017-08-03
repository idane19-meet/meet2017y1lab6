def story2():
    ques1 = input("you was hiking with you friends on the everest.blizzard came, and caught you surprised.after the blizzard you could not find your friends.couple of bears are chasing you right now.press y to keep runing(you won't last long).press n to climb on a tree.")
    if ques1 == 'y':
        ques2 = input("you kept runing, suddenly, you stucked in an invisible wall,the bears got closer and closer and dissapered. and fairy appered.the fairy said:'hello young man,i see you are trying to enter our home.we are more than welcome you to come to our house.suddenly you appered in a hospitol, press a if you want to run away,press w if you want to wait(faires are coming to you)")
        if ques2 == 'w':
            ques3 = input("the nurse fairy came to you and said:'you fainted,before 3 days ago,you need to rest.press r to run away after she goes.press s to rest")
            if ques3 == 's':
                ques4 = input("you fell asleep.you woke up in the middle of the night, and heard 2 faires talking quitley,the said something about sacrifaice the human,press g to go and ask them. press s to sleep")
                if ques4 == 's':
                        input("")
                else:
                    print('you were asking what they are talking about and they put a spell on you.you appered on mars.GAME OVER')
                              
                    
            else:
                print('you started running away,when a spell was shot on you and you are fried.GAME OVER')
        else:
            print('you jumped from a 100 meters window,you are DEAD. GAME OVER!')
    else:
        print('you slipped off the tree and the bears had eaten you! GAME OVER!')

story2()
