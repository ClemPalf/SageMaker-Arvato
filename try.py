import numpy as np
import pandas as pd
import os
import time
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


# ANOTHER WAY TO INVESTIGATE A CLUSTER COMPOSITION

def explain_cluster(kmeans_model, cluster_no, data, pca_model, num_components=2, num_feat_per_comp=3):
    
    weights = kmeans_model.cluster_centers_[cluster_no]
    components = list(range(len(weights)))
    
    cluster_expl = pd.DataFrame({"Weights":weights, "Component":components})
    cluster_expl.sort_values("Weights", ascending=False, inplace=True, ignore_index=True)

    comps = []
    weights = []
    comp_infos = []
    for index, row in cluster_expl.head(n=num_components).iterrows():
        
        #plot_feature_weights(features, components, dimension, n_weights = 3, figsize=(7,8)):
        #    plot_feature_weights(azdias.columns.values, pca_175.components_, dimension=0)
        component_info = plot_feature_weights(data.columns.values, pca_model.components_, int(row["Component"]))
        comp_infos.append(component_info)
        comps += [int(row["Component"])] * len(component_info)
        weights +=  [row["Weights"]] * len(component_info)
        
    component_info = pd.concat(comp_infos, ignore_index=True)
    component_info.insert(0, "ComponentWeight", pd.Series(weights))
    component_info.insert(0, "Component", pd.Series(comps))
        
    return component_info

cluster_0 = explain_cluster(kmeans, 3, azdias, pca_175)
cluster_0