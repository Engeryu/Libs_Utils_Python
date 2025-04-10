import numpy as np
def descriptive_stats(df, column, value=None):
    values = df[column].values
    # Calculer le nombre de valeurs
    count = len(values)
    # Calculer la somme des valeurs
    total = np.sum(values)
    # Calculer la moyenne
    mean = total / count
    # Calculer l'écart type
    std = np.sqrt(sum((values - mean) ** 2) / count)
    # Calculer les percentiles
    percentile_25 = np.percentile(values, 25)
    percentile_50 = np.percentile(values, 50)
    percentile_75 = np.percentile(values, 75)
    IQr = percentile_75 - percentile_25
    lower = percentile_25 - 1.5 * IQr
    lower_values = values[values <= lower]
    lower_whisker = np.max(lower_values) if lower_values.size > 0 else np.min(values)
    upper = percentile_75 + 1.5 * IQr
    upper_values = values[values >= upper]
    upper_whisker = np.min(upper_values) if upper_values.size > 0 else np.max(values)
    # Calculer le minimum et le maximum
    min_value = np.min(values)
    max_value = np.max(values)
    # Créer un dictionnaire avec les résultats
    stats = {
        'count': count,
        'total': total,
        'min': min_value,
        'max': max_value,
        'mean': mean,
        'std': std,
        '25%': percentile_25,
        '50%': percentile_50,
        '75%': percentile_75,
        'lower_fence': lower,
        'lower_whisker': lower_whisker,
        'upper_fence': upper,
        'upper_whisker': upper_whisker,
        'interquartile_deviation': round(IQr, 2)
    }
    return stats


