# 1.1.2 Fonction d'analyze d'un dataframe, de ses lignes et de ses valeurs dupliquées ou vides :
def analyze_dataframe(df, table_name, columns=None, distinct=None):
    # Formatage d'une chaîne de caractère avec condition via opérateur ternaire afin de vérifier et compter les lignes dupliquées et les cellules vides :
    get_info = lambda duplicated_rows, null_cells: (f"il se trouve {duplicated_rows} lignes dupliquées, " if duplicated_rows > 0 else "aucune ligne n'est dupliquée, ") + (f"et il se trouve {null_cells} cellules nulles.\n" if null_cells > 0 else "aucune cellule n'est vide.\n")
    text = f"Dans la table {table_name}, {get_info(sum(df.duplicated()), sum(df.isnull().any()))}"
    # L'argument columns effectue une itération sur chaque colonne spécifié si l'argument est appelé
    if columns is not None:
        for column in columns:
            duplicated_values = sum(df.duplicated(column))
            non_null_duplicated_values = sum(df.duplicated(column) & df[column].notnull())
            null_values = df[column].isnull().sum()
            # Formatage d'une chaîne de caractère avec condition via un opérateur ternaire afin de vérifier et compter les valeurs dupliquées et/ou nulles
            text += f"Dans la colonne {column}, "
            text += f"il se trouve {duplicated_values} valeurs dupliquées, dont {non_null_duplicated_values} valeurs non-nulles.\n" if duplicated_values > 0 else  f"il ne se trouve pas de valeur dupliquée. Le nombre d'articles correspond au nombre de lignes.\n"
            text += f"et {null_values} valeurs nulles.\nIl s'y trouve donc {df[column].nunique()} valeurs distinctes sur {df.shape[0]} lignes.\n" if null_values > 0 and duplicated_values > 0 else ""
    # Retour des valeurs distinctes des colonnes appelées
    if distinct is not None:
        for dist_col in distinct:
            unique_values = df[dist_col].unique()
            unique_values_str = list(map(str, unique_values))
            unique_values_text = ', '.join(unique_values_str)
            text += f"Dans la colonne {dist_col}, il se trouve {df[dist_col].nunique()} valeurs distinctes, que sont : {unique_values_text}.\n"
    print(text)