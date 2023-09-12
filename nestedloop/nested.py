#nestedloop= the inner loop will finish all of trhe iterations 
#before finishing one iterations of the outer loop
rows=int(input("How many rows:"))
col=int(input("how many col:"))
symbol=input("enter symbol to use")
for i in range(rows):#outer loop
    for j in range(col):#innerloop
      print(symbol, end='')
      print()