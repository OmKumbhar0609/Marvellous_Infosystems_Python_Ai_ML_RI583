import psutil
import sys
import os
import time

# ----------------------------------------------------------
# Function Name : CreateLog
# Description   : Creates log file of running processes
# ----------------------------------------------------------

def CreateLog(FolderName):

    print("CreateLog Function Started")

    Border = "-" * 65

    Ret = os.path.exists(FolderName)

    if(Ret == True):

        Ret = os.path.isdir(FolderName)

        if(Ret == False):
            print("Unable to proceed as given name is not a directory")
            return

    else:

        os.mkdir(FolderName)
        print("Directory created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)

    fobj = open(FileName, "w")

    print("Log file created successfully with name :",FileName)

    fobj.write(Border + "\n")
    fobj.write("        Marvellous Process Information System\n")
    fobj.write(Border + "\n")
    fobj.write("Log Created At : " + timestamp + "\n")
    fobj.write(Border + "\n\n")

    fobj.write("{:<10}{:<35}{:<30}\n".format("PID", "Process Name", "Username"))
    fobj.write(Border + "\n")

    for proc in psutil.process_iter(['pid', 'name', 'username']):

        try:

            fobj.write("{:<10}{:<35}{:<30}\n".format(
                proc.info['pid'],
                str(proc.info['name']),
                str(proc.info['username'])
            ))

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    fobj.write("\n")
    fobj.write(Border + "\n")
    fobj.write("End Of Log File\n")
    fobj.write(Border + "\n")

    fobj.close()

    print("Log file saved successfully.")

def main():

    Border = "-" * 65

    print(Border)
    print("------------- Marvellous Process Information System -------------")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This application creates log file of running processes.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Usage : python ProcInfoLog.py DirectoryName")

        else:

            CreateLog(sys.argv[1])

    else:

        print("Invalid number of arguments")
        print("Please use --h or --u for help")

    print(Border)
    print("Thank you for using Marvellous Automation")
    print(Border)

if __name__ == "__main__":
    main()