import os

while True:
    print(
        """
        -----------------------------------------------------
        Docker Menu Based Command 
        -----------------------------------------------------
        1. Launch new container
        2. Stop the container
        3. Remove the container
        4. Start the container
        5. Show Docker images
        6. Show all containers
        7. Exit
        """
    )

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name of container: ")
        image = input("Enter the name of image: ")
        os.system(f"docker run -dit --name {name} {image}")

    elif choice == "2":
        name = input("Enter name of container: ")
        os.system(f"docker stop {name}")

    elif choice == "3":
        name = input("Enter name of container: ")
        os.system(f"docker rm -f {name}")

    elif choice == "4":
        name = input("Enter name of container: ")
        os.system(f"docker start {name}")

    elif choice == "5":
        os.system("docker images")

    elif choice == "6":
        os.system("docker ps -a")
    elif choice == "7":
	os.system("

    elif choice == "8":
        print("Exiting Docker menu...")
        break

    else:
        print("Please enter a valid option (1-7).")
