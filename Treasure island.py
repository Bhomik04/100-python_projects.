print('''

            (                 ,&&&.
             )                .,.&&
            (  (              \=__/
                )             ,'-'.
          (    (  ,,      _.__|/ /|
           ) /\ -((------((_|___/ |
         (  // | (`'      ((  `'--|
       _ -.;_/ \\--._      \\ \-._/.
      (_;-// | \ \-'.\    <_,\_\`--'| 
      ( `.__ _  ___,')      <_,-'__,'
 jrei  `'(_ )_)(_)_)'






    .(
   /%/\
  (%(%))
 .-'..`-.
 `-'.'`-'dd ''')
print('''Welcome to Treasure Island.
      In a time long past, when the seas were wild and untamed, there was an island shrouded in mystery and legend. This island, known to daring sailors as Treasure Island, was said to hold unimaginable riches hidden deep within its dense jungles and treacherous caves.

Generations ago, the notorious pirate Captain Blackbeard plundered the high seas, amassing a fortune in gold, jewels, and priceless artifacts. Fearing betrayal from his crew, he hid his treasure on this remote island, leaving behind a series of cryptic clues and cunning traps to safeguard it. With his last breath, Blackbeard swore that only the bravest and most cunning adventurer would ever lay hands on his hidden bounty.

Now, the call of Treasure Island has reached your ears. As a bold and fearless explorer, you have decided to embark on this perilous journey. Armed with a tattered map and a heart full of courage, you set sail, ready to face whatever dangers and challenges lie ahead. The island is rumored to be full of secrets, from whispering forests to treacherous swamps, each step fraught with danger and mystery.

Will you outwit the traps set by Blackbeard, solve the riddles that guard the treasure, and claim the riches that have eluded so many before you? Your adventure begins now. Steady your nerves, sharpen your wits, and prepare for the adventure of a lifetime.

Welcome to Treasure Island. The treasure awaits—if you dare to find it.
Your mission is to find the treasure.''')


choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
