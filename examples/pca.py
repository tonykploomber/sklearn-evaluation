from sklearn_evaluation import plot
from sklearn.datasets import load_iris as load_data

X, y = load_data(return_X_y=True)
plot.pca(X, y, n_components=3, target_names=["Setosa", "Versicolor", "Virginica"])
