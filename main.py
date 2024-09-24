#Kennon Sauter, U2 L1, Mutiplcation Table, 9/24/24



# ONE LINE - NO MORE, NO LESS
table = [num*i for num in range(1,11) for i in range(1,11) ]




########### NO TOUCHY ###########
for i, num in enumerate(table):
    if i % 10 == 0:
        print()
    
    print(num, end="\t")
print()
#################################
