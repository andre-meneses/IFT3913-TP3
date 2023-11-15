import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plot_data

def filter_groups(csv_file):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Create two groups based on the condition TASSERT > 20
    group_greater_than_20 = df[df['TASSERT'] > 20]

    # Create another group based on the condition TASSERT < 20
    group_less_than_20 = df[df['TASSERT'] < 20]

    # Extract relevant columns for each group
    group_gt_20_data = group_greater_than_20[['WMC', 'TLOC']]
    group_lt_20_data = group_less_than_20[['WMC', 'TLOC']]

    return group_lt_20_data,group_gt_20_data

def plot_boxplots(group_lt_20_data, group_gt_20_data):
    # Set up subplots for TLOC
    fig, axes_tloc = plt.subplots(nrows=1, ncols=2, figsize=(12, 6), sharey=True)

    # Boxplot for TLOC in group with TASSERT < 20
    sns.boxplot(x='variable', y='value', data=pd.melt(group_lt_20_data[['TLOC']]), ax=axes_tloc[0])
    axes_tloc[0].set_title('TASSERT < 20 - TLOC')

    # Boxplot for TLOC in group with TASSERT > 20
    sns.boxplot(x='variable', y='value', data=pd.melt(group_gt_20_data[['TLOC']]), ax=axes_tloc[1])
    axes_tloc[1].set_title('TASSERT > 20 - TLOC')

    # Set common labels for TLOC subplot
    fig.suptitle('Boxplots for Metrics Comparison')

    fig.savefig(f'figures/quasi-experience/TLOC_lt_20_vs_gt_20_boite_a_moustaches.pdf', dpi=300)  # Sauvegarde en haute qualité

    # Set up subplots for WMC
    fig_wmc, axes_wmc = plt.subplots(nrows=1, ncols=2, figsize=(12, 6), sharey=True)

    # Boxplot for WMC in group with TASSERT < 20
    sns.boxplot(x='variable', y='value', data=pd.melt(group_lt_20_data[['WMC']]), ax=axes_wmc[0])
    axes_wmc[0].set_title('TASSERT < 20 - WMC')

    # Boxplot for WMC in group with TASSERT > 20
    sns.boxplot(x='variable', y='value', data=pd.melt(group_gt_20_data[['WMC']]), ax=axes_wmc[1])
    axes_wmc[1].set_title('TASSERT > 20 - WMC')

    # Set common labels for WMC subplot
    fig_wmc.suptitle('Boxplots for Metrics Comparison')

    fig_wmc.savefig(f'figures/quasi-experience/WMC_lt_20_vs_gt_20_boite_a_moustaches.pdf', dpi=300)  # Sauvegarde en haute qualité
    # Show the plots
    plt.show()

def main():
    file_path = 'data/jfreechart-test-stats.csv'
    data = filter_groups(file_path)

    stats_lt_20 = {}
    stats_gt_20 = {}
    for column_lt in data[0].columns:
        stats_lt_20[column_lt] = plot_data.calculate_stats(data[0][column_lt])

    for column_gt in data[1].columns:
        stats_gt_20[column_gt] = plot_data.calculate_stats(data[1][column_gt])

    plot_data.save_statistics(stats_lt_20, 'output/quasi-experience/statistiques_lt_20.csv')
    plot_data.save_statistics(stats_gt_20, 'output/quasi-experience/statistiques_gt_20.csv')

    plot_boxplots(data[0], data[1])

if __name__ == "__main__":
    main()