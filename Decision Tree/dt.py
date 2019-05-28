import pandas as pd,math
from copy import deepcopy

#read data file
data=pd.read_csv('dt.csv')

#set the source, attribute and outcome variable sets
S=['Outlook','Temperature','Humidity','Wind']
A={'Outlook':['Sunny','Rain','Overcast'],'Temperature':['Hot','Mild','Cool'],'Humidity':['High','Normal'],'Wind':['Weak','Strong']}
O=['Yes','No']
outcome='PlayTennis'

#Function to calculate entropy
#Input: dataframe classified based on outcome values
def entropy(data):
	pos=len(data[data[outcome]==O[0]])
	neg=len(data[data[outcome]==O[1]])
	total=len(data)
	if total==0:
		return 0
	pos=float(pos)/total
	neg=float(neg)/total

	#to deal with log(0)
	if pos==0:
		pos=1
	if neg==0:
		neg=1

	return -1*(pos*math.log(pos,2)+neg*math.log(neg,2))

#Function to compute information gain
#Input: E - entropy value of the dataframe
#       data - dataframe
#       attr - attribute over which gain is computed
#Output: tuple (attribute, entropy value)
def gain(E,data,attr):
	total=len(data)
	value=0

	#iterate over each value of the attribute
	for item in A[attr]:
		ea=entropy(data[data[attr]==item])
		num=len(data[data[attr]==item])
		value=value+(float(num)/total)*ea

	return (attr,round(E-value,3))

#Recursive function call to the decision tree algorithm
#Input: S - remaining source attributes
#       newdata - dataframe over which algorithm is iterated
#       tabs - number of tabs for display purposes
#Output: displays the decision tree
def _dt(S,newdata,tabs):
	newS=deepcopy(S)
	
	eS=entropy(newdata)

	#when the dataframe has only one classification
	if eS==0:
		print "\t",newdata['PlayTennis'].iloc[0]
		return

	if len(newS)!=0:
		gains=[]
		gainlist=[]

		#for each remaining attribute
		for item in newS:
			a=gain(eS,newdata,item)
			gains.append(a[1])
			gainlist.append(a)

		#select the next attribute 
		attr=newS[gains.index(max(gains))]
		print gainlist,"\n","\t"*tabs,
		print attr
		newS.remove(attr)

		#recursive call for the values of the selected attribute
		for item in A[attr]:
			print "\t"*tabs,
			print "\t",item,
			_dt(newS,newdata[newdata[attr]==item],tabs+2)


#Function that calls the recursive decision tree algorithm
def decisionTree():
	_dt(S,data,0)

#Main function
if __name__=="__main__":
	decisionTree()
	print "\n"