n_1, n_2, n_3 = int(input()), int(input()), int(input())
if n_1 == n_2 == n_3:
    print("Равносторонний")
elif n_1 == n_2 or n_2 == n_3 or n_1 == n_3:
    print("Равнобедренный")
else:
    print("равносторонний")
