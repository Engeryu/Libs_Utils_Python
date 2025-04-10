# 1.4.1. Fonction de préparation à la prédiction, de la visualisation graphique et des résultats :
def evaluate_model(model, X_train, y_train, X_test):
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    return y_pred