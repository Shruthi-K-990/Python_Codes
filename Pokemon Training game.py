powers= [2,6,8,1]
mini,maxi=0,0

for power in powers:
    if mini == 0 and maxi== 0:
        mini,maxi=powers[0],powers[1]
        print(mini,maxi)
    else:
        mini = min(mini,power)
        maxi = max(maxi,power)
        print(mini,maxi)
