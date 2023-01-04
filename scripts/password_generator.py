import random


def generate_password(pass_length):
  lowers = [chr(x) for x in range(97,123)]  
  capitals = [chr(x) for x in range(65,91)]
  numbers = [chr(x) for x in range(48,58)]
  symbols = ['!','@','#','$','%','^','&','*','+']

  password = ''
  for i in range(pass_length):
    rand_char = random.choice(random.choice([lowers,numbers,capitals,symbols]))
    password+=rand_char

  return password   



if __name__ == '__main__':
  print(generate_password(11))

  

