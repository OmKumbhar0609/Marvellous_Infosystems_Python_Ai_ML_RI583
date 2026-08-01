import psutil
import sys

# ----------------------------------------------------------
# Function Name : SearchProcess
# Description   : Search process by name
# ----------------------------------------------------------

def SearchProcess(ProcessName):

    Border = "-" * 65

    Found = False

    print(Border)
    print("{:<10}{:<35}{:<30}".format("PID", "Process Name", "Username"))
    print(Border)

    for proc in psutil.process_iter(['pid', 'name', 'username']):

        try:

            if(proc.info['name'] != None):

                if(proc.info['name'].lower() == ProcessName.lower()):

                    print("{:<10}{:<35}{:<30}".format(
                        proc.info['pid'],
                        proc.info['name'],
                        str(proc.info['username'])
                    ))

                    Found = True

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    if(Found == False):
        print("\nProcess not found.")

def main():

    Border = "-" * 65

    print(Border)
    print("------------- Marvellous Process Information System -------------")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This application searches running process by name.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Usage : python ProcInfo.py ProcessName")

        else:

            SearchProcess(sys.argv[1])

    else:

        print("Invalid number of arguments")

    print(Border)
    print("Thank you for using Marvellous Automation")
    print(Border)

if __name__ == "__main__":
    main()