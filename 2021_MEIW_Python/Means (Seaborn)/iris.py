import pandas as pd  #importa biblioteca pandas
import seaborn as sns #importa biblioteca seaborn

p = pd.read_csv("iris_dataset.csv") #importa conjunto de dados com panda
s = sns.load_dataset("iris") #importa conjunto de dados com seaborn

#fornece snapshot das características do conjunto de dados
print("DATASET")
print(str(s.info()) + "\n") #informações
print(str(s.describe()) + "\n") #resumo de cada espécie
print(str(s.shape) + "\n") #contagem total de linhas e colunas
print((s.columns), "\n") #nomes das colunas do conjunto de dados

#encontra centróides (means)
print("Mean of Sepal Length is", s["sepal_length"].mean())
print("Mean of Sepal Width is", s["sepal_width"].mean())
print("Mean of Petal Length is", s["petal_length"].mean())
print("Mean of Petal Width is", s["petal_width"].mean())
print("\n")

#agrupa o conjunto de dados iris pela espécie
print("GROUP")
group = s.groupby("species")
print(group)

#encontra mean de cada atributo para as 3 espécies utilizando a função group
print("Mean of all 3 species")
print(group.mean())
print("\n")

#encontra mean através da divisão do conjunto de dados com a função loc - Seaborn
print("Mean of Setosa species")
print(s.loc[s["species"]=="setosa"].mean()) 
print("\n")
print("Mean of Versicolor species")
print(s.loc[s["species"]=="versicolor"].mean()) 
print("\n")
print("Mean of Virginica species")
print(s.loc[s["species"]=="virginica"].mean()) 
print("\n")

#encontra means através da divisão do conjunto de dados com a função iloc - Seaborn
print("Mean of Setosa species")
print(s.iloc[0:50].mean()) #dados estão entre linhas 0 e 50
print("\n")
print("Mean of Versicolor species")
print(s.iloc[50:100].mean()) #dados estão entre linhas 50 e 100
print("\n")
print("Mean of Virginica species")
print(s.iloc[100:150].mean()) #dados estão entre linhas 100 e 150
print("\n")

#divide o conjunto de dados com base na espécie com a função iloc - Pandas
print("SPLIT")
print("Setosa")
print(p.iloc[0:50])
print("\n")
print("Versicolor")
print(p.iloc[50:100]) 
print("\n")
print("Virginica")
print(p.iloc[100:150])

