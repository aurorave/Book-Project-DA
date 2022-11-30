import pandas as pd
import numpy as np
import re


chosun = pd.read_csv('chosun_news_202211211723.csv')

stoplist = ['통판광고','전면광고','신춘문예', '당선작', '일사일언', '동정', '생활한자', '리빙 포인트', '리빙포인트', 
    'hot & cold', '기업공시', '부음','플라자','편집자에게','신문은 선생님','알림','사진', '시사', '교양', '확성기', '기고', 
    '의견', '이규태', '경제 브리핑', '날씨 이야기', '문화게시판', '쇼트트랙', '취재메모', '아이스하키', '만물상', '태평로', 
    '시네마', '문화나들이 어디로 할까', '방송가', '튼튼스타', '단신', '새의자', '시시각각', '스포츠', 'TEPS', '연극리뷰', 
    '클래식', '부부의 속마음', '병원 Q & A', '여행수첩', '여행단신', '그래픽 뉴스', '오태진', '내정', '사진기사', 
    '이곳이 좋아요', '알뜰정보', '학술 소식', '조용헌', '알립니다', '호남사람들', '인사;']
    

def chosun_new(chosun):
    df = chosun.drop([chosun.columns[0]], axis = 1)
    df = df.rename(columns={'0':'title'})
    df = df.drop_duplicates(['title'])
    
    df_result = pd.DataFrame()

    for i in stoplist:
        result = df[df['title'].str.contains(i)]
        df_result = pd.concat([df_result,result])

    df = pd.merge(df, df_result, how='outer', indicator=True)
    df = df.query('_merge == "left_only"').drop(columns=['_merge'])
    df['company'] = 'chosun'
    return df

df_c = chosun_new(chosun)



    









