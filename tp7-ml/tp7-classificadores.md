# TP7 - IA

# PARTE A

## Matriz de confusión para el clasificador aleatorio

| Prediction | Reference |     |
|------------|-----------|-----|
|            | 0         | 1   |
| 0          | 2910      | 344 |
| 1          | 2759      | 369 |

|                        |                  |
|-----------------------:|-----------------:|
|               Accuracy |           0.5138 |
|                 95% CI | (0.5014, 0.5261) |
|    No Information Rate |           0.8883 |
|   P-Value [Acc \> NIR] |                1 |
|                  Kappa |           0.0124 |
| Mcnemar's Test P-Value |          \<2e-16 |
|            Sensitivity |           0.5133 |
|            Specificity |           0.5175 |
|         Pos Pred Value |           0.8943 |
|         Neg Pred Value |           0.1180 |
|             Prevalence |           0.8883 |
|         Detection Rate |           0.4560 |
|   Detection Prevalence |           0.5099 |
|      Balanced Accuracy |           0.5154 |

## Matriz de confusión para el clasificador por clase mayoritaria

| Prediction | Reference |     |
|------------|----------:|----:|
|            |         0 |   1 |
| 0          |      5669 | 713 |
| 1          |         0 |   0 |

|                        |                  |
|-----------------------:|-----------------:|
|               Accuracy |           0.8883 |
|                 95% CI | (0.8803, 0.8959) |
|    No Information Rate |           0.8883 |
|   P-Value [Acc \> NIR] |             0.51 |
|                  Kappa |                0 |
| Mcnemar's Test P-Value |          \<2e-16 |
|            Sensitivity |           1.0000 |
|            Specificity |           0.0000 |
|         Pos Pred Value |           0.8883 |
|         Neg Pred Value |              NaN |
|             Prevalence |           0.8883 |
|         Detection Rate |           0.8883 |
|   Detection Prevalence |           1.0000 |
|      Balanced Accuracy |           0.5000 |
