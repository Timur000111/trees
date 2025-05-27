import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Сгенерируем фейковые зарплаты
np.random.seed(0)
salaries = np.random.normal(loc=60000, scale=15000, size=1000)  # Средняя 60к, разброс 15к

# Поместим в DataFrame
df = pd.DataFrame({'salary': salaries})

# 📊 Основная статистика
print("Средняя зарплата:", round(df['salary'].mean(), 2))
print("Медианная зарплата:", round(df['salary'].median(), 2))
print("Стандартное отклонение:", round(df['salary'].std(), 2))
print("Дисперсия:", round(df['salary'].var(), 2))

# 📈 Построим гистограмму
plt.hist(df['salary'], bins=30, color='skyblue', edgecolor='black')
plt.axvline(df['salary'].mean(), color='red', linestyle='dashed', linewidth=1, label='Среднее')
plt.axvline(df['salary'].median(), color='green', linestyle='dotted', linewidth=1, label='Медиана')
plt.title('Распределение зарплат')
plt.xlabel('Зарплата')
plt.ylabel('Количество сотрудников')
plt.legend()
plt.show()
