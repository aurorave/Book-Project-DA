#필요한 라이브러리 소환

import pandas as pd
import numpy as np
import re

hani = pd.read_csv('hani_news_202211262344.csv')
#칼럼 "index","category","title","pdate"


stoplist = ['책&생각','육퇴한 밤','강재훈의 살핌','슬기로운 기자생활','김명인 칼럼','숨&결',
'나는 역사다','오금택의 100㎝','날씨','타인의 시선','권혁웅의 오목렌즈','전우용의 현대를 만든 물건들']



def hani_new(hani):
    df = hani.drop([hani.columns[0]], axis=1)
    df = df[['title','pdate','category']]
    df = df.drop_duplicates(['title'])
    
    df_result = pd.DataFrame()
    for i in stoplist:
        result = df[df['title'].str.contains(i,na=False)]
        df_result = pd.concat([df_result,result])

    df = pd.merge(df,df_result, how='outer', indicator=True)
    df = df.query('_merge == "left_only"').drop(columns=['_merge'])
    df['pdate'] = df['pdate'].str.slice(4,14)
    df = df.rename(columns={'pdate':'date'})
    df['company'] = 'hani'
    df = df[['title','date','company','category']]
    return df


df_h = hani_new(hani)


