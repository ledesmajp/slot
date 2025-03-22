import random

print("WELCOME TO THE SLOT\n🍒=   $5\n🍇=  $10\n🍉=  $15\n💯 = $100")
coins = int(input('How much cash do you want to play? $'))

def play(coins):
    while coins > 0:
      symbols = ['🍒','🍇', '🍉', '💯']
      symbols = random.choices(symbols, k=3)
      print(f'{symbols[0]} | {symbols[1]} | {symbols[2]} ')
      if symbols[0] == '🍒' and symbols[0] == symbols[1] == symbols[2]:
        print('You Win: $5 🎰🎰🎰🎰')
        coins += 5
      elif symbols[0] == '🍇' and symbols[0] == symbols[1] == symbols[2]:
          print('You win: $10 🎰🎰🎰🎰')
          coins += 10
      elif symbols[0] == '🍉' and symbols[0] == symbols[1] == symbols[2]:
          print('You win: $15 🎰🎰🎰🎰')
          coins += 15
      elif symbols [0] == '💯' and symbols[0] == symbols[1] == symbols[2]:
          print('JACK POT!!: $100 🎰🎰🎰🎰')
          coins += 100
      else:
          print('No win this time 🚫')

      coins -= 1
      print(f'You have ${coins}')
      
      if coins > 0:
        keep = input("Do you wanna keep playing? Y/N: ").strip().lower()
        if keep != 'y' and keep != 'n':
           while keep != 'y' and keep != 'n':
              keep = input("Type Y or N: ").strip().lower()

        if keep != 'y':
           print(f'Thanks for playing you got ${coins}')
           break
        
      if coins == 0:
         print('You lost all your money 💀💀💀')
         break
            

play(coins)
