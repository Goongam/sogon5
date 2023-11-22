import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일을 읽어옵니다. 파일 경로를 적절히 수정하세요.
file_path = 'cox-violent-parsed_filt_usable.csv'
data = pd.read_csv(file_path)

# 나이(age) 컬럼을 기준으로 행의 개수를 구합니다.
age_counts = data['age'].value_counts()

# 바 형태의 그래프를 그립니다.
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
age_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Age')  # x축 라벨
plt.ylabel('Number of Rows')  # y축 라벨
plt.title('Number of Rows per Age Group')  # 그래프 제목
plt.xticks(rotation=45)  # x축 라벨 회전
plt.grid(axis='y', linestyle='--', alpha=0.7)  # 그리드 표시
plt.tight_layout()  # 레이아웃 조정
plt.show()
