import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일을 읽어들입니다. 파일명은 적절히 수정해주세요.
file_name = 'cox-violent-parsed_filt_usable.csv'
data = pd.read_csv(file_name)

# 'sex' 컬럼을 기준으로 행의 개수를 세어줍니다.
sex_counts = data['sex'].value_counts()

# 바형 그래프로 시각화합니다.
sex_counts.plot(kind='bar')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.title('Number of Rows by Sex')
plt.show()
