from compress import compress
from decompress import decompress
from trainNeuro import trainNeuro

print("----------MENU----------")
print("1. Training neural network\n2. Compress image\n3. Decompress image\n")
action = input("Choose your action: ")

if (action == '1'):
    trainNeuro()
elif (action == '2'):
    compress()
elif (action == '3'):
    decompress()