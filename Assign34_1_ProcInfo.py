import psutil
import sys

# ----------------------------------------------------------
# Function Name : DisplayProcesses
# Description   : Display all running processes
# ----------------------------------------------------------

def DisplayProcesses():

    Border = "-" * 65

    print(Border)
    print("{:<10}{:<35}{:<30}".format("PID", "Process Name", "Username"))
    print(Border)

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            print("{:<10}{:<35}{:<30}".format(
                proc.info['pid'],
                proc.info['name'],
                str(proc.info['username'])
            ))

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

def main():

    Border = "-" * 65

    print(Border)
    print("------------- Marvellous Process Information System -------------")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This application displays information of running processes.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Usage : python ProcInfo.py")

        else:

            print("Invalid option")

    elif(len(sys.argv) == 1):

        DisplayProcesses()

    else:

        print("Invalid number of arguments")

    print(Border)
    print("Thank you for using Marvellous Automation")
    print(Border)

if __name__ == "__main__":
    main()