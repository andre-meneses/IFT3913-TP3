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

def plot_boxplot(data, column_name):
    sns.set_theme(style="whitegrid")  # Choix du thème Seaborn
    plt.figure(figsize=(10, 6))  # Ajustement de la taille du graphique
    sns.boxplot(x=data[column_name], palette="Set2")  # Utilisation d'une palette de couleurs
    plt.title(f'Boîte à moustaches de {column_name}', fontsize=14)
    plt.xlabel('Valeurs', fontsize=12)
    plt.ylabel('Distribution', fontsize=12)
    plt.savefig(f'figures/{column_name}_boite_a_moustaches.pdf', dpi=300)  # Sauvegarde en haute qualité
    plt.show()

def plot_scatterplot(data, column1, column2):
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=column1, y=column2, palette="Set2")
    plt.title(f'Nuage de points entre {column1} et {column2}', fontsize=14)
    plt.xlabel(column1, fontsize=12)
    plt.ylabel(column2, fontsize=12)
    plt.savefig(f'figures/{column1}_vs_{column2}_nuage_de_points.pdf', dpi=300)
    plt.show()

def save_statistics(stats, file_name):
    stats_df = pd.DataFrame()
    for metric, values in stats.items():
        temp_df = pd.DataFrame.from_dict(values, orient='index').T  # Transpose to make values as rows
        temp_df.insert(0, 'Métrique', metric)  # Insert 'metrique' as the first column
        stats_df = pd.concat([stats_df, temp_df], ignore_index=True)
    stats_df.to_csv(file_name, index=False)

def main():
    file_path = 'jfreechart-test-stats.csv'  
    data = load_data(file_path)

    stats = {}
    for column in data.columns:
        # plot_boxplot(data, column)
        stats[column] = calculate_stats(data[column])

    plot_scatterplot(data, 'TLOC', 'TASSERT')
    plot_scatterplot(data, 'WMC', 'TASSERT')

    save_statistics(stats, 'statistiques_metriques.csv')
    print("Boîtes à moustaches créées et statistiques sauvegardées.")

if __name__ == "__main__":
    main()


