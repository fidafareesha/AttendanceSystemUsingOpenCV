
import sqlite3


print(''' Enter Your Choice:
              1- saving dataset
              2- training the model
              3- face recognition
              4- exit''')
choice=0
while(choice<1 or choice>4):
    choice = int(input("Enter Here : "))
if(choice == 1):
    import face_dataset
elif choice == 2:
    import training 
elif choice == 3:
    import face_recognition

elif choice == 4:
    print("Exiting the program")
    exit()



