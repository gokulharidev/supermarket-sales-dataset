
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('supermarket.csv')
data=pd.DataFrame(data)
data=data.fillna('0')
data['City']=data['City'].astype('str')
data['City']=data['City'].str.upper()
data['Branch']=data['Branch'].astype('str')
data['Customer type']=data['Customer type'].astype('str')
data['Gender']=data['Gender'].astype('str')
data['Product line']=data['Product line'].astype('str')
data['Date']=pd.to_datetime(data['Date']) 
data['gross margin percentage']=round(data['gross margin percentage'],2)
#print(data.info())  
data.to_csv('output.csv',index=False)

data['date']=data['Date'].dt.date
data['month']=data['Date'].dt.month
dateinc = data.groupby('month')['gross income'].sum()
plt.plot(dateinc, color='skyblue')
plt.xlabel('months in number')
plt.ylabel('gross income')
plt.show()
#date and gross income 

datecog = data.groupby('month')['cogs'].sum()
plt.plot(datecog, color='skyblue')
plt.xlabel('months in number')
plt.ylabel('cost of goods sold')
plt.show()
#date and cogs

datot=data.groupby(data['date'])['Total'].sum()
plt.plot(datot, color='skyblue')
plt.xlabel('date in number')
plt.ylabel('cost of goods sold')
plt.show()
#total and date

braninc=data.groupby('Branch')['gross income'].sum()
plt.bar(braninc.index,braninc.values)
plt.xlabel('branch')
plt.ylabel('gross income')
plt.show()
#branch and gross income

branqua=data.groupby('Branch')['Quantity'].sum()
plt.bar(branqua.index,branqua.values)
plt.xlabel('branch')
plt.ylabel('quantity sold')
plt.show()
#branch and quantity

promar=data.groupby('Product line')['gross margin percentage'].mean()
plt.bar(promar.index,promar.values)
plt.xlabel('product')
plt.ylabel('gross margin')
plt.xticks(fontsize=6)
plt.show()
#product and margin

proinc=data.groupby('Product line')['gross income'].sum()
plt.bar(proinc.index,proinc.values)
plt.xlabel('product')
plt.ylabel('gross income')
plt.xticks(fontsize=6)
plt.show()
#product and income

prora=data.groupby('Product line')['Rating'].mean()
plt.bar(prora.index,prora.values)
plt.xlabel('product')
plt.ylabel('rating')
plt.xticks(fontsize=6)
plt.show()
#product and rating

citpr=data.groupby('City')['Product line'].count()
plt.pie(citpr.values,labels=citpr.index)
plt.show()
#[pie is useful when visula at single entity]