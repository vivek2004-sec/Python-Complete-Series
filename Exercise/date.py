from datetime import datetime

now = datetime.now()
print(now.strftime("%H"))  # Hour (24-hour format)
print(now.strftime("%M"))  # Minute
print(now.strftime("%S"))  # Second
print(now.strftime("%y"))  # Year (2-digit)
print(now.strftime("%Y"))  # Year (4-digit)
print(now.strftime("%m"))  # Month (01-12)
print(now.strftime("%d"))  # Day of the month (01-31)
print(now.strftime("%a"))  # Abbreviated weekday (e.g., Mon)
print(now.strftime("%A"))  # Full weekday (e.g., Monday)
print(now.strftime("%b"))  # Abbreviated month name (e.g., Jan)
print(now.strftime("%B"))  # Full month name (e.g., January)
print(now.strftime("%c"))  # Locale's full date and time
print(now.strftime("%I"))  # Hour (12-hour format)
print(now.strftime("%j"))  # Day of the year (001-366)
print(now.strftime("%p"))  # AM/PM
print(now.strftime("%U"))  # Week number of the year (Sunday as the first day)
print(now.strftime("%u"))  # Weekday (1=Monday, 7=Sunday)
print(now.strftime("%w"))  # Weekday (0=Sunday, 6=Saturday)
print(now.strftime("%W"))  # Week number of the year (Monday as the first day)
print(now.strftime("%x"))  # Locale's date representation
print(now.strftime("%X"))  # Locale's time representation
print(now.strftime("%%"))  # A literal '%'
