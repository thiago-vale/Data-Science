import yaml
import numpy as np
import shap
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


def load_config(path="./config/config.yml"):
    """Simple function to load the yaml configuration file

    Args:
        path (str, optional): Path to the yaml file. Defaults to "./config/config.yml".

    Returns:
        dict: Dictionary loaded from yaml file
    """
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return config


def iqr(df):
    """Function that receives a column DF and return the lower bound,
    upper bound and the percentage of data outside these bounds

    Args:
        df (pd.DataFrame): Column dataframe

    Returns:
        float: lower_bound, minimum acceptable value
        float: upper_bound, maximum acceptable value
        float pct_outliers, pct of outliers detected by this method
    """
    q1, q3 = df.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    pct_outliers = len(
        df.loc[(~df.isnull()) & (~df.between(lower_bound, upper_bound))]
    ) / len(~df.isnull())
    return lower_bound, upper_bound, round(pct_outliers, 2)


def percentiles(df, percentile_level=0.01):
    """Function that receives a column dataframe and returns the lower bound
    upper bound and percentage of data outside these bounds

    Args:
        df (pd.DataFrame): column dataframe
        percentile_level (float, optional): percentile to be used. Defaults to 0.01.

    Returns:
        float: lower_bound, minimum acceptable value
        float: upper_bound, maximum acceptable value
        float pct_outliers, pct of outliers detected by this method
    """
    lower_bound, upper_bound = df.quantile([percentile_level, 1 - percentile_level])
    pct_outliers = len(
        df.loc[(~df.isnull()) & (~df.between(lower_bound, upper_bound))]
    ) / len(~df.isnull())
    return lower_bound, upper_bound, round(pct_outliers, 2)


def mape(y_test, y_pred):
    """Function that calculates MAPE (mean absolute percentage error)

    Args:
        y_test (np.array): Actual values
        y_pred (np.array): Predicted values

    Returns:
        float: mape value
    """
    return np.mean(np.abs(y_test - y_pred) / y_test)


def create_summary(y_test, y_pred, shap_values, feature_importance):
    """Function that creates a model summary plot

    Args:
        y_test (np.array): Actual values
        y_pred (np.array): Predicted values
        shap_values (np.array): shap values for explainability
        feature_importance (pd.DataFrame): Feature importance dataframe

    Returns:
        plt.figure: Figure with summary plots
    """
    residuals = y_test - y_pred
    fig = plt.figure()
    fig.add_subplot(2, 2, 1)
    sns.histplot(residuals, kde=True)
    plt.axvline(x=0, linestyle=":", c="r")
    plt.title(
        f"Residuals avg: {np.mean(residuals):.2f} ({np.mean(residuals/y_test)*100:.2f} %)"
    )
    fig.add_subplot(2, 2, 2)
    sns.scatterplot(y=residuals, x=range(len(residuals)), alpha=0.25)
    plt.axhline(y=0, linestyle=":", c="r")
    plt.title("Residuals scatterplot")
    fig.add_subplot(2, 2, 3)
    shap.plots.beeswarm(shap_values, show=False)
    plt.title("Shap plot")
    fig.add_subplot(2, 2, 4)
    sns.barplot(data=feature_importance, y="Feature Id", x="Importances", color="b")
    plt.title("Feature importance")
    fig.set_figheight(10)
    fig.set_figwidth(15)
    plt.tight_layout()
    return fig