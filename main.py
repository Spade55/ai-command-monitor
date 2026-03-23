from monitor import monitor_command

def main():
    print("AI Command Monitoring System Started")
    print("Type 'exit' to quit\n")

    while True:
        command = input("Enter command: ")

        if command.lower() == "exit":
            print("Exiting system...")
            break

        monitor_command(command)

if __name__ == "__main__":
    main()