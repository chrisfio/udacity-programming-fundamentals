import time
import webbrowser

total_breaks = 3
break_count = 0

print("This is the start of the program " +time.ctime())

while(break_count<total_breaks):
	time.sleep(10)
	webbrowser.open("http://www.chrisfiorino.com")
	break_count += 1