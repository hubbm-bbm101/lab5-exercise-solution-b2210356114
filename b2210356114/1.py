n=int(input("Write an N: "))
sumo = 0
sume = 0
nume = 0
for i in range(1,n+1):
    if i%2 == 1:
        sumo = sumo + i 
    else:
        sume = sume + i

for a in range(1,n+1):
    if a%2 == 0:
        nume= nume + 1
    else:
        continue
avge = sume / nume



print ("Sum of odd number: {a}".format(a={sumo})) 
print ("Average of even number: {a}".format(a={avge}))     