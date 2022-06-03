from random import*

choices = ['Rock', 'Paper', 'Scissors']
user_box = {'r':'Rock', 'p':'Paper', 's':'Scissors'}
sh = 'rps'

while True:
        print("User please, select.. Rock, Paper, Scissors\n press R for Rock, P for paper and S for Scissors")
        user = str(input("::"))
        comp = choice(choices)
        if user.lower() not in sh:
                print("Wrong Input")
        new_user = user_box.get(user.lower())
        print(f'\nPlayer`s choice : {new_user}, Comp`s choice : {comp}\n')
        if new_user == comp:
                print("Tie")
        else:
                if comp[0] == 'R' and  new_user[0] == 'S':
                        print("Comp Wins")
                elif comp[0] == 'P' and new_user[0] == 'R':
                        print("Comp Wins")
                elif comp[0] == 'S' and new_user[0] == 'P':
                        print("Comp Wins")
                elif new_user[0] == 'R' and  comp[0] == 'S':
                        print("Player Wins")
                elif new_user[0] == 'P' and comp[0] == 'R':
                        print("Player Wins")
                elif new_user[0] == 'S' and comp[0] == 'P':
                        print("Player Wins")
                break
                
                        
        
