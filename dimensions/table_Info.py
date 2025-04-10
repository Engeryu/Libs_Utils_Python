# 1.1.1 Fonction retournant les informations principales d'un jeu de donnée (Dimensions, premières lignes, types de données) :
def get_table_info(df, table_name, n=5):
    # Display the dimensions of the table
    print(f"The table {table_name} has {df.shape[1]} column(s) and {df.shape[0]} observation(s) or article(s).\n")
    # Display the first n rows of the DataFrame
    print(f"Here are the first {n} rows of the table {table_name}:")
    display(df.head(n))
    # Display information about the DataFrame
    print(f"Here is the information about the table {table_name}:")
    df.info()