import os
print(
    """
    -----------------------------------------------------------------------
    This is the Menu Based Project - Run any Command of Linux on Windowns
    -----------------------------------------------------------------------
    1.	For Date
    2.	For Calendar
    3.	For Ip Address
    4.	ls - of folders and files
    5.	rmdir -help -> tells about the what is the use of the rmdir 
    6.	touch - with this command in linux make the files in the linux terminal
    7.	cat - with the cat you can read the text file which is you made with the touch command
    8.	vim - with this command you can accesses the text files and you can edit on that files
    9.	python - with this command a python terminal is launched
    10. echo - this command is used to print something on the terminal 
    11. pwd - this command shows the present working directory
    12. history - this command shows all the command that you entered above in the terminal
    13. head - this command shows only the text lines you want to see (e.g - head -n 2 file.txt)
    14. grep - this command is used for searching something your text file (e.g - grep hello file.txt)
    15.
    """)

choice = input("Enter Your Choice :")
if choice =="1":
    user=input("Enter UserName : " )
    ip=input("Enter Your Remote IP: ")
    os.system(f"ssh {user}@{ip} date")
              
elif choice == "2":
    user=input("Enter UserName : ")
    ip = input ("Enter your Remote Ip : ")
    os.system(f"ssh {user}@{ip} cal")
elif choice =="3":

    user=input("Enter UserName : ")
    ip = input("Enter your Remote Ip :")
    os.system(f"ssh {user}@{ip} ifconfig")
elif choice =="4":
    user=input("Enter UserName : ")
    ip = input ("Enter Remote Ip : ")
    os.system(f"ssh {user}@{ip} ls ")
elif choice =="5":
    user=input("Enter UserName : ")
    ip = input("Enter Your Remote Ip : ")
    os.system(f"ssh {user}@{ip} rmdir --help")
elif choice == "6":
    user = input("Enter UserName : ")
    ip = input("Enter Your Remote Ip : ")
    os.system(f"ssh {user}@{ip} touch textfile2.txt")

elif choice == "7":
    user = input("Enter UserName : ")
    ip = input("Enter Your Remote Ip Address : ")
    os.system(f"ssh {user}@{ip} cat textfile.txt")

elif choice == "8":
    user = input("Enter UserName : ")
    ip = input("Enter Your Remote Ip : ")
    os.system(f"ssh {user}@{ip} vim textfile.txt")
elif choice == "9":
    user = input("Enter UserName : ")
    ip = input("Enter Your Remote Ip : ")
    os.system(f"ssh {user}@{ip} python")
    