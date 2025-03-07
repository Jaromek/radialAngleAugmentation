import seaborn as sns

def plot_data(data_standard_x, data_standard_y, data_augmented_x, data_augmented_y):
    sns.scatterplot(x=data_augmented_x[:,0], y=data_augmented_x[:,1], hue=data_augmented_y, palette='dark', legend=False)
    sns.scatterplot(x=data_standard_x[:,0], y=data_standard_x[:,1], hue=data_standard_y, legend=False)

