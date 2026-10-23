
#Gather information on all available files.
files = ["security.log", "users.csv", "access.log", "report.txt"]
# This line of code gathers up all files that end in .log
log_files = [file for file in files if file.endswith(".log")]
# This line prints all the files that end in .log
print("These are all of the log files:", log_files)