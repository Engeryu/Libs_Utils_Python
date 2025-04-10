# 1.2. Fonction créant un nouveau tableau de donnée à partir d'un jeu de donnée (par les optionnels choix de trie selon des colonnes spécifiques, l'extraction de colonnes, ou de groupement) :
def data_filtering(df_name, nom_csv=None, filters=None, data_columns=None, group_by=None, aggregation=None):
    # Générer et afficher une phrase contenant les arguments et les paramètres passés à la fonction
    text = f'Appel de la fonction data_filtering avec les arguments suivants :\n'
    text += f'    nom_csv: {nom_csv}\n'
    if filters:
        text += f'    filters: {filters}\n'
    if data_columns:
        text += f'    data_columns: {data_columns}\n'
    if group_by:
        text += f'    group_by: {group_by}\n'
    text += f'    aggregation: {aggregation}\n'

    # Filtrer le DataFrame en fonction des valeurs choisies pour 'filters'
    if filters:
        query_parts = []
        query_params = {}
        for i, (col, val) in enumerate(filters.items()):
            param_name = f'val_{i}'
            if isinstance(val, list):
                query_parts.append(f'{col} in @{param_name}')
            else:
                query_parts.append(f'{col} == @{param_name}')
            query_params[param_name] = val
        query_string = ' & '.join(query_parts)
        filtered_df = df_name.query(query_string, local_dict=query_params)
    else:
        filtered_df = df_name.copy()

    # Extraire les colonnes spécifiées
    if data_columns is not None:
        filtered_df = filtered_df[data_columns]

    # Regrouper les données par la colonne spécifiée
    if group_by is not None:
        if aggregation == 'mean':
            filtered_df = filtered_df.groupby(group_by).mean(numeric_only=True)
        elif aggregation == 'median':
            filtered_df = filtered_df.groupby(group_by).median(numeric_only=True)


    print(text)  # Afficher le texte généré
    return filtered_df