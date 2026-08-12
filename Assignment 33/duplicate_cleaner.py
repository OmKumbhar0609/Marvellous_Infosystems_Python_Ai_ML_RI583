# Duplicate File Removal Automation Using python

import os
import sys
import hashlib

from datetime import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import re
import time

##############################################
# Scanning directories, 
# Calculating checksum,
# Identifying/ deleteing duplicate files
##############################################
def log_func(message):
    print(message)

def CalculateChecksum(FileName):
    try:
        fobj = open(FileName,"rb")
        hobj = hashlib.md5()
        Buffer = fobj.read(1024)
        while(len(Buffer) > 0):
            hobj.update(Buffer)
            Buffer = fobj.read(1024)
        fobj.close()
        return hobj.hexdigest()
    except Exception as e:
        log_func(f"Error reading file {FileName}: {str(e)}")
        return None

def FindDuplicate(DirectoryName):
    Ret = False
    Ret = os.path.exists(DirectoryName)
    
    if Ret == False:
        print("Path is invalid")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("It is not a Directory")
        return
    
    deleted_file_info = {}
    total_scanned = 0
    duplicate_found = 0
    duplicate_deleted = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.abspath(os.path.join(FolderName, fname))

            # File validation before checksum calculation
            if not os.path.exists(fname) or not os.path.isfile(fname):
                continue

            if not os.access(fname, os.R_OK):
                print(f"Error: Permission denied (Read) - {fname}")
                continue

            Checksum = CalculateChecksum(fname)
            if Checksum is None:
                log_func(F"Error: Could not read file content for checksum - {fname}")
                continue

            total_scanned = total_scanned + 1

            if Checksum in deleted_file_info:   # if balckShirt in Kapat"
                duplicate_found = duplicate_found + 1
                # Attempt to delete duplicate file
                if os.access(fname, os.W_OK):
                    try:
                        os.remove(fname)
                        log_func(f"Deleted duplicate file: {fname}")
                        duplicate_deleted = duplicate_deleted + 1
                        deleted_file_info[Checksum].append(fname)
                    except Exception as e:
                        log_func(f"Error: Failed to delete file {fname}: {str(e)}")
                else:
                    log_func(f"Error: Permission denied (Delete) - {fname}")
            else:
                deleted_file_info[Checksum] = [fname]

    return { 
        "total_scanned" : total_scanned,
        "duplicate_found" : duplicate_found,
        "duplicate_deleted" : duplicate_deleted,
        "deleted_file_info": deleted_file_info
    }

#####################################################
# Handle directory creation and detialed file logging
#####################################################

def create_log_directory(dir_name="Marvellous"):
    # create directory if it's not exists.
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return dir_name

def generate_log_filepath(log_dir="Marvellous"):
    # Generate log file path formatted as DupliateRemovalLog_DD_MM_YYYY_HH_MM_SS.log
    now = datetime.now()
    filename = f"DupliateRemovalLog_{now.strftime('%d_%m_%Y_%H_%M_%S')}.log"
    return os.path.join(log_dir, filename)

class Logger:
    def __init__(self, log_filepath):
        self.log_filepath = log_filepath

    def write_line(self, message):
        # write operational messages to the log file instead of console.
        f = open(self.log_filepath, "a")
        f.write(message + "\n")

#####################################################
# Handles secure email creation and log attachment
#####################################################

# Default configuration - standard recommendation is using environment variables
sender_email = os.environ.get("Sender_email", "kumbharniki21.nk@gmail.com")
sender_password = os.environ.get("Sender_password", "rltgypdbqrkeyapx")

def send_npotification_email(receiver_email, stats, log_filepath):
    # send execution statistics and attaches the generated log file.
    if not sender_email or not sender_password:
        return False, "Sender credentials missing the environment variables."

    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Duplicate File Removal Operation Report"

        body = f"""Jay Ganesh,
The duplicate file removal operation has been completed successfully.
        
Operation Statistics:
        
Starting time of scanning: {stats['start_time']}
Completion time of scanning: {stats['end_time']}
Directory scanned: {stats['scanned_dir']}
Total number of files scanned: {stats['total_scanned']}
Total number of duplicate file found: {stats['duplicate_found']}
Total number of duplicate file deleted: {stats['duplicate_deleted']}

Please find the detailed log file attached to this email.

Regards,
Marvellous Automation system
"""
        msg.attach(MIMEText(body, 'plain'))

        # Attach log file
        if os.path.exists(log_filepath):
            attachement = open(log_filepath,"rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachement.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(log_filepath)}")
            msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email,sender_password)
        text = msg.as_string()
        server.sendmail(sender_email,receiver_email,text)
        server.quit()
        return True, "Email sent successfully."

        attachement.close()
    except Exception as e:
        return False, str(e)

