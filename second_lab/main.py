from trainNeuro import trainNeuro
from predict import predict
from functions import *
from operations import *

print("----------MENU----------")
print("1. Training neural network\n2. Predict")
action = input("Choose your action: ")

if (action == '1'):
    trainNeuro()
elif (action == '2'):
    predict()