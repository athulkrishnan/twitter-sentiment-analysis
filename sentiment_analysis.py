from textblob import TextBlob
import pandas as pd
import numpy as np


def sentiment_detection(filname,col):
    data = pd.read_excel(filname)
    blob = [TextBlob(data[col].ix[i]) for i in range(len(data))]
    data['polarity'] = [blob[i].sentiment.polarity for i in range(len(blob))]
    data['prediction'] = np.where(data['polarity'] < 0, 'negative',(np.where(data['polarity']  > 0, 'positive','neutral')))  
    pd.DataFrame.to_excel(data,'sentiprediction.xlsx')


