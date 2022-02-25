import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from six import StringIO
import graphviz
from sklearn.tree import export_graphviz
import pydotplus
from IPython.display import Image

# Carrega dataset original
wine_ds = pd.read_csv("wine.csv")
wine_ds.columns = ['Cult', 'Alc', 'MA', 'Ash', 'AA', 'M', 'TP', 'Flav' , 'NFP', 'Proa', 'CI', 'Hue', 'ODDW', 'Prol'] # redução dos nomes para que o dataset caiba no ecrã

# Mostra dataset
print("\n* DATASET *\n")
print(wine_ds)

attributes = wine_ds.columns
print("\nOs atributos no dataset são: \n", attributes, "\nque correspondem respetivamente (em inglês): \nCultivar, Alcohol, Malic Acid, Ash, Alcalinity of Ash, Magnesium, Total Phenols, Flavanoids, Nonflavanoid Phenols, Proanthocyanins, Color Intensity, Hue, OD280/OD315 of Diluted Wines, Proline")

# Existem alguns registos com dados NaN?
print("\n* TRATAMENTO DE NaN *\n")
NaN_data_flag = wine_ds.isnull().any()
if NaN_data_flag.any():
    print("Alguns registos têm valores de NaN. Estes serão removidos...\n")
    before_rows, before_cols = wine_ds.shape
    wine_ds = wine_ds.dropna()
    after_rows, after_cols = wine_ds.shape
    print("Descartados", after_rows - before_rows, "registos. O dataset tratado tem", after_rows, "registos.\n")
else:
    print("OK")

# Estatística descritiva
print("\n* ESTATÍSTICA DESCRITIVA *\n")
pd.options.display.max_columns = wine_ds.shape[1]
print(wine_ds.describe()) # detalhes estatísticos básicos como percentil, média, std etc.

print("\n* GRÁFICOS E HISTOGRAMAS *\n")
# Gráfico de pizza - Amostras por cultivar
region_counts = wine_ds['Cult'].value_counts()
explode = (0, 0.1, 0)
region_counts.plot(kind='pie',autopct='%.0f%%', shadow=True, figsize=(4,4), radius=1.0)
plt.title('Distribuição - Cultivar')
plt.show()

# Gráfico de dispersão - Teor Alcoólico X Cultivar
wine_ds.plot.scatter(x = 'Alc', y = 'Cult')
plt.title('Teor Alcoólico X Cultivar')
plt.show()

# Histograma - Álcool
hist_quality = wine_ds['Alc']
plt.hist(hist_quality, 10, facecolor='orange')
plt.title('Distribuição - Teor Alcoólico')
plt.xlabel('Álcool')
plt.ylabel('Contagem')
plt.grid(False)
plt.show()

# Histograma - Total de fenóis
hist_fixed = wine_ds['TP']
plt.hist(hist_fixed, 10, facecolor='green')
plt.title('Distribuição - Fenóis')
plt.xlabel('Fenóis')
plt.xticks(rotation=90)
plt.locator_params(axis="x", nbins=20)
plt.ylabel('Contagem')
plt.grid(False)
plt.show()

# Histograma - Total de fenóis não flavonóides
hist_citric = wine_ds['NFP']
plt.hist(hist_citric, 10, facecolor='blue')
plt.title('Distribuição - Não flavonóides')
plt.xlabel('Fenóis Não Flavonóides')
plt.xticks(rotation=90)
plt.locator_params(axis="x", nbins=19)
plt.ylabel('Contagem')
plt.grid(False)
plt.show()

# Histograma - Intensidade de cor
hist_volatile = wine_ds['CI']
plt.hist(hist_volatile, 10, facecolor='red')
plt.title('Distribuição - Intensidade da Cor')
plt.xlabel('Intensidade da Cor')
plt.xticks(rotation=90)
plt.locator_params(axis="x", nbins=20)
plt.ylabel('Contagem')
plt.grid(False)
plt.show()

# Teste de técnicas  de classificação
print("\n * TESTE DE TÉCNICAS DE CLASSIFICAÇÃO - ACURÁCIA *\n")

# Dataset dividido em features e target variable
# apenas para teste: feature_cols = ['Cult', 'Alc', 'MA', 'Ash', 'AA', 'M', 'TP']
feature_cols = wine_ds.columns
X = wine_ds[feature_cols] # Features: todos
Y = wine_ds.Cult # Target variable: Cultivar

print("X -> FEATURES:\n", X)
print("\nY -> TARGET VARIABLE:\n", Y)

# Divide o dataset em conjunto de training e conjunto de testes
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4) # 60% training e 40% test
print("\nX_train (dataset de training): ", X_train.shape)
print("X_test (dataset de teste): ", X_test.shape)

