import json
import requests  
from flask import Flask



app = Flask (__name__)


#if __name__=="__main__":
price_list = []
response = requests.get("http://api.nbp.pl/api/cenyzlota/last/30/?format=json")
data=response.json()
print(type(data))
print(f"zawartosć data to : {data[-2:-1]}")
for i in data:
    #print(f"data: {i['data']} cena tego dnia {i['cena']}")
    price_list.append(i['cena'])
    
@app.route("/")
def main():
    return f"dzisiejsza cena wzgledem wczorajszej : {round(float(price_list[-1]-price_list[-2]),2)},zł" 


if __name__ == '__main__':
    app.run(debug=True)

"""with open("baza.csv",'w') as f:
        writer = csv.writer(f) #inicjalizuje zapisywacz
        columns = ['data','cena']
        writer.writerow(columns)# wpisuje nazwy kolumn (pierwsze linie pola)
        for row in data:
            print(row)
            writer.writerow(row)"""


"""  with open("baza.csv") as f:
        for i in f:
            print(f"wiersz zawiera : {i} \n")"""
# dict = json.loads(file jsona)
    #print(data)

    
"""Sztabki złota o gramaturach 1 g, 2g, 5 g, 10 g, 20 g, 31,1 g, 50 g, 100 g
         oraz złote monety bulionowe - 1 oz, 1/2 oz, 1/4 oz i 1/10 oz:]
         gold_list_units = [(1,'g'),(2,'g'),(5,'g'),(10,'g'),(20,'g'),(31,1,'g'),(50,'g'),(100,'g')] """