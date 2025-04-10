# 1.3.2. Fonction de conversion des variables d'entraînements :
def prepare_df_model(df, new_df_name, data, dummies):
    new_df = df.copy()
    new_df = new_df[data]
    new_df = pd.get_dummies(new_df, columns=dummies)
    return new_df
