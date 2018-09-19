import MySQLdb
import bs4
import requests

res=requests.get("https://www.indiamart.com/jcbindialtd/")
soup=bs4.BeautifulSoup(res.text,'lxml')
l=[]
for product in soup.find_all('h3',{"class":"bo1 fnt20_mn"}):
    l.append(product.text)

db = MySQLdb.connect(host='127.0.0.1', user='root', password='root', db='indiamart')
cur = db.cursor()
sql_insert_query='''REPLACE  INTO `indiamart`.`jcb_product` (`Product`) VALUES (%s)'''
df=cur.executemany(sql_insert_query,l)
db.commit()
print("Total "+str(len(l))+" Products Successfully stored in database.")