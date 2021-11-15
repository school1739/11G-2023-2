a=int(input())
b=int(input())
c=int(input())
if a==b and b==c:
    print('Равносторонний')
elif a==b:
    print('Равнобедренный')
elif a==c:
    print('Равнобедренный')
elif b==c:
    print('Равнобедренный')
else:
    print('Разносторонний')

# Evaluation: OK. В следующий раз лучше бы объединять похожие условия с помощью логических операторов типа OR.