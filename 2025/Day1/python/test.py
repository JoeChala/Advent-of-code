cur_dial = 50
value = 350
max_dial = 100

move = cur_dial - value
while move < 0:
    move += max_dial
cur_dial = move

print(cur_dial)