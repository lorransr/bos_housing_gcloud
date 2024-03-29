# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O9EhY7pZzc8Jw2OYbTd00jDsicZ5FHFc

## Regression Boston
"""
#importando bibliotecas
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import pickle
import os
#importando dados
boston_dataset = datasets.load_boston()

#definindo variaveis
X = boston_dataset.data
y = boston_dataset.target

#fitando o modelo
regressor = LinearRegression(normalize=True)
regressor.fit(X,y)

#criando a pasta model
os.mkdir("model")
#salvando o modelo
pickle.dump(regressor,open('model/regressor.pickle','wb'))
