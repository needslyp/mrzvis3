from compress import compress
from decompress import decompress
from funcs import normalWeightMatrix
from training import training


print(bool('false'))

print("----------MENU----------")
print("1. Training neural network\n2. Compress image\n3. Decompress image\n")
action = input("Choose your action: ")

if (action == '1'):
    training()
elif (action == '2'):
    compress()
elif (action == '3'):
    decompress()