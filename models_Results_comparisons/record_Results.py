# 1.4.3 Fonction de sauvegarde des résultats et du score de modèle :
def record_results(model, results, y_test, y_pred, start_time, end_time, n_neighbors=None, alpha=None):
    execution_time = end_time - start_time
    if isinstance(y_test.dtype, pd.api.types.CategoricalDtype):
        error = accuracy_score(y_test, y_pred)
        error_name = 'Accuracy'
    else:
        error = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
        error_name = 'MAPE'
    results['Modèle'].append(model.__class__.__name__)
    results['n_neighbors'].append(n_neighbors)
    results['alpha'].append(alpha)
    results['Temps d\'exécution (secondes)'].append(execution_time)
    results[error_name].append(error)