for i in range(1,101):
    if i%7==0 or (i-7)%10==0:
        continue
    elif i-70>=1 and i-70<10:
        continue
    else:
        print(i)
        print('
')

