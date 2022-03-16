log_file = open("um-server-01.txt") #opens a text file and assigning its contents to the log_file variable


def generate_sales_reports(log_file): #create a function that generates a sales report based on a log file
    for line in log_file: #iterates through each line of the file
        line = line.rstrip() #removes whitespace from the right
        day = line[0:3] #assigns a 3 char long string to the day variable
        if day == "Mon": #conditional that check if day matches "Tue"
            print(line) #prints an output of line


generate_sales_reports(log_file) #calls function with an argument
