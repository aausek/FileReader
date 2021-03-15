# Import modules
import urllib.request
import smtplib, ssl

# Define function to read in user input and open url to read file contents
def UrlReader(N):
    # Desired page url
    url = 'https://www.cmgcheckin.com/login/exceptionlistupdate.txt'

    # Utilize urllib to open url assign it to variable f
    with urllib.request.urlopen(url) as f:
        # Loop through contents of file and print N rows based on user input
        for line in (f.readlines() [-N:]):
            # Format rows to print in vertical order in utf-8
            formattedLines = line.decode("utf-8")
            print(formattedLines, end ='') 

# Prompt user for number of rows 
N = input("Enter number of records desired: ")

# Cast input to int to be passed through UrlReader function
UrlReader(int(N))
