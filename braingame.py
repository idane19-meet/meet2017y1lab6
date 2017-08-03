import random
a_list=[]



#first question
def story1():
    ques1 = input("you are walking into a bar. in the right, u see old man getting robbed. will you help him? (y/n)")
    print("------------------------------------------------------------")
    #what happens in different cases(ques1)
    if ques1 == "y" or ques1=="yes":
        #second question
        ques2 = input("you are getting into a fight with anonymus robbers, you see a gun with your eye. if you want to fight press y. if you wanna run away, press n! ")
        print("------------------------------------------------------------")
        #what happens in different cases(ques2)
        if ques2 == 'y' or ques2 == 'yes':
            #third question
            ques3 = input('the robber pulled the gun on you. would you like to unarm him? if so press y!')
            print("------------------------------------------------------------")
            #what happens in different cases(ques3)
            if ques3 == 'y':
                print('you approched the robber.he aimed the gun towards you and you kicked the gun.you killed the robbers.you see that the old man is not an old man,and he took your wallet.')
                print('will you fight with him(he looks strong) (y), you are going to pick up the gun you kicked before in order to shoot him (n), you let him escape(z)')
                #fourth question
                ques4 = input()
                print("------------------------------------------------------------")
                #what happens in different cases(ques4)
                if ques4 == "y":
                    print("he knocked you out, you woke up in antartica, NAKED, game over!")
                    print("------------------------------------------------------------")
                elif ques4 == "n":

                    #fifth question

                    ques5 = print("you were running to pick the gun off the floor, but the old man escaped.")

                    print('--------------------------------------------------------------------------------------')
                    print(" you are going to your car, and when you are close to your home, the old man jumps on you from the bushes and you started wresling!")
                    ques5 = input('would you like continue wresling with him?press y.would you like shut your door house in his face?press n!')
                    if ques5 == 'n':
                          print('are you afraid?chicken! GAME OVER!')
                    else:
                          print('you continued wresling with the old man,he knocked you out!you woke up in a small room,and you body is tight!')
                          print('the old man walks into the room.he says:"hello ,nice to meet you,my dear son!!!')
                          print('will be continued!!!!!')


###___________________________________________________________________________
def story2():
    ques1 = input("you was hiking with you friends on the everest.blizzard came, and caught you surprised.after the blizzard you could not find your friends.couple of bears are chasing you right now.press y to keep runing(you won't last long).press n to climb on a tree.")
    if ques1 == 'y':
        ques2 = input("you kept runing, suddenly, you stucked in an invisible wall,the bears got closer and closer and dissapered. and fairy appered.the fairy said:'hello young man,i see you are trying to enter our home.we are more than welcome you to come to our house.suddenly you appered in a hospitol, press a if you want to run away,press w if you want to wait(faires are coming to you)")
        if ques2 == 'w':
            ques3 = input("the nurse fairy came to you and said:'you fainted,before 3 days ago,you need to rest.press r to run away after she goes.press s to rest")
            if ques3 == 's':
                ques4 = input("you fell asleep.you woke up in the middle of the night, and heard 2 faires talking quitley,the said something about sacrifaice the human,press g to go and ask them. press s to sleep")
                if ques4 == 's':
                        print("you woke up above a lava mountain,and you heared a lot of noise.the queen of the faires yelled:'the glourius day arrived!we are sacreficing the human to you god,for releace as from our curse.the rope that holds you was started burning.the rope ripped apart.")
                        print('WILL BE CONTINUE!!!')
                else:
                    print('you were asking what they are talking about and they put a spell on you.you appered on mars.GAME OVER')
                              
                    
            else:
                print('you started running away,when a spell was shot on you and you are fried.GAME OVER')
        else:
            print('you jumped from a 100 meters window,you are DEAD. GAME OVER!')
    else:
        print('you slipped off the tree and the bears had eaten you! GAME OVER!')

a_list.append(story1)
a_list.append(story2)
x = random.randint(1,2)
if x == 1:
    story1()
else:
    story2()

 
