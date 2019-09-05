from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
import csv

x = []
y = []
counter = 1
headerdel = 0
my_url = "https://www.currency-converter.org.uk/currency-rates/historical/table/USD-INR.html"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")

filename = "USD-INR.csv"
f = open(filename,"w")

#Can add these headers to csv file, but it creates problem during visualization
#headers = "Date,High,Open,Low,Close*,Adj.close**,Volume\n"
#f.write(headers)

TableContainer = page_soup.findAll("div",{"id":"content"})
Table1 = TableContainer[0].table
Table = Table1.findAll("tr")

for DataRow in Table:
    ValContainer = DataRow.findAll("td")
    if (headerdel==0):
        headerdel+=1
        continue
    for ValueC in ValContainer:
        if((counter%5)==0):
            counter+=1
            continue
        Value = ValueC.text
        if((counter%5)==2):
            x.append(Value)
            #print(x)
        if((counter%5)==4):
            Rupee = float(Value.strip('INR'))
            y.append(Rupee)
            #print(Rupee)
        f.write(Value+",")
        counter+=1
    f.write("\n")
        #print(Value)
    #print("----------------------------------------------")

f.close()

'''
with open('SENSEX_Shares.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print(row)
        x.append(row[0])
        if(x[0]=='Date'):
            del x[0]
        y.append(float(row[5]))
        print(y)
'''

x.reverse()
#print(x)
print('Len X is : ',len(x))
print('------------------------')
y.reverse()
#print(y)
print('Len Y is : ',len(y))
plt.plot(x,y)
plt.xlabel('Dates -->')
plt.ylabel('U S Dollar Vs Indian Rupee-->')
plt.subplots_adjust(bottom=0.20)
plt.xticks(x,rotation='vertical')
plt.title('USD vs INR')
plt.show()

