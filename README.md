# Predicción de abandono de clientes (churn) en telecomunicaciones

> **English summary.** Exploratory analysis and two classification models (logistic regression and random forest) to predict customer churn in a telecom dataset of 3,333 customers, 14.5 % of whom churned. On a single stratified 80/20 split, the random forest reaches a recall of 0.62 and a precision of 0.82 on the churn class. There is no cross-validation or threshold tuning yet, so these figures are a first estimate.

## Qué hace

El notebook `notebooks/01_eda.ipynb`:

1. explora el dataset: distribución del churn, correlaciones y diferencias entre clientes que abandonan y los que no;
2. separa los datos en entrenamiento y prueba (80/20, estratificado, semilla 42);
3. entrena una regresión logística (con variables estandarizadas) y un random forest (200 árboles, profundidad máxima 8);
4. compara ambos modelos con accuracy, precision, recall, F1 y ROC-AUC, y revisa la importancia de variables.

## Resultados

Métricas sobre el conjunto de prueba (667 clientes, 97 con churn), tomadas de las salidas guardadas en el notebook:

| Modelo | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| Regresión logística | 0,858 | 0,526 | 0,206 | 0,296 | 0,809 |
| Random forest | 0,925 | 0,822 | 0,619 | 0,706 | 0,865 |

Cómo leerlas:

- **El accuracy solo no dice mucho.** El 85,5 % de los clientes de prueba no abandona, así que un modelo que predijera "nadie abandona" tendría un accuracy de 0,855. La regresión logística (0,858) apenas lo supera y detecta solo el 21 % de los abandonos.
- **El random forest detecta el 62 % de los clientes que abandonan**, y el 82 % de sus alertas son correctas.
- Las variables con más peso en el random forest son los minutos diurnos, el cargo mensual y las llamadas a servicio al cliente.

## Limitaciones

- Una sola partición de entrenamiento y prueba: las métricas pueden variar con otra semilla. Falta validación cruzada.
- No hay un modelo base explícito en el notebook, ni ajuste de hiperparámetros o del umbral de decisión.
- No se traduce el resultado a costo o beneficio de una campaña de retención.
- El dataset no trae fechas, por lo que no se puede validar el modelo sobre un periodo posterior.

## Cómo reproducirlo

1. Descarga `telecom_churn.csv` desde Kaggle ([Customer Churn](https://www.kaggle.com/datasets/barun2104/telecom-churn)) y guárdalo en `data/`.
2. Ejecuta:

```bash
pip install -r requirements.txt
python scripts/check_data.py
jupyter nbconvert --to notebook --execute --inplace notebooks/01_eda.ipynb
```

`check_data.py` confirma que el archivo tiene las 3.333 filas y 11 columnas esperadas.

## Datos

3.333 clientes y 11 variables numéricas: `Churn` (variable objetivo), `AccountWeeks`, `ContractRenewal`, `DataPlan`, `DataUsage`, `CustServCalls`, `DayMins`, `DayCalls`, `MonthlyCharge`, `OverageFee` y `RoamMins`. No tiene valores nulos. El archivo no se versiona en este repositorio.

## Estructura

```
data/                 aquí va telecom_churn.csv (no versionado)
notebooks/
  01_eda.ipynb        análisis exploratorio y modelos
scripts/
  check_data.py       verifica que el dataset esté y tenga la forma esperada
requirements.txt
```

## Stack

Python, pandas, scikit-learn, matplotlib y seaborn.
