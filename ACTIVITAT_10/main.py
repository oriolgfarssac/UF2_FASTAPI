import pandas as pd
from connection import conexio

readedDocument = pd.read_csv("paraules_temàtica_penjat.csv")
processedDocument = readedDocument.to_dict(orient="list")
words = processedDocument['WORD']
themes = processedDocument['THEME']

enviar = True
cursor = conexio()
for word, theme in zip(words, themes):
    sql = '''
        INSERT INTO jocDelPenjat (word_column, theme_column)
        VALUES (?, ?)
        '''
    cursor.execute(sql, (word, theme))

