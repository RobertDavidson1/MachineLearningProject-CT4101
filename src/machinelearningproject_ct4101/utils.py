import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_distribution(df,type, nrows, ncols, suptitle, columns):
    """
    Helps plot features during data 
    """

    # Create subplots with nrows and n cols
    fig, axs = plt.subplots(nrows, ncols, figsize=(22,5))

    # Iterate over the columns and plot each in a subplot 
    for i in range(nrows):
        for j in range(ncols):
            idx = (i * ncols) + j
            colName = columns[idx]

            if type=="hist":
                sns.histplot(df, x=colName, ax=axs[i,j])
            elif type=="counts":
                sns.countplot(df,x=colName,ax=axs[i, j], stat='proportion')
            elif type=="boxplot":
                sns.boxplot(df,x=colName, ax=axs[i, j])


            axs[i,j].set_title(colName)
            axs[i,j].set_ylabel('count')
    
    plt.suptitle(suptitle, fontsize=14)
    plt.tight_layout()
    plt.show()


def save_splits(splits_dir, X_train, X_test, X_val, y_train, y_test, y_val):
    """
    Saves processed splits
    """
    X_train.to_csv(f"{splits_dir}/X_train.csv", index=False)
    X_test.to_csv(f"{splits_dir}/X_test.csv", index=False)
    X_val.to_csv(f"{splits_dir}/X_val.csv", index=False)

    y_train.to_csv(f"{splits_dir}/y_train.csv", index=False)
    y_test.to_csv(f"{splits_dir}/y_test.csv", index=False)
    y_val.to_csv(f"{splits_dir}/y_val.csv", index=False)


def load_splits(splits_dir):
    """
    Loads processed splits
    """
    X_train = pd.read_csv(f"{splits_dir}/X_train.csv")
    X_test = pd.read_csv(f"{splits_dir}/X_test.csv")
    X_val = pd.read_csv(f"{splits_dir}/X_val.csv")

    y_train = pd.read_csv(f"{splits_dir}/y_train.csv")["Revenue"]
    y_test = pd.read_csv(f"{splits_dir}/y_test.csv")["Revenue"]
    y_val = pd.read_csv(f"{splits_dir}/y_val.csv")["Revenue"]

    return X_train, X_test, X_val, y_train, y_test, y_val