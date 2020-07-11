import re

str = input('Please enter string with mobile number: ')
phone = re.search(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', str)
print(phone)
