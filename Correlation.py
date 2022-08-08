import pandas as pd
url = https://www.kaggle.com/datasets/ruchi798/movies-on-netflix-prime-video-hulu-and-disney?resource=download
movies = pd.read_csv(url)
movies['Rotten Tomatoes'] = movies["Rotten Tomatoes"].str.replace("%", "").astype(float)
movies.drop("Type", inplace=True, axis=1)
correlations = movies.corr(method='pearson')
# Correlation Between All The Features
print(correlations)
# Correlation Between A Particular column "Year"
print(correlations["Year"])
# Visualizing Correlation
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(correlations)
plt.show()
