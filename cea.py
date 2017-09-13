import random

attributes = [['Sunny','Rainy'],['Warm','Cold'],['Normal','High'],['Strong','Weak'],['Warm','Cool'],['Same','Change']]
num_attributes=len(attributes)

S = [['0']*num_attributes]
G = [['?']*num_attributes]


def getRandomTrainingExample(target_concept=['?']*num_attributes):
	training_example=[]
	classification=True
	for i in range(num_attributes):
		training_example.append(attributes[i][random.randint(0,1)])
		if target_concept[i]!='?' and target_concept[i]!=training_example[i]:
			classification=False
	return training_example,classification


#check if positive training example is consistent with G
#remove inconsistent hypothesis' from G
def pConsistent(instance):
	global G
	glist=[]
	for i in range(len(G)):
		for j in range(num_attributes):
			if G[i][j] != '?' and instance[j] != G[i][j]:
				glist.append(G[i])
				break
	for item in glist:
		G.remove(item)


#check if negative training example is consistent with S
#remove inconsistent hypothesis' from S
def nConsistent(instance):
	global S
	slist=[]
	for i in range(len(S)):
		flag=True
		for j in range(num_attributes):
			if instance[j] != S[i][j]:
				flag=False
				break
		if flag:
			slist.append(S[i])
	for item in slist:
		S.remove(item)


#get other attributes values 
def getOtherValues(index,value):
	global attributes
	return [x for x in attributes[index] if x!=value]


#generalise hypothesis' in S wrt positive training example
def generaliseS(instance):
	global S
	for sitem in S:
		if '0' in sitem:
			S.pop()
			S.append(instance)
			break
		else:
			for j in range(num_attributes):
				if sitem[j] != instance[j]:
					sitem[j]='?'
	
	#remove duplicates if any
	newlist=[]
	for item in S:
		if item not in newlist:
			newlist.append(item)
	S=newlist


#specialise hypothesis' in G wrt negative training example
def specialiseG(instance):
	global G
	glist=[]
	newg=[]
	for gitem in G:
		for j in range(num_attributes):
			if gitem[j]=='?':
				vals=getOtherValues(j,instance[j])
				for v in vals:
					newitem=list(gitem)
					newitem[j]=v
					newg.append(newitem)
				if gitem not in glist:
					glist.append(gitem)
	for item in glist:
		G.remove(item)
	for item in newg:
		G.append(item)
	
	#remove duplicates if any
	newlist=[]
	for item in G:
		if item not in newlist:
			newlist.append(item)
	G=newlist


#check if hypothesis' in G and S are consistent with each other
def checkBoundaries(type):
	global G,S

	if type == "G": #check if G is consistent with S for negative training example
		glist=[] 
		for gitem in G:
			for sitem in S:
				for j in range(num_attributes):
					if sitem[j]!=gitem[j] and gitem[j]!='?' and sitem[j] != '0':
						glist.append(gitem)
						break
		for item in glist:
			G.remove(item)
	
	elif type == "S": #check if S is consistent with G for positive training example
		slist=[]
		for sitem in S:
			for gitem in G:
				for j in range(num_attributes):
					if sitem[j]!=gitem[j] and gitem[j]!='?' and sitem[j] != '0':
						slist.append(sitem)
						break
		for item in slist:
			S.remove(item)
	
	#if either G or S is empty
	if len(G)==0:
		S=[]
	elif len(S)==0:
		G=[]


#perform candidate elimination algorithm
def CEA(instance,target):
	global S,G
	print "\nX:\t",instance,"\t",target,"\n"
	if target:
		pConsistent(instance)
		generaliseS(instance)
		checkBoundaries("S")
	else:
		nConsistent(instance)
		specialiseG(instance)
		checkBoundaries("G")
	print "G:\t",G	
	print "S:\t",S,"\n"



def main():
	target_concept=['Sunny','Warm','?','Strong','?','?']
	num_experiments=10
	training_examples=[(['Sunny','Warm','Normal','Strong','Warm','Same'],True),(['Sunny','Warm','High','Strong','Warm','Same'],True),(['Rainy','Cold','High','Strong','Warm','Change'],False),(['Sunny','Warm','High','Strong','Cool','Change'],True)]
	#training_examples=[]

	print "G:\t",G	
	print "S:\t",S,"\n"
	for i in range(4):
		#training_examples.append(getRandomTrainingExample(target_concept))
		CEA(training_examples[i][0],training_examples[i][1])


if __name__=="__main__":
	main()

