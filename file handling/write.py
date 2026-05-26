big=['hello world' for i in range (1000)]
with open ('big.txt','w') as f:
    f.writelines(big) 