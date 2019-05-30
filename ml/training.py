# moduli per analisi dati e di calcolo
import pandas as pd  
import numpy as np  

# moduli scikit-learn per il machine learning
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# modulo per esportare i modelli
from joblib import dump

# caricamento dei dati dal database
df = pd.read_csv('issueDB.csv', low_memory=False) 

# le colonne interessate dall'analisi sono quelle
# del problema e del tipo quindi vanno ripulite le 
# righe con dei campi nulli
df = df.dropna(subset=['ISSUES'], axis=0)
df = df.dropna(subset=['TYPE'], axis=0)

# selezione delle colonne interessanti 
df = df[['TYPE', 'ISSUES', 'PP', 'SOLUTIONS']]

# creo la pipeline per le predizioni
clf = Pipeline([
    ('vect', CountVectorizer(ngram_range=(1,5))),
    ('tfidf', TfidfTransformer(use_idf=True)),
    ('clf', SGDClassifier(loss='hinge', penalty='elasticnet',
                         alpha=1e-5, random_state=42,
                         max_iter=5, tol=None)),
])

# creazione modello di predizione
clf = clf.fit(df['ISSUES'], df['TYPE'])

# esporto il modello di predizione per
# l'uso separato
dump(clf, 'models/text_model.joblib')