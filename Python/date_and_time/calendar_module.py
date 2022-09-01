# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
mm,dd,yyyy = input().split()
print(calendar.day_name[calendar.weekday(int(yyyy),int(mm),int(dd))].upper())