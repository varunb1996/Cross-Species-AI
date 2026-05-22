import umap
import hdbscan

def cluster_embeddings(embeddings):

    reducer = umap.UMAP()

    reduced = reducer.fit_transform(
        embeddings
    )

    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=5
    )

    labels = clusterer.fit_predict(
        reduced
    )

    return reduced, labels