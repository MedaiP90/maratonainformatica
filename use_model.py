# modulo per caricare i modelli
from joblib import load

# moduli scikit-learn per le classificazioni
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# modulo per analisi dati
import pandas as pd  

class get_solutions:
    def __init__(self):
        self.clf = load('ml/models/text_model.joblib') # carico il modello di predizione
        df = pd.read_csv('ml/issueDB.csv', low_memory=False) # carico il DB che contiene le soluzioni
        df = df.dropna(subset=['TYPE'], axis=0) # pulisco le righe con tipo nullo
        df = df.dropna(subset=['SOLUTIONS'], axis=0) # pulisco le righe con soluzione nulla
        self.db = df[['TYPE', 'PP', 'SOLUTIONS']] # seleziono le colonne interessanti
        self.tp = pd.read_csv('Type.csv', low_memory=False) # carico i tipi per la traduzione

    def GetPrediction(self, issue):
        X = [issue]
        predicted = self.clf.predict(X)
        return predicted[0]

    def GetSolution(self, issue, pp):
        result = {} # preparo il dizionario (risultato del metodo)
        predict = self.GetPrediction(issue) # ottengo la predizione
        # seleziono le righe corrispondenti al tipo predetto
        solutions = self.db.loc[self.db['TYPE'] == predict]
        # seleziono la soluzione in base al pezzo considerato
        # (pezzi nulli danno soluzioni generiche "valide")
        solutions_notem = solutions.loc[solutions['PP'] == pp]
        solutions_empty = solutions.loc[solutions['PP'] == None] 
        solutions = pd.concat([solutions_notem, solutions_empty])
        result['solutions'] = solutions['SOLUTIONS'].tolist() # aggiorno il dizionario
        tpd = self.tp.loc[self.tp['Type'] == predict] # estraggo la riga corrispondente al tipo
        type_list = tpd['Description'].tolist()
        result['type'] = type_list[0] # aggiorno il dizionario
        return result