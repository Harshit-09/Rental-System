date_string = '12-25-2018'
format = "%Y-%m-d"
try:
  datetime.datetime.strpti(date_string, format)
  print("This is the correct datstring format.")
except ValueError:
   print("This is the incorrect datstring format. It should be YYYY-MM-DD")