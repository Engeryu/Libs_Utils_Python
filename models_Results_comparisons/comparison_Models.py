# 1.4.4 Fonction de répartition des résultats sur tableau de donnée :
def create_comparison_table(results):
    comparison_df = pd.DataFrame(results).dropna(axis=1, how='all')
    float_cols = [col for col in comparison_df.columns if comparison_df[col].dtype == 'float']
    comparison_df[float_cols] = comparison_df[float_cols].round(2)

    error_cols = [col for col in comparison_df.columns if col not in ['Modèle', 'n_neighbors', 'alpha', 'Temps d\'exécution (secondes)']]
    sort_by = error_cols[0]
    
    if sort_by == 'Accuracy':
        comparison_df.sort_values(by=sort_by, ascending=False, inplace=True)
        best_model_index = comparison_df[sort_by].idxmax()
    else:
        comparison_df.sort_values(by=sort_by, inplace=True)
        best_model_index = comparison_df[sort_by].idxmin()
    
    pd.options.display.float_format = '{:.2f}'.format
    best_model = comparison_df.loc[best_model_index, 'Modèle']
    print(f'Le meilleur modèle est {best_model} avec un score {sort_by} de {comparison_df.loc[best_model_index, sort_by]:.2f}%')    
    return best_model, comparison_df