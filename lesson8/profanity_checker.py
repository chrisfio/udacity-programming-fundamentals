import urllib

def read_text():
    quotes = open("/home/fio/Desktop/udacity/lesson8/movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Found!")
    elif "false" in output:
        print("This document contains no profanity.")
    else:
        print("There was an error scanning the document.")
    
read_text()
