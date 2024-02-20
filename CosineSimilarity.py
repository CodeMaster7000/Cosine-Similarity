from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

print("The cosine similarity ranges from 0 to 1.")
print("0: No similarity between the two sentences.")
print("1: The two sentences are identical in terms of their word content.")
print()

X = input("Enter first sentence: ").lower() 
Y = input("Enter second sentence: ").lower() 

X_list = word_tokenize(X) 
Y_list = word_tokenize(Y) 

sw = stopwords.words('english') # Stopwords
l1 =[];l2 =[] 

X_set = {w for w in X_list if not w in sw} 
Y_set = {w for w in Y_list if not w in sw} 

rvector = X_set.union(Y_set) 
for w in rvector: 
    if w in X_set: l1.append(1) # Create vector
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0) 
c = 0

for i in range(len(rvector)): 
    c += l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 
print("Similarity between the two sentences: ", cosine) 
