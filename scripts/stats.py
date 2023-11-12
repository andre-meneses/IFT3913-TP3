import pandas as pd
import numpy as np
from scipy.stats import shapiro, pearsonr, spearmanr
import statsmodels.api as sm
from statsmodels.regression.linear_model import RegressionResultsWrapper
import matplotlib.pyplot as plt

def test_normality(data):
    stat, p = shapiro(data)
    return p > 0.05  # Returns True if data is normally distributed

def compute_correlation(x, y, normal):
    if normal:
        return pearsonr(x, y)[0]  # Pearson correlation
    else:
        return spearmanr(x, y)[0]  # Spearman rank correlation

def linear_regression(x, y):
    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    result = model.fit()
    return result.params


if __name__=="__main__":

    df = pd.read_csv('data/jfreechart-test-stats.csv').iloc[:,1:]

    # Test for normality
    normality_results = {col: test_normality(df[col]) for col in df.columns}

    # Compute correlations
    correlation_tloc_tassert = compute_correlation(df['TLOC'], df['TASSERT'], normality_results['TLOC'] and normality_results['TASSERT'])
    correlation_wmc_tassert = compute_correlation(df['WMC'], df['TASSERT'], normality_results['WMC'] and normality_results['TASSERT'])

    # Linear regression
    lr_tloc_tassert = linear_regression(df['TLOC'], df['TASSERT'])
    lr_wmc_tassert = linear_regression(df['WMC'], df['TASSERT'])


    plt.figure(figsize=(12, 6))

    # TLOC x TASSERT
    plt.subplot(1, 2, 1)
    plt.scatter(df['TLOC'], df['TASSERT'], color='blue')
    plt.plot(df['TLOC'], lr_tloc_tassert[0] + lr_tloc_tassert[1] * df['TLOC'], color='red')
    plt.title('Régression Lineaire: TLOC x TASSERT')
    plt.xlabel('TLOC')
    plt.ylabel('TASSERT')

    # WMC x TASSERT
    plt.subplot(1, 2, 2)
    plt.scatter(df['WMC'], df['TASSERT'], color='green')
    plt.plot(df['WMC'], lr_wmc_tassert[0] + lr_wmc_tassert[1] * df['WMC'], color='red')
    plt.title('Régression Lineaire: WMC x TASSERT')
    plt.xlabel('WMC')
    plt.ylabel('TASSERT')

    plt.tight_layout()
    plt.savefig('figures/regression.pdf', dpi=300)
    plt.show()

    print("Parametres Régression Lineaire TLOC x TASSERT:", lr_tloc_tassert)
    print("Parametres Régression Lineaire WMC x TASSERT:", lr_wmc_tassert)

    # Save results to CSV
    pd.DataFrame.from_dict(normality_results, orient='index', columns=['Normal Distribution']).to_csv('output/normality_test_results.csv')
    correlation_results = pd.DataFrame({
        'Correlation': ['TLOC x TASSERT', 'WMC x TASSERT'],
        'Coefficient': [correlation_tloc_tassert, correlation_wmc_tassert]
    })
    correlation_results.to_csv('output/correlation_coefficients.csv', index=False)

    print("Analysis complete. Results saved to CSV files.")

