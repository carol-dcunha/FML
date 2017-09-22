import random

attributes = [['Sunny','Rainy'],['Warm','Cold'],['Normal','High'],['Strong','Weak'],['Warm','Cool'],['Same','Change']]
num_attributes=len(attributes)
hp = [0]*num_attributes


def getRandomTrainingExample(target_concept=['?']*num_attributes):
	training_example=[]
	classification=True
	for i in range(num_attributes):
		training_example.append(attributes[i][random.randint(0,1)])
		if target_concept[i]!='?' and target_concept[i]!=training_example[i]:
			classification=False
	return training_example,classification

def findS(training_instance):
	global hp
	print "x:\t",training_instance
	if training_instance[1]:
		if 0 in hp:
			hp=training_instance[0]
		else:
			for i in range(num_attributes):
				if hp[i] != training_instance[0][i]:
					hp[i]='?'
	print "H:\t",hp,"\n"


def main():
	target_concept=['Sunny','Warm','?','Strong','?','?']
	num_experiments=10
	training_examples=[]
	print "H:\t",hp,"\n"
	for i in range(num_experiments):
		training_examples.append(getRandomTrainingExample(target_concept))
		findS(training_examples[i])
	



if __name__=="__main__":
	main()
