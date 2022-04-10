log_file = open("um-server-01.txt")
#this line opens the file "um-server-01.txt" and stores in it the variable "log_file"


def sales_reports(log_file):
#this calles the function "sales_reports"
    for line in log_file:
#classic for-loop in python syntax. For x in y. In this scenario, "line", or "x" is each line of the "um-server-01.txt"
        line = line.rstrip()
#each iteration that passes, ech line will be stripped of any whitespace or trailing characters.
        day = line[0:3]
#Simply defines a new variable, "day" to be equal the beginning 0'th place in each line to ending at the 3rd charcter space.
        if day == "Tue":
#if statement, executes if the variable "day" equals "Tue".
            print(line)
#prints out to the console the entire line of text, as created from the log_file.

sales_reports(log_file)

#calls the function "sales_reports" and ties it to the variable (storing the txt file) "log_file"
log_file.close()
log_file = open("um-server-01.txt")

def melon_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        melon_count = line[16:18]
        melon_count = melon_count.rstrip()
        melon_count = int(melon_count)
        if melon_count > 10:
            print(line)

melon_reports(log_file)
