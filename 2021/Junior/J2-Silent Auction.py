bidnum = int(input(""))
bid_max = 0
by_whom = ''

for i in range(0, bidnum):
    bidname = str(input(""))
    bidmoney = int(input(""))
    if bidmoney > bid_max:
        bid_max = bidmoney
        by_whom = bidname

print(by_whom)
