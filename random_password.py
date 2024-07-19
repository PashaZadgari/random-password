import random as r

characters = '''QqWwEeRrTtYyUuIiOo!@#&*_PpAaSsdDFf
GgHhJjKkLlZz1234567890XxCcVvBbNnmM'''

password  =''
letters = 0

while letters < 14:
    password += characters[r.randrange(0, len(characters)-1)]
    letters += 1

print(password)