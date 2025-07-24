import os
print(
    """
    -----------------------------------------------------
    This is Menu Based Project - Run any Command of Linux
    -----------------------------------------------------
    1.Date Command
    2.Cal Command
    3.IfConfig
    4.ls
    5.uptime-Tells how long the system has been          	     running
    6.uname -a ->Shows system information
    	 
    """
)
choice = input ("Enter Your Choice ")
if choice == "1":
    user= input("Enter UserName: ")
    ip =input("Enter Your Remote Ip: ")
    os.system(f"ssh {user}@{ip} date")

elif choice == "2":
    user= input("Enter UserName: ")
    ip =input("Enter Your Remote Ip: ")
    os.system(f"ssh {user}@{ip} cal ")
elif choice == "3":
    user= input("Enter UserName: ")
    ip =input("Enter Your Remote Ip: ")
    os.system(f"ssh {user}@{ip} ifconfig ")
elif choice == "4":
    user= input("Enter UserName: ")
    ip =input("Enter Your Remote Ip: ")
    os.system(f"ssh {user}@{ip} ls ")
elif choice == "5":
    user= input("Enter UserName: ")
    ip =input("Enter Your Remote Ip: ")
    os.system(f"ssh {user}@{ip} uptime ")
elif choice == "6":
    user= input("Enter UserName: ")
    ip =input("Enter Your Remote Ip: ")
    os.system(f"ssh {user}@{ip} uname -a ")
elif choice == "7":
    user= input("Enter UserName: ")
    ip =input("Enter Your Remote Ip: ")
    os.system(f"ssh {user}@{ip} ls ")
elif choice == "8":
    user= input("Enter UserName: ")
    ip =input("Enter Your Remote Ip: ")
    os.system(f"ssh {user}@{ip} ls ")
elif choice == "9":
    user= input("Enter UserName: ")
    ip =input("Enter Your Remote Ip: ")
    os.system(f"ssh {user}@{ip} ls ")
elif choice == "9":
    user= input("Enter UserName: ")
    ip =input("Enter Your Remote Ip: ")
    os.system(f"ssh {user}@{ip} ls ")
elif choice == "10":
    user= input("Enter UserName: ")
    ip =input("Enter Your Remote Ip: ")
    os.system(f"ssh {user}@{ip} ls ")
elif choice == "11":
    user= input("Enter UserName: ")
    ip =input("Enter Your Remote Ip: ")
    os.system(f"ssh {user}@{ip} ls ")
    

