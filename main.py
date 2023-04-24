from bs4 import BeautifulSoup
import requests
import csv

# url = 'http://nxcoreapi.com/symbols.php?search=alti&m_exchange=AMEX&m_type=e&s_type=contains&m_symbol=on&m_name=on'
# url = 'http://nxcoreapi.com/symbols.php?search=&m_exchange=&m_type=e&s_type=contains&m_symbol=on&m_name=on'

url = input("Please enter URL: ")
filename=input("Please type filename(WO /'.csv/' extension): ")

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

data = []
for tr in table.find_all('tr'):
    row = []
    for td in tr.find_all('td'):
        row.append(td.text)
    data.append(row)

filename += ".csv"


with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)

len = len(data)-1

print("done, {d} rows saved (WO Header row)".format(d=len))
input("Press any key to exit\n")