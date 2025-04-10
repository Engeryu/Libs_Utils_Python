# 1.4.2. Fonction d'execution des différents modèles de regression/classification et d'évaluation des résultats sur tableau de donnée :
def train_and_evaluate_models(models, model_names, X_train, y_train, X_test, y_test, n_neighbors_values, alpha_values):
    if isinstance(y_test.dtype, pd.api.types.CategoricalDtype):
        results = {'Modèle': [], 'n_neighbors': [], 'alpha': [], 'Temps d\'exécution (secondes)': [], 'Accuracy': []}
    else:
        results = {'Modèle': [], 'n_neighbors': [], 'alpha': [], 'Temps d\'exécution (secondes)': [], 'MAPE': []}
    trained_models = {}
    y_preds = {}
    hyperparam_index = 0
    for model, model_name in zip(models,model_names):
        y_preds[model_name] = []
        if isinstance(model,knnR):
            if n_neighbors_values is not None:
                for n_neighbors in n_neighbors_values:
                    model.set_params(n_neighbors=n_neighbors)
                    start_time = time.time()
                    y_pred = evaluate_model(model,X_train,y_train,X_test)
                    end_time = time.time()
                    record_results(model,results,y_test,y_pred,start_time,end_time,n_neighbors=n_neighbors)
                    y_preds[model_name].append(y_pred)
                    hyperparam_index += 1
        elif isinstance(model,l1):
            if alpha_values is not None:
                for alpha in alpha_values:
                    model.set_params(alpha=alpha)
                    start_time = time.time()
                    y_pred = evaluate_model(model,X_train,y_train,X_test)
                    end_time = time.time()
                    record_results(model,results,y_test,y_pred,start_time,end_time,alpha=alpha)
                    y_preds[model_name].append(y_pred)
                    hyperparam_index += 1
        elif isinstance(model,l2):
            if alpha_values is not None:
                for alpha in alpha_values:
                    model.set_params(alpha=alpha)
                    start_time = time.time()
                    y_pred = evaluate_model(model,X_train,y_train,X_test)
                    end_time = time.time()
                    record_results(model,results,y_test,y_pred,start_time,end_time,alpha=alpha)
                    y_preds[model_name].append(y_pred)
                    hyperparam_index += 1
        else:
            start_time = time.time()
            y_pred = evaluate_model(model,X_train,y_train,X_test)
            end_time = time.time()
            record_results(model,results,y_test,y_pred,start_time,end_time)
            y_preds[model_name].append(y_pred)
        trained_models[model_name] = model
    return results, trained_models, y_preds