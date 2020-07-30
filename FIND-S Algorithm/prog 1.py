import pandas as pd
	
df = pd.read_csv("enjoysport.csv")
print("The data is: \n\n",df)
print("\n"+"*" * 70)
print("The shape of dataset is",df.shape,"\n")
# defining the attributes
num_attributes = 6
#initialize the instance
a = []
#stroing the dataset items in list
for i in range(len(df)):
    a.append(df.iloc[i].tolist())
	
#storing zero at every place 
hypo = ['0']* num_attributes
# initialize the specific hypothesis
for j in range(0, num_attributes):
    hypo[j] = a[0][j]
print("Most Specific hypotheis is: ",hypo)
# For each positive training instance x
for i in range(len(a)):
    if a[i][num_attributes]=='yes':
        for j in range(0,num_attributes):# For each attribute constraint ai in h
            if a[i][j] != hypo[j]:# Else replace ai in h by the next more general constraint that is satisfied by x
                hypo[j]="?"
    else:# If the constraint ai is satisfied by x
        hypo[j]=a[i][j]# Then do nothing
    print(" \n\nFor Training instance No:{0} the hypothesis is\n".format(i),hypo)    # Output hypothesis h       
	
print("\n The Maximally Specific Hypothesis for a given Training Examples :\n")
print(hypo)
