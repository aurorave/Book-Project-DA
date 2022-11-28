import pandas as pd
import numpy as np
import re
import datetime



donga = pd.read_csv('donga_news_202211221448.csv')
#컬럼 이름 : index, 0, date

stoplist = ['부고','오늘의 채널A','오늘의 운세','사설','인사','알립니다','무비줌인','칼럼','포토 에세이','인사이드＆인사이트',
'게시판','바람개비','오늘의 경기','신문과 놀자!','우병탁의 절세통통(通)','양종구의 100세 시대 건강법','프리미엄뷰','머니 컨설팅',
'책의 향기','글로벌 포커스','우병탁의 절세통통','Food&Dining','DBR/Special Report','날씨 이야기','그림책 한조각','프리미엄뷰',
'edu+book','파워리더 인터뷰','알립니다','시사일본어학원','아파트 미리보기','Tech&','영남 파워기업','company&','특별기고','정도언의 마음의 지도',
'지표로 보는 경제','광화문에서','횡설수설','시론','안영식의 스포츠&','만화 그리는 의사들', '홍지윤 요리쌤의 오늘 뭐 먹지?','HBR','왕은철의 스토리와 치유',
'기고','직장인을 위한 김호의 생존의 방식','주성하 기자의 서울과 평양 사이','애널리스트의 마켓뷰','바둑','동아광장','Love&Gift','골든걸','화제의 분양현장',
'책속의 이 한줄','토요이슈','인물동정','토요기획','토요판 커버스토리','Money&Life','기업&CEO','짧은 소설','Economic Review','신나는 공부',
'Best of Best','이슈&뷰스','오늘과 내일','고미석의 詩로 여는 주말','Feeling','사이버대학','이 사람이 읽는 법','VISIT JAPAN!',
'톡투 건강 핫클릭','한국에서살아보니','아하! 질병이야기','뉴리더','e-코리아로 가는길','징검다리','방송','전시']


def donga_new(donga):
    df = donga.drop([donga.columns[0]], axis=1)
    df = df.drop_duplicates(['0'])

    df_result = pd.DataFrame()

    for i in stoplist:
        result = df[df['0'].str.contains(i,na=False)]
        df_result = pd.concat([df_result,result])
    
    df = pd.merge(df,df_result, how='outer', indicator=True)
    df = df.query('_merge == "left_only"').drop(columns=['_merge'])
    df['date'] = df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y-%m-%d'))
    df = df.rename(columns={'0':'title'})
    df['company'] = 'donga'
    return df

df_d = donga_new(donga)
    