def display_help():
    print("""
    Duplicate file Removal Automation
    This Script scans a directory, identifies duplicate files using checksum,
    delete duplicate files, create a log files, and sends the log file through email..
    
    Usage:
        python duplicate_cleaner.py <Directorypath> <IntervalMinutes> <ReceiverMails>
        
    Options:
        -h, --help   Show this help message and exit.
        -u, --usage  Show command usage information and exit.
        
    Example:
        python duplicate_cleaner.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
    """)

def display_usage():
    print("\nUsage:\npython duplicate_cleaner.py <AbosoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>\n")

def validate_email(email):
    # Validate email address format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email)

#####################################################
# Main Operation
#####################################################

def perform_operation(dir_path, receiver_email):
    log_dir = create_log_directory("Marvellous")
    log_file_path = generate_log_filepath(log_dir)
    logger = Logger(log_file_path)

    start_time_str = datetime.now().strftime('%d %B %Y, %I:%M:%S %p')

    # Log summary statistics
    logger.write_line("=" * 60)
    logger.write_line("DUPLICATE FILE REMOVAL AUTOMATION LOG")
    logger.write_line("=" * 60)
    logger.write_line(f"Starting time of directory scanning: {start_time_str}")
    logger.write_line(f"Directory scanned: {dir_path}\n")

    # Perform cleaning operation
    results = FindDuplicate(dir_path)
    if not results:
        return

    end_time_str = datetime.now().strftime('%d %B %Y, %I:%M:%S %p')

    # Log summary statistics
    logger.write_line("=" * 40)
    logger.write_line("DELETED DUPLICATE FILES: ")
    logger.write_line("=" * 40)
    deleted_info = results.get("deleted_file_info", {})
    duplicates = [files for checksum, files in deleted_info.items() if len(files) > 1]

    if duplicates:
        for files in duplicates:
            for file_path in files[1:]:
                logger.write_line(f"Path: {file_path}")
    else:
        logger.write_line("No duplicate files deleted")

    logger.write_line("\n" + "-" * 40)
    logger.write_line("OPEARTION SUMMARY")
    logger.write_line("-" * 40)
    logger.write_line(f"Total number of files scanned: {results['total_scanned']}")
    logger.write_line(f"Total number of dupliate files found: {results['duplicate_found']}")
    logger.write_line(f"Total number of dupliate files deleted: {results['duplicate_deleted']}")
    logger.write_line(f"Completion time of directory scanning: {end_time_str}")

    # Prepare stats for email body
    stats = {
        "start_time": start_time_str,
        "end_time": end_time_str,
        "scanned_dir": dir_path,
        "total_scanned": results["total_scanned"],
        "duplicate_found": results["duplicate_found"],
        "duplicate_deleted": results["duplicate_deleted"],
    }

    # Send Email Notification
    success, message = send_npotification_email(receiver_email, stats, log_file_path)
    logger.write_line(f"Email delivery status: {'Success' if success else 'Failed (' + message + ')'}")

def main():
    # Handle help/usage flag
    if len(sys.argv) == 2:
        if sys.argv[1] in ("-h", "--help"):
            display_help()
            sys.exit(0)
        elif sys.argv[1] in ("-u", "--usage"):
            display_usage()
            sys.exit(0)
        else:
            print("Invalid argument. Use -h or --help for instruction.")
            sys.exit(1)

    # Command line validation 
    if len(sys.argv) != 4:
        print("Invalid number of arguments. Please provide Directory Path, Interval in Minutes, and Receiver Email")
        display_usage()
        sys.exit(1)

    dir_path = sys.argv[1]
    interval_str = sys.argv[2]
    receiver_email = sys.argv[3]

    # Directory Validations
    if not os.path.isabs(dir_path):
        print("Error: Provided path must be an absolute path.")
        sys.exit(1)
    if not os.path.exists(dir_path):
        print("Error: Directory path does not exist.")
        sys.exit(1)
    if not os.path.isdir(dir_path):
        print("Error: Provided path is not directory.")
        sys.exit(1)
    if not os.access(dir_path, os.R_OK):
        print("Error: Permission denied to access the directory.")
        sys.exit(1)

    # Time-Interval Validation
    if not interval_str.isdigit() or int(interval_str) <= 0:
        print("Error: time interval must be a positive numeric value greater than zero")
        sys.exit(1)

    interval_minutes = int(interval_str)

    # Email Validation
    if not validate_email(receiver_email):
        print("Error: Invalid email format.")
        sys.exit(1)

    # Periodic Scheduling Loop
    try:
        while True:
            perform_operation(dir_path, receiver_email)
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
