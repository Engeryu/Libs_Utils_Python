# 1.3.1 Fonction de conversion automatique à partir d'un dictionnaire :
def convert_columns(df, conversions):
    common_cols = set(df.columns) & set(conversions.keys())
    # Vérifier que les colonnes spécifiées dans le dictionnaire 'conversions' existent bien dans le DataFrame avant de les convertir
    for col in common_cols:
        if col in df.columns:
            df = df.astype({col: conversions[col]})
    return df