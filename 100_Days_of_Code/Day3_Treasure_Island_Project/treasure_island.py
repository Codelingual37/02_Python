print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print('''You walk along the path and find yourself at a crossroad. The one to the right 
leads to a small, peaceful-looking shack, and the one to the left leads to a dark 
forest.''')
path = input("Which path do you want to take (left or right)? ")
if path != "left":
    if path == "right":
        print('''
                   ____,'`-, 
      _,--'   ,/::.; 
   ,-'       ,/::,' `---.___        ___,_ 
   |       ,:';:/        ;'"`;"`--./ ,-^.;--. 
   |:     ,:';,'         '         `.   ;`   `-. 
    \:.,:::/;/ -:.                   `  | `     `-. 
     \:::,'//__.;  ,;  ,  ,  :.`-.   :. |  ;       :. 
      \,',';/O)^. :'  ;  :   '__` `  :::`.       .:' ) 
      |,'  |\__,: ;      ;  '/O)`.   :::`;       ' ,' 
           |`--''            \__,' , ::::(       ,' 
           `    ,            `--' ,: :::,'\   ,-' 
            | ,;         ,    ,::'  ,:::   |,' 
            |,:        .(          ,:::|   ` 
            ::'_   _   ::         ,::/:| 
           ,',' `-' \   `.      ,:::/,:| 
          | : _  _   |   '     ,::,' ::: 
          | \ O`'O  ,',   ,    :,'   ;:: 
           \ `-'`--',:' ,' , ,,'      :: 
            ``:.:.__   ',-','        ::' 
    -hrr-      `--.__, ,::.         ::' 
                   |:  ::::.       ::' 
                   |:  ::::::    ,::' 
        ''')
        print('''You enter the shack, and upon entering, accidentally hit a puppy,
injuring the poor, defenseless doggo. Too bad for you; the owner, none other than
John Wick, sees this happen. John doesn't forgive and doesn't forget. (Did you
know he ended a dude with a pencil?!) His disappointed face is the last thing
you see before he gives you a one-way ticket to the next life. And you deserve it,
the poor pupper. GAME OVER.''')
    else:
        print("Did I stutter? I said right or left, fool. GAME OVER.")
else:
    print('''You walk through the dark forest. You see some plants and animals. You 
make sure to contain yourself not to eat the shrooms you see along the way. Don't
lick any frogs. This is a game for a coding project; keep it classy. Eventually, you
come to a large lake.''')
    action = input("Do you swim or do you chill and see what magically happens next ('swim' or 'wait')? ")
    if action != "wait":
        if action == "swim":
            print('''
            ,---,
  _    _,-'    `--,
 ( `-,'            `\\
  \           ,    o \\
  /   ,       ;       \\
 (_,-' \       `, _   ""/
     pb `-,___ =='__,-'
              ````
            ''')
            print('''Some extremely aggressive piranhas attack and nom you to death. It's possible.
It's happened before, no need to google it. Source: just trust me, bro. I guess your years
of taking those swimming lessons amounted to nothing in the end. GAME OVER.''')
        else:
            print("Do I need to remind you of your position here? It's 'swim' or 'wait'. GAME OVER.")
    else:
        print('''You hear a strange sound and turn around to see that three magical doors 
have appeared behind you, one red, one yellow, and one blue. (Are you sure you didn't
touch those shrooms?) Anyway, after you finish gawking and questioning reality you
come to the obvious conclusion that you have to make a choice.''')
        door = input('''Do you choose the red pill... I mean, door... the blue door, or the yellow door?
Again, 'red', 'blue', or 'yellow'? What's it going to be, Neo? ''')
        if door != "yellow":
            if door == "red":
                print('''
                /)_(\
                                                   ______( 0 0 )______
                                                  /_/_/_/\` ' `/\_\_\_\
                                                          )'_'(
                                                     ____.""_"".____
                                               /    |___|___|___|___|
                                              /       |___|___|___|
                     Abandon hope, ye who enter         |-      |
                              here                      |       |
                                                       _|_______|_
                            ___                       |___|___|___|
                           /   \                        |'   | ||
                           )'__/                        |       |
                           \(\\                         |       |
                             _\\__                      |       |
                            /,_ \--\                    |     - |
                       ____// \ |   \                   |       |
                      /,-' `  _)/   |\_                 |       |
                      ``     ,o_:)  ```                 |       |
                 .          /    \        .             |       |
                           /      \                     | |     |
              .    (      c        c     )    .         |       |
               (    )      \      /     (    )          |       |
              ( )  '        |     |      '  ( )        _|_______|_
              _#, .    ...,:o    o:,..    . ,#_ ,, ,,,|___b'ger___|,,,
                ''')
                print('''The gates of hell open up to greet you. It's diabolically hot. Hotter than
a thousand suns! Hotter than the most attractive person you've never been able
to date because they were too good for you! You are burned to death... only, I
guess you're in hell now, so it's like did you even really "die?" Anyway, you're there
for eternity. How embarrassing for you. GAME OVER.''')
            elif door == "blue":
                print('''
                ,-
                                       ,'::|
                                      /::::|
                                    ,'::::o\                                      _..
                 ____........-------,..::?88b                                  ,-' /
         _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
        <. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
         `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
             """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
                 ""--.__     P(       \               ` ``:`:``:::: .   .;'
                        "\""--.:-.     `.                             .:/
                          \. /    `-._   `.""-----.,-..::(--"".\""`.  `:\
                           `P         `-._ \          `-:\          `. `:\
                                           ""            "            `-._)  -Seal
                ''')
                print('''Remember how you waited not to swim across that river? Well, what good
that did you. You fall into an ocean of sharks, and not the cool kind. These
sharks are hungry, and they're a-comin. You swim furiously, desperately, glad
that you paid for those swimming lessons. Only guess what? You can't swim like
a shark. Fail. GAME OVER.''')
            else:
                print('''Sometimes I wonder what your IQ is. Do you know your colors? 'red', 'blue',
or 'yellow'. GAME OVER.''')
        else:
            print('''I can't believe it. You... you made it. Congratulations. You got the treasure!
But maybe the real treasure was the shrooms we got along the way.''')
