import pandas as pd
import numpy as np
import re
import datetime

df = pd.read_csv('khan_news_202211221449.csv')
#컬럼이름 : "index","context","date"


stoplist = ['노래와 세상','NGO 발언대','황규관의 전환의 상상력','우리말 산책',
'詩想과 세상','케이블·위성 하이라이트','TV하이라이트','여적','COP27',
'신경과학 저널클럽','김용민의 그림마당','[숨]','김지연의 미술소환','[시선]',
'사유와 성찰','세상읽기','현장에서','내일 날씨','칼럼','책과 삶','기고',
'우당탕탕 귤엔터','박상희의 구해줘! 내 맘','이진송의 아니 근데','지극히 味적인 시장',
'이종산의 장르를 읽다','새책','오늘의 날씨','부고','홍경한의 예술산책-깊이 보다'
'김월회의 행로난','이굴기의 꽃산 꽃글','장도리','생각그림','경향포토',
'도재기의 천년향기','[직설]','신시 111년 건강의료 기획','청소년책','책과 삶',
'여적','박성진의 한국군 코멘터리','생각그림','경향사람들','이명학의 내 인생의 책',
'문명, 그 길을 묻다','오늘의 운세','사회공헌 특집','서민의 과학과 사회','여적',
'알림','이택광의 왜?','경향논단','스포츠 플러스','인사','어제의 오늘','게시판',
'시민 기자석','인물로 본 2008 정치','아침을 열며','오늘의 경기','돋보기','말속의 말',
'독자의 소리','문화플라자','지금, 여기']


def khan_new(df):
    df = df.drop_duplicates(['context'])

    df_result = pd.DataFrame()
    
    for i in stoplist:
        result = df[df['context'].str.contains(i,na=False)]
        df_result = pd.concat([df_result,result])
    
    df = pd.merge(df,df_result, how='outer', indicator=True)
    df = df.query('_merge == "left_only"').drop(columns=['_merge'])
    df['date'] = df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y-%m-%d'))
    df = df.rename(columns={'context':'title'})
    df['company'] = 'khan'
    df = df.drop([df.columns[0]], axis=1)
    return df

df_k = khan_new(df)

    