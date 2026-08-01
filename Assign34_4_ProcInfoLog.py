import psutil
import sys
import os
import schedule
import time
import SimpleGmailMailSenderX

# Gmail Credentials
sender_email = "pc.omkumbhar@gmail.com"
app_password = "kgrloceiodszlaaj"

# ----------------------------------------------------------
# Function Name : ProcInfo
# Description   : Creates log file and sends mail
# ----------------------------------------------------------

def ProcInfo(FolderName, ReceiverName):

    Border = "-" * 65

    Ret = os.path.exists(FolderName)

    if(Ret == True):

        Ret = os.path.isdir(FolderName)

        if(Ret == False):

            print("Unable to proceed as directory exists but it is not a folder")
            return

    else:

        os.mkdir(FolderName)
        print("Directory created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(
        FolderName,
        "Marvellous_%s.log" % timestamp
    )

    fobj = open(FileName,"w")

    print("Log file created successfully :",FileName)

    fobj.write(Border+"\n")
    fobj.write("        Marvellous Process Information System\n")
    fobj.write(Border+"\n")
    fobj.write("Log Created At : "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("{:<10}{:<35}{:<30}\n".format(
        "PID",
        "Process Name",
        "Username"
    ))

    fobj.write(Border+"\n")

    for proc in psutil.process_iter(['pid','name','username']):

        try:

            pid = proc.info['pid']

            pname = proc.info['name']
            if pname is None:
                pname = "N/A"

            username = proc.info['username']
            if username is None:
                username = "N/A"

            fobj.write("{:<10}{:<35}{:<30}\n".format(
                pid,
                pname,
                username
            ))

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):

            pass

    fobj.write("\n")
    fobj.write(Border+"\n")
    fobj.write("End Of Log File\n")
    fobj.write(Border+"\n")

    fobj.close()

    print("Log file generated successfully")

    subject = "Running Process Log"

    body = """Jay Ganesh,

Please find the attached log file.

This log contains information about all running processes.

Regards,
Om Kumbhar
"""

    try:

        SimpleGmailMailSenderX.send_mail(
            sender_email,
            app_password,
            ReceiverName,
            subject,
            body,
            FileName
        )

        print("Mail Sent Successfully")

    except Exception as e:

        print("Mail Sending Failed")
        print(e)

# ----------------------------------------------------------
# Function Name : main
# Description   : Entry Point
# ----------------------------------------------------------

def main():

    Border = "-" * 65

    print(Border)
    print("---- Marvellous Process Information System ----")
    print(Border)

    # Help and Usage

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This automation script is used to create")
            print("log file of running processes and")
            print("send the log file through Gmail.")

            return

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Usage :")
            print("python ProcInfo.py TimeInterval FolderName ReceiverEmail")
            print("")
            print("Example :")
            print("python ProcInfo.py 5 Demo abc@gmail.com")

            return

        else:

            print("Invalid Argument")
            print("Use --h or --u")

            return

    # Actual Project

    elif(len(sys.argv) == 4):

        try:

            Interval = int(sys.argv[1])

        except ValueError:

            print("Time Interval should be Integer")
            return

        FolderName = sys.argv[2]

        ReceiverName = sys.argv[3]

        print("Scheduler Started Successfully")
        print("Press Ctrl + C to stop automation")

        schedule.every(Interval).minutes.do(
            ProcInfo,
            FolderName,
            ReceiverName
        )

        # Execute once immediately
        ProcInfo(FolderName, ReceiverName)

        while True:

            schedule.run_pending()

            time.sleep(1)

    else:

        print("Invalid Number of Arguments")
        print("Use --h or --u")

    print(Border)
    print("Thank You For Using Marvellous Automation")
    print(Border)


# ----------------------------------------------------------
# Entry Point
# ----------------------------------------------------------

if __name__ == "__main__":

    main()

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