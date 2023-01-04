import random

def guess_game():
  first_num = random.randint(0,20)
  sec_num = random.randint(20,50)
  third_num = random.randint(first_num, sec_num)

  try:
    guesses = int(input('რამდენი ცდის უფლება გსურთ? :'))
  except:
    print('შეიყვანეთ რიცხვი!')
    return
  i = 0

  while True:
   
    try:
      guess = int(input('შეიყვანეთ რიცხვი: '))
      if guess != third_num:
        print('შეყვანილი რიცხვი არასწორია')
        i+=1
        if i == guesses:
          print('თქვენ წააგეთ.') 
          break
        if input('გსურთ მინიშნება? (კი, არა):') == 'კი':
          if guess < third_num:
            print('თქვენი შეყვანილი რიცხვი ნაკლები იყო ჩაფიქრებულ რიცხვზე')
          else:
            print('თქვენი შეყვანილი რიცხვი მეტი იყო ჩაფიქრებულ რიცხვზე')
      elif guess == third_num:
        print(f'თქვენ გაიმარჯვეთ, {guess} სწორი რიცვია.') 
        break 
        

    except: print('რიცხვი სწორად შეიყანეთ')
  input('დააჭრეთ ენთერს დასასრულებლად')

guess_game()