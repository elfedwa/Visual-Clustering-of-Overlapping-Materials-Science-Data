import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.metrics import silhouette_score

# Load your data
df = pd.read_csv('10bar_DATA.csv')

# Select features for PCA
features = ['PS', 'WS', 'MC', 'UPTAKE', 'QH']
X = df[features]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X)
# Create a list to store the results
results = []
# Apply PCA
for n_components in range(2,11):
    # You can choose the number of principal components
    # pca = PCA(n_components=n_components)
    # principal_components = pca.fit_transform(X_scaled)
    # Apply K-Means clustering on the principal components
    n_clusters = n_components  # Adjust as needed
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df['cluster'] = kmeans.fit_predict(X)

    # Reshape X_scaled to a 2D array
    X_scaled_2d = np.reshape(X, (X.shape[0], -1))
    # Calculate silhouette score using the reshaped X_scaled
    score = silhouette_score(X_scaled_2d, df['cluster'])
    print('Silhouette Score:', score)
    print('Cluster size', 'Silhouette Score', n_components, score)
        # Append the results to the list
    results.append([n_components, score])

    # Print the results
    print('Cluster size:', n_components, 'Silhouette Score:', score)

# Convert the results list to a DataFrame
results_df = pd.DataFrame(results, columns=['Cluster size', 'Silhouette Score'])

# Save the DataFrame to a CSV file
results_df.to_csv('cluster_results.csv', index=False)

print('Results saved to cluster_results.csv')