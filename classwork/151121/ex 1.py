max=int(input())
row=0
column=0
print('', end='\t')
for column in range(max+1):
    print(column, end="\t")
print()
for row in range(max+1):
    print(row,end='\t')
    for column in range(max+1):
        print(row*column, end='\t')
    print('')

# Evaluation: OK