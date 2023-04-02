import pandas as pd
import math

def oklid_uzaklik(x1, x2):
    uzaklik = 0.0
    for i in range(len(x1)):
        uzaklik += (x1[i] - x2[i])**2
    return math.sqrt(uzaklik)

def chebyshev_uzaklik(x1, x2):
    uzaklik = 0.0
    for i in range(len(x1)):
        uzaklik = max(uzaklik, abs(x1[i] - x2[i]))
    return uzaklik

def jaccard_uzaklik(x1, x2):
    intersection = len(set(x1).intersection(set(x2)))
    union = len(set(x1).union(set(x2)))
    uzaklik = 1.0 - (intersection / union)
    return uzaklik


class KNN:
    def __init__(self, uzaklik_fonks, k, x_train,y_train, x_test):
        self.uzaklik_fonks = uzaklik_fonks
        self.k = k
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
    
    def knn(self):
        uzakliklar = []
        for i in range(len(self.x_train)):
            uzaklik = self.uzaklik_fonks(self.x_train[i], self.x_test)
            uzakliklar.append((uzaklik, i))
        uzakliklar.sort()
        komsular = []
        for i in range(self.k):
            komsular.append(uzakliklar[i][1])
        votes = {}
        for i in komsular:
            if self.y_train[i] in votes:
                votes[self.y_train[i]] += 1
            else:
                votes[self.y_train[i]] = 1
        sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
        return sorted_votes[0][0]

# DATASET
iris_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

X_train = iris_df.iloc[:, :-1].values.tolist()
Y_train = iris_df.iloc[:, -1].values.tolist()

# TEST ORNEKLERI

# OKLID ICIN
print("\nOKLID UZAKLIK METRIGI ICIN")
X_test1 = [4.6,3.1,1.5,0.2] # Iris-setosa  # datasette random bir koordinat 
k = 5
prediction1 = KNN(oklid_uzaklik,k, X_train, Y_train, X_test1)
print("Oklid - test1 :",prediction1.knn())  

X_test2 = [5.4,3.0,4.5,1.5] # Iris-versicolor
k = 5
prediction2 = KNN(oklid_uzaklik,k, X_train, Y_train, X_test2)
print("Oklid - test3 :",prediction2.knn()) 

X_test3 = [7.6,3.0,6.6,2.1] # Iris-virginica
k = 5
prediction2 = KNN(oklid_uzaklik,k, X_train, Y_train, X_test3)
print("Oklid - test2 :",prediction2.knn())
    

# CHEBYSHEV ICIN
print("\nCHEBYSHEV UZAKLIK METRIGI ICIN")
X_test1 = [5.1,2.5,3.0,1.1] # Iris-versicolor 
k = 5
prediction1 = KNN(chebyshev_uzaklik,k, X_train, Y_train, X_test1)
print("Chebyshev - test1 :",prediction1.knn())  

X_test2 = [4.7,3.2,1.3,0.2] # Iris-setosa  
k = 5
prediction2 = KNN(chebyshev_uzaklik,k, X_train, Y_train, X_test2)
print("Chebyshev - test3 :",prediction2.knn())
X_test3 = [5.9,3.0,5.1,1.8] # Iris-virginica
k = 5
prediction2 = KNN(chebyshev_uzaklik,k, X_train, Y_train, X_test3)
print("Chebyshev - test2 :",prediction2.knn())


# JACCARD ICIN
print("\nJACCARD UZAKLIK METRIGI ICIN")
X_test1 = [6.4,2.8,5.6,2.1] # Iris-virginica 
k = 5
prediction1 = KNN(chebyshev_uzaklik,k, X_train, Y_train, X_test1)
print("Jaccard - test1 :",prediction1.knn())  

X_test2 = [5.7,2.8,4.1,1.3] # Iris-versicolor   
k = 5
prediction2 = KNN(chebyshev_uzaklik,k, X_train, Y_train, X_test2)
print("Jaccard - test3 :",prediction2.knn())

X_test3 = [5.0,3.4,1.5,0.2] # Iris-setosa
k = 5
prediction2 = KNN(chebyshev_uzaklik,k, X_train, Y_train, X_test3)
print("Jaccard - test2 :",prediction2.knn())
    