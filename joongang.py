import pandas as pd
import numpy as np
import re
import datetime


df = pd.read_csv('joongang_news_202211212130.csv')
#최초컬럼명 "index","context","date"

stoplist = ['사진설명','신년사','문장으로 읽는 책','건강한 가족','오늘의 운세','만평','우리말 바루기','로또 복권','오늘의 날씨','사랑방',
'인사','부고','사진','채서영의 별별영어','중앙SUNDAY 카툰','책꽂이','쿠킹','분수대','시조가 있는 아침','KCSI 우수기업','분양 FOCUS',
'삶의 향기','권근영의 그림 속 얼굴','노트북을 열며','머니 브리핑','BOOK책갈피','어린이책','스포츠 중계','주말의 경기','스포츠카',
'행복한책 읽기']


def joongang_new(df):
    df['context'] = df['context'].str.strip("\n")
    df = df.drop_duplicates(['context'])
    
    df_result = pd.DataFrame()
    for i in stoplist:
        result = df[df['context'].str.contains(i)]
        df_result = pd.concat([df_result,result])

    df = pd.merge(df,df_result, how='outer', indicator=True)
    df = df.query('_merge == "left_only"').drop(columns=['_merge'])
    df['date']= df['date'].str.slice(0,10)
    df['date']= pd.to_datetime(df['date'])
    df = df.rename(columns={'context':'title'})
    df['company'] = 'joongang'
    df = df.drop([df.columns[0]], axis=1)
    return df

df_j = joongang_new(df)


    

