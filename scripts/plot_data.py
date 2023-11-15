import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    data = pd.read_csv(file_path)
    data = data.iloc[:, 1:]  # Sélection des colonnes
    return data

def calculate_stats(column):
    quartiles = column.quantile([0.25, 0.5, 0.75])
    min_value = column.min()
    outliers = column[(column < quartiles[0.25] - 1.5 * (quartiles[0.75] - quartiles[0.25])) |
                      (column > quartiles[0.75] + 1.5 * (quartiles[0.75] - quartiles[0.25]))]
    return {
        'Médiane': quartiles[0.5],
        'Quartile Inférieur': quartiles[0.25],
        'Quartile Supérieur': quartiles[0.75],
        'Longueur': quartiles[0.75] - quartiles[0.25],
        'Limite Supérieure': quartiles[0.75] + 1.5 * (quartiles[0.75] - quartiles[0.25]),
        'Limite Inférieure': max(quartiles[0.25] - 1.5 * (quartiles[0.75] - quartiles[0.25]), min_value),
        'Points extrêmes': ', '.join(map(str, outliers.values))
    }

def plot_scatterplot(data, column1, column2, ax):
    sns.scatterplot(data=data, x=column1, y=column2, color="darkblue", s=50, alpha=0.7, ax=ax)  # Dark color, larger size, and some transparency
    ax.set_facecolor("lightgray")  # Light gray background for contrast
    ax.set_title(f'Nuage de points entre {column1} et {column2}', fontsize=14)
    ax.set_xlabel(column1, fontsize=12)
    ax.set_ylabel(column2, fontsize=12)

def save_statistics(stats, file_name):
    stats_df = pd.DataFrame()
    for metric, values in stats.items():
        temp_df = pd.DataFrame.from_dict(values, orient='index').T  # Transpose to make values as rows
        temp_df.insert(0, 'Métrique', metric)  # Insert 'metrique' as the first column
        stats_df = pd.concat([stats_df, temp_df], ignore_index=True)
    stats_df.to_csv(file_name, index=False)


def plot_boxplot(data, column_name, ax):
    sns.boxplot(x=data[column_name], palette="Set2", ax=ax)  # Draw on the passed axes
    ax.set_title(f'Boîte à moustaches de {column_name}', fontsize=14)
    ax.set_xlabel('Valeurs', fontsize=12)
    ax.set_ylabel('Distribution', fontsize=12)

def main():
    file_path = 'data/jfreechart-test-stats.csv'
    data = load_data(file_path)

    stats = {}
    columns = data.columns
    fig, axs = plt.subplots(3, 1, figsize=(15, 10))  # Create a 2x2 grid of subplots
    axs = axs.flatten()  # Flatten the 2D array of axes

    for i, column in enumerate(columns):
        plot_boxplot(data, column, axs[i])
        stats[column] = calculate_stats(data[column])

    # Adjust layout and save the figure
    plt.tight_layout()
    plt.savefig('figures/all_boxplots.pdf', dpi=300)
    plt.show()

    fig, axs = plt.subplots(1, 2, figsize=(20, 10))  # 1 row, 2 columns

    plot_scatterplot(data, 'TLOC', 'TASSERT', axs[0])
    plot_scatterplot(data, 'WMC', 'TASSERT', axs[1])

    plt.tight_layout()
    plt.savefig('figures/scatterplots_grid.pdf', dpi=300)
    plt.show()

    save_statistics(stats, 'output/statistiques_metriques.csv')
    print("Boîtes à moustaches créées et statistiques sauvegardées.")

if __name__ == "__main__":
    main()

