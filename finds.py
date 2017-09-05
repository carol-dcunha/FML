import random

attributes = [['Sunny','Rainy'],['Warm','Cold'],['Normal','High'],['Strong','Weak'],['Warm','Cool'],['Same','Change']]
num_attributes=len(attributes)

def getRandomTrainingExample(target_concept=['?']*num_attributes):
	training_example=[]
	classification=True
	for i in range(num_attributes):
		training_example.append(attributes[i][random.randint(0,1)])
		if target_concept[i]!='?' and target_concept[i]!=training_example[i]:
			classification=False
	return training_example,classification

def main():
	target_concept=['Sunny','Warm','?','?','?','?']
	num_experiments=15
	training_examples=[]

	for i in range(num_experiments):
		training_examples.append(getRandomTrainingExample(target_concept))
		print(training_examples[i])

if __name__=="__main__":
	main()