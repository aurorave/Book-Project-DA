import pandas as pd

kyobo_weekly = pd.read_csv(r'C:\Users\maeve\AIB 14\Section6\Codestates Project 2\data\kyobo\all_week_list_202211221714.csv', encoding = 'cp949') # 여기서만 encoding 에러 발생으로 cp949 설정 추가 (참고. https://zephyrus1111.tistory.com/39)
kyobo_monthly = pd.read_csv(r'C:\Users\maeve\AIB 14\Section6\Codestates Project 2\data\kyobo\all_month_list_202211221711.csv')
kyobo_yearly = pd.read_csv(r'C:\Users\maeve\AIB 14\Section6\Codestates Project 2\data\kyobo\all_year_list_202211221713.csv')

def kyobo_dup(df):
    df = df.drop_duplicates(subset = ['기간', '순위', '제목']) # keep = 'first' by default
    
    return df 

kyobo_dup(kyobo_weekly)
kyobo_dup(kyobo_monthly)
kyobo_dup(kyobo_yearly) # 결과 출력 확인
