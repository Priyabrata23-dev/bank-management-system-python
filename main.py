from pathlib import Path
import json
import random
import string

class Bank:
    database = "data.json"
    data = []

    try:
        if Path(database).exists:
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("Path not found")
    except Exception as err:
        print(f"Exception is raise {err}")

    

    @classmethod
    def __accountNoGenerator(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        digits = random.choices(string.digits, k=3)
        spchr = random.choices("!@#$%^&*", k=1)
        id = alpha + digits + spchr
        random.shuffle(id)
        return "".join(id)

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as f:
            f.write(json.dumps(cls.data))





    def createAccount(self):
        info = {
            "Name" : input("Enter your name: "),
            "Age" : int(input("Enter your age: ")),
            "Email-ID" : input("Enter your email-id: "),
            "Pin" : int(input("Enter your pin: ")),
            "Account-No" : Bank.__accountNoGenerator(),
            "Balance" : 0
        }
        if info["Age"] < 18 or len(str(info["Pin"])) != 4:
            print("Sorry your account cannot be created.")
        else:
            print("Account successfully created.")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note your account number.")
            Bank.data.append(info)
            Bank.__update()


    def depositMoney(self):
        acn = input("\nEnter your account number: ")
        pin = int(input("Enter the pin: "))

        userdata = [i for i in Bank.data if i["Account-No"]==acn and i["Pin"]==pin]

        if not userdata:
            print("No account found!!")
        else:
            amt = float(input("\nEnter the amount to be deposited: "))
            if amt>10000 or amt<0:
                print("\nThe given amount cannot be deposited")
            else:
                userdata[0]["Balance"] += amt
                Bank.__update()
                print("\nAmount deposited successfully")


    def withdrawMoney(self):
        acn = input("\nEnter your account number: ")
        pin = int(input("Enter the pin: "))

        userdata = [i for i in Bank.data if i["Account-No"]==acn and i["Pin"]==pin]

        if userdata==False:
            print("No account found!!")
        else:
            amt = float(input("\nEnter the amount to be withdrawn: "))
            if amt>userdata[0]["Balance"]:
                print("\nInsufficient balance!!")
            elif amt<0:
                print("\nInvalid Amount")
            else:
                userdata[0]["Balance"] -= amt
                Bank.__update()
                print("\nAmount withdrawn successfully")

    
    def updateAccountDetails(self):
        acn = input("\nEnter your account number: ")
        pin = int(input("Enter the pin: "))

        userdata = [i for i in Bank.data if i["Account-No"]==acn and i["Pin"]==pin]

        if userdata==False:
            print("No account found!!")
        else:
            print("\nPress 1 to update the name")
            print("Press 2 to update the email-id")
            print("Press 3 to update both")
            ch = int(input("\nEnter your choice: "))
            if ch==1:
                nn = input("\nEnter the new name: ")
                userdata[0]["Name"] = nn
                Bank.__update()
                print("Account Updated Successfully.")
            elif ch==2:
                ne = input("\nEnter the new email-id: ")
                userdata[0]["Email-ID"] = ne
                Bank.__update()
                print("Account Updated Successfully.")
            elif ch==3:
                nn = input("\nEnter the new name: ")
                userdata[0]["Name"] = nn
                ne = input("Enter the new email-id: ")
                userdata[0]["Email-ID"] = ne
                Bank.__update()
                print("Account Updated Successfully.")
            else:
                print("\nInvalid Choice")
        
    def displayAccountDetails(self):
        acn = input("\nEnter your account number: ")
        pin = int(input("Enter the pin: "))

        userdata = [i for i in Bank.data if i["Account-No"]==acn and i["Pin"]==pin]

        if userdata==False:
            print("No account found!!")
        else:
            print("\nAccount Details:")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def deleteAccount(self):
        acn = input("\nEnter your account number: ")
        pin = int(input("Enter the pin: "))

        userdata = [i for i in Bank.data if i["Account-No"]==acn and i["Pin"]==pin]

        if userdata==False:
            print("No account found!!")
        else:
            Bank.data.remove(userdata[0])
            Bank.__update()
            print("\nAccount deleted succesfully.")


user = Bank()
print("Press 1 for creating a new bank account")
print("Press 2 for depositing money")
print("Press 3 for withdrawing money")
print("Press 4 for updating account details")
print("Press 5 for displaying account details")
print("Press 6 for deleting account")
ch = int(input("Enter your choice: "))
if ch==1:
    user.createAccount()
elif ch==2:
    user.depositMoney()
elif ch==3:
    user.withdrawMoney()
elif ch==4:
    user.updateAccountDetails()
elif ch==5:
    user.displayAccountDetails()
elif ch==6:
    user.deleteAccount()
else:
    print("\nInvalid Choice!!")
