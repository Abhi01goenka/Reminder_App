import time
import os
from plyer import notification

def add_notification(d):
    t=int(input("Enter seconds after which reminder should occur : "))
    notif=input("Enter reminder : ")
    message=input("Enter message : ")
    d[t]=[notif,message]

os.system("cls")
print("Reminder App")
time.sleep(0.5)
print("\n\nPress Y/y for adding a reminder\nPress N/n for exiting the app\n")

while True:
    choice=input("Enter your choice : ")
    if choice in "N/n":
        print("Exiting...")
        break
    d={}
    add_notification(d)
    time.sleep(0.5)
    print("Notification added..")
    print("\n")
if __name__=="__main__":
    while True:
        for key in sorted(d.keys()):
            notification.notify(
                title = d[key][0],
                message=d[key][1],
                timeout=10
            )
            time.sleep(key)

    