import kagglehub

# Download latest version
path = kagglehub.dataset_download("xavierberge/road-accident-dataset")

print("Path to dataset files:", path)