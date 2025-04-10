def convert_columns_inplace(df, conversions):
    for col, new_type in conversions.items():
        if col in df.columns:  # Vérifiez si la colonne existe
            if new_type == "ordinal":
                df[col] = df[col].apply(lambda date: np.uint32(date.toordinal()))
            elif new_type == "category":
                df[col] = df[col].astype(CategoricalDtype())
            else:
                df[col] = df[col].astype(new_type)