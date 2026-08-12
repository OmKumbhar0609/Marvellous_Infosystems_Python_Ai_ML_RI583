# Duplicate File Removal Automation

## Project Description
This Python automation script periodically scans a specified directory recursively, detects duplicate files using MD5 checksum algorithm on actual file content, keeps the original file while deleting remaining duplicate copies, creates a detailed timestamped log file, and sends the operation log and summary statistics to a target email address.

## Features
* Recursive directory scanning
* Checksum-based duplicate detection (MD5 hash)
* Automatic duplicate file deletion (preserves the first instance)
* Timestamp-based log generation inside Marvellous/ directory
* Periodic execution based on user-defined interval
* Automated email notification with log attachment
* Comprehensive command-line validations and exception handling
* Modular software design

## Requirements
* *Python Version:* Python 3.8+
* *Required Standard Libraries:* sys, os, re, time, hashlib, datetime, smtplib, email
* *Network Requirement:* Active Internet connection for email delivery
* *SMTP Setup:* Gmail App Password or configured SMTP credentials set in environment variables (SENDER_EMAIL and SENDER_PASSWORD).

## Project Structure
* DuplicateFileRemoval.py: Main CLI execution entry point and periodic scheduler.
* duplicate_cleaner.py: Core logic for file system traversal and checksum creation.
* log_manager.py: Utilities for directory creation and timestamped file logging.
* email_sender.py: Handles SMTP client connection and sending emails with attachments.

## Command-Line Options
* <AbsoluteDirectoryPath>: Absolute path of target folder to scan.
* <TimeIntervalInMinutes>: Numeric execution interval (in minutes).
* <ReceiverEmailAddress>: Destination email address for operation summary and log file.

## Execution Command
*  python duplicate_cleaner.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
