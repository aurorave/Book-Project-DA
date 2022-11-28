import pandas as pd
import numpy as np
import re
import datetime

'''
아니 왜 임포트만 했는데 출력이 되는건지... ??????
어이가없다..어이가없다..어이가.. 일단 밑에 주석처리 해놨서요

'''

# from chosun import df_c 
# from donga import df_d
# from joongang import df_j
# from hani import df_h
# from khan import df_k

'''
위에 임포트 넘 오래걸려서 걍 불러와서함
파일들도 같이 올려놨어요

'''
df_c = pd.read_csv('chosun_new.csv')
df_d = pd.read_csv('donga_new.csv')
df_j = pd.read_csv('joongang_new.csv')
df_k = pd.read_csv('khan_new.csv')
df_h = pd.read_csv('hani_new.csv')


final_before = pd.concat([df_c,df_d,df_j,df_k,df_h])
final = final_before.copy()

def make_final(final):
    final = final.drop([final.columns[0]], axis=1)
    final['year']= final['date'].str.slice(0,4)
    final['month']= final['date'].str.slice(5,7)
    final['day']= final['date'].str.slice(8,10)
    final['date'] = pd.to_datetime(final.date)
    final = final.sort_values('date')
    final = final.reset_index()
    final = final.drop([final.columns[0]], axis=1)
    return final


news_sum = make_final(final)
titles = news_sum['title'].iloc[101:110] 


#자연어처리부분
import konlpy
from konlpy.tag import Okt
from konlpy.utils import pprint
from collections import Counter
okt = Okt()

#불용어 사전 - 파일첨부해놓음
#자연어처리한 부분이 현재 분석에 필요하지않아 
#따로 사용 안하는 중이지만 일단은 드립니다

def get_stopwords():
    stopwords = list()
    
    f = open('stopwords.txt', 'r', encoding='utf-8')
    
    while True:
        line = f.readline()
        if not line: break
        stopwords.append(line.strip())
        
    return stopwords



#함수 아래 첫줄 자연어 처리할부분 타이틀변수에 저장해서 사용
#46번 줄 참고하쉐요

def frequency(titles):
    titles = titles.str.replace("[^ ㄱ-ㅣ가-힣A-Za-z]","",regex=True)
    stopwords = get_stopwords()
    titles = titles.apply(okt.morphs)
    titles = titles.apply(lambda x: [item for item in x if item not in stopwords])
    keywords = np.hstack(titles.values)
    keywords_counting = Counter(keywords)
    keywords_counting.most_common(10)
    print(keywords_counting)

frequency(titles)



