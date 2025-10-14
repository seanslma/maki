# Hyper Parameters

## Bayesian Optimization
- https://xgboosting.com/bayesian-optimization-of-xgboost-hyperparameters-with-bayes_opt/
- https://www.kaggle.com/code/somang1418/tuning-hyperparameters-under-10-minutes-lgbm
- https://www.analyticsvidhya.com/blog/2021/05/bayesian-optimization-bayes_opt-or-hyperopt/

packages:
- bayes_opt [bayesian-optimization]
- hyperopt
- skopt [scikit-optimize]

## example code
```py
t0 = time()
from bayes_opt import BayesianOptimization
def lgb_hyper_opt_bayes(
    X_train, y_train, init_round=5, opt_round=10, n_folds=5, n_estimators=10000, random_seed=13
):
    # prepare data
    train_set = lgb.Dataset(data=X_train, label=y_train, free_raw_data=False)
    
    # parameters
    def lgb_eval(
        learning_rate, 
        num_leaves, 
        max_depth, 
        min_data_in_leaf, 
        feature_fraction, 
        bagging_fraction, 
        bagging_freq, 
        lambda_l1,
        lambda_l2,
    ):
        params = {
            'objective':'regression', 
            'metric':'mae',
            'verbosity': -1,  # suppress all output [-1, 0, 1, 2]
            'force_col_wise': True, # only for cpu
            'learning_rate': max(min(learning_rate, 1), 0),
            'num_leaves': int(round(num_leaves)),
            'max_depth': int(round(max_depth)),
            'min_data_in_leaf': int(round(min_data_in_leaf)),
            'feature_fraction': max(min(feature_fraction, 1), 0),
            'bagging_fraction': max(min(bagging_fraction, 1), 0),
            'bagging_freq': int(round(bagging_freq)),
            'lambda_l1': max(lambda_l1, 0),
            'lambda_l2': max(lambda_l2, 0),
        }

        lgb_cv = lgb.cv(
            params=params, 
            train_set=train_set, 
            metrics=['l1'], 
            num_boost_round=n_estimators,
            nfold=n_folds, 
            stratified=False, 
            shuffle=False, 
            seed=random_seed, 
            callbacks=[
                lgb.early_stopping(stopping_rounds=100, verbose=False), # verbose: log message with early stopping information
                lgb.log_evaluation(500), # output every 500 boosts
            ],
        )
        # negative because we are minimizing
        return -min(lgb_cv['valid l1-mean'])
        
    pbounds = {
        'learning_rate': (0.001, 0.2),
        'num_leaves': (10, 100),
        'max_depth': (15, 100),  
        'min_data_in_leaf': (10, 200),
        'feature_fraction': (0.1, 1),
        'bagging_fraction': (0.8, 1),
        'bagging_freq': (0, 10),
        'lambda_l1': (0, 10),
        'lambda_l2': (0, 10),
    }   
    lgb_bo = BayesianOptimization(
        f=lgb_eval, 
        pbounds=pbounds,
        random_state=200,
    )

    #init_points (5-20): How many steps of random exploration you want to perform. Random exploration can help by diversifying the exploration space.
    #n_iter (20-100): How many steps of bayesian optimization you want to perform. The more steps the more likely to find a good maximum you are.
    lgb_bo.maximize(init_points=init_round, n_iter=opt_round)

    # extracting the best result (highest -MAE is the best)
    best_params = lgb_bo.max['params']
    best_score = lgb_bo.max['target']
    return best_params, best_score

opt_params, opt_score = lgb_hyper_opt_bayes(X_train, y_train, init_round=5, opt_round=10, n_folds=5, n_estimators=10000, random_seed=13)
print(f'hyper opt time: {time() - t0:.3f} seconds')
print(opt_score)
print(opt_params)
```
