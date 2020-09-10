Array = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

flatArray = []

def flatArr(origArr):
    for i in origArr:
        if type(i) == list:
            flatArr(i)
        else:
            flatArray.append(i)

flatArr(Array)

for i in flatArray:
          print (i)