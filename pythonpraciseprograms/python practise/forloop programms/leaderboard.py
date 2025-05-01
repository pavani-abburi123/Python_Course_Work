import random
def display(l,purpose):
    print('Leader board'.center(30,'-'),'-',purpose)
    for i,val in enumerate(l):
          print(i,".",val)

l=[]
print('Results of my game')
while True:
    print('1.Create a Leaderboard')
    print('2.Add Multiple Players')
    print('3.Add a Single Player')
    print('4.Remove a Player')
    print('5. Find a Player')
    print('6.Sort the Leaderboard:-(Highest to Lowest)')
    print('7.Sort the Leaderboard:-(Lowest to Highest)')
    print('8.Check the Leaderboard ')
    print('9.Tie Break ')
    print('10.Top Players')
    print('11.Least Players')
    print('12.Score Division:-Gold (Above 400)')
    print('13.Score Division:-Silver (Between 250 and 400)')
    print('14.Score Division:-Bronze (Below 250)')
    print('15.Clear Leaderboard ')
    print('16. Exit')

    ch=int(input('enter the choice:'))

    if ch==1:
        n=int(input('enter the no of players:'))
        l=[(random.randint(1,5))*100 for i in range(n)]
        display(l,'Create a Leaderboard')
    elif ch==2:
        n=int(input('enter the how many no of players u want ot add:'))
        new=[(random.randint(1,5))*100 for i in range(n)]
        l.extend(new)
        display(l,'Add Multiple Players')
    elif ch==3:
        sc=int(input('Enter the score of the single player:'))
        l.append(sc)
        display(l,'Add a Single Player')
    elif ch==4:
        display(l,'Select the index to remove the player')
        index=int(input())
        l.pop(index)
        display(l,'Remove a Player')
    elif ch==5:
        f=int(input(' find the best player in the leaderboard'))
        l.find(f)
        display(l,'Find a Player')
    elif ch==6:
        s=int(input('find the first player'))
        l.sort(s)
        display(l,'Sort the Leaderboard:-(Highest to Lowest)')
    elif ch==7:
        s=int(input('find the last  player'))
        l.sort(s)
        display(l,'Sort the Leaderboard:-(Lowest to Highest)')
    elif ch==8:
        display(l,'Check the Leaderboard ')
    elif ch==9:
        n==int(input('enter the tie break players'))
        display(l,'Tie Break')
    elif ch==10:
        n=int(input('who are in the top '))
        display(l,'Top Players')
    else:
        print('invalid option:')