# Resultados
print("\nRESULTADOS:\n")
models = []
models.append(("Decision Tree:",DecisionTreeClassifier()))
models.append(("Naive Bayes:",GaussianNB()))
models.append(("AdaBoost Classifier:",AdaBoostClassifier()))
models.append(("Gradient Boosting Classifier:",GradientBoostingClassifier()))
models.append(("Random Forest:",RandomForestClassifier(n_estimators=7)))
models.append(("Support Vector Machine - Linear:",SVC(kernel="linear")))
models.append(("Support Vector Machine - Radial Basis Function (RBF)",SVC(kernel="rbf")))
models.append(("K-Nearest Neighbour:",KNeighborsClassifier(n_neighbors=3)))
models.append(("Multi-layer Perceptron (MLP):",MLPClassifier(hidden_layer_sizes=(45,30,15),solver='sgd',learning_rate_init=0.01,max_iter=500)))
results = []
names = []
for name,model in models:
    kfold = KFold(n_splits=10)
    cv_result = cross_val_score(model,X_train,Y_train.values.ravel(), cv = kfold,scoring = "accuracy")
    names.append(name)
    results.append(cv_result)
for i in range(len(names)):
    print(names[i],results[i].mean())

# Classificação utilizando árvore de decisão
print ("\n* ÁRVORE DE DECISÃO *\n")

classifier = DecisionTreeClassifier() # Cria objeto Decision Tree Classifer
classifier = classifier.fit(X_train,Y_train) # Train Decision Tree Classifer

Y_pred = classifier.predict(X_test) # Prevê a resposta para o dataset do teste
print("Y_pred:", Y_pred)

print("\nAcurácia: ", metrics.accuracy_score(Y_test, Y_pred)) # Acurácia do modelo, freqüência que o classificador é correto
print("\nMatriz de Confusão: \n", metrics.confusion_matrix(Y_test, Y_pred)) # Matriz de confusão
print("\nRelatório de Classificação: \n", metrics.classification_report(Y_test, Y_pred)) # Relatório de Classificação

print("* IMAGEM DA ÁRVORE DE DECISÃO *")
dot_data = StringIO()
export_graphviz(classifier, out_file=dot_data, feature_names=feature_cols)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('wine.png')
Image(graph.create_png())

print("\n* FIM - ÁRVORE DE DECISÃO - CULTIVAR*\n")

print("\n* TESTE COM ÁLCOOL (ARREDONDADO) *\n")

#TESTAR
Y = wine_ds.Alc.round() # Target variable: Álcool (valor arredondado)

print("\nY -> TARGET VARIABLE:\n", Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4) 
print("\nX_train (dataset de training): ", X_train.shape)
print("X_test (dataset de teste): ", X_test.shape)

# Resultados
print("\nRESULTADOS:\n")
models = []
models.append(("Decision Tree:",DecisionTreeClassifier()))
models.append(("Naive Bayes:",GaussianNB()))
models.append(("AdaBoost Classifier:",AdaBoostClassifier()))
models.append(("Gradient Boosting Classifier:",GradientBoostingClassifier()))
models.append(("Random Forest:",RandomForestClassifier(n_estimators=7)))
models.append(("Support Vector Machine - Linear:",SVC(kernel="linear")))
models.append(("Support Vector Machine - Radial Basis Function (RBF)",SVC(kernel="rbf")))
models.append(("K-Nearest Neighbour:",KNeighborsClassifier(n_neighbors=3)))
models.append(("Multi-layer Perceptron (MLP):",MLPClassifier(hidden_layer_sizes=(45,30,15),solver='sgd',learning_rate_init=0.01,max_iter=500)))
results = []
names = []
for name,model in models:
    kfold = KFold(n_splits=10)
    cv_result = cross_val_score(model,X_train,Y_train.values.ravel(), cv = kfold,scoring = "accuracy")
    names.append(name)
    results.append(cv_result)
for i in range(len(names)):
    print(names[i],results[i].mean())

print ("\n* ÁRVORE DE DECISÃO *\n")

classifier = DecisionTreeClassifier() 
classifier = classifier.fit(X_train,Y_train)

Y_pred = classifier.predict(X_test) 
print("Y_pred:", Y_pred)

print("\nMatriz de Confusão: \n", metrics.confusion_matrix(Y_test, Y_pred)) 
print("\nRelatório de Classificação: \n", metrics.classification_report(Y_test, Y_pred))

print("* IMAGEM DA ÁRVORE DE DECISÃO *")
dot_data = StringIO()
export_graphviz(classifier, out_file=dot_data, feature_names=feature_cols)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('wine2.png')
Image(graph.create_png())

print("\n* FIM - ÁLCOOL (ARREDONDADO) *\n")

