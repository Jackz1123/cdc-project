import pandas as pd

data = pd.read_csv('Datab.csv')

print(data['Total Shipped'].unique())
data['Total Shipped'] = pd.to_numeric(data['Total Shipped'], errors='coerce')
data.dropna(subset=['Total Shipped'], inplace=True)
developer_shipped = data.groupby('Developer')['Total Shipped'].sum().sort_values(ascending=False)
print(developer_shipped)
total_market_shipped = data['Total Shipped'].sum()
developer_proportion_shipped = developer_shipped / total_market_shipped * 100
import matplotlib.pyplot as plt
import seaborn as sns
import sys
print(sys.path)

# Top N developers by shipped
N = 10
top_developers_shipped = developer_shipped.head(N)

plt.figure(figsize=(12, 8))
sns.barplot(x=top_developers_shipped.values, y=top_developers_shipped.index, palette="viridis")
plt.title('Top {} Developers by Game Shipped'.format(N))
plt.xlabel('Total Shipped')
plt.ylabel('Developer')
plt.show()

avg_shipped_per_game = data.groupby('Developer')['Total Shipped'].mean().sort_values(ascending=False)


