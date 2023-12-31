# -*- coding: utf-8 -*-
"""Proyecto_Berral.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vscLg5pKfsq44d24YA_KluFAdlNKcNJT

# Rotación de clientes de telecomunicaciones
El dataset elegido contiene informacion sobre una empresa de telecomunicaciones ficticia que proporcionó servicios de Internet y telefonía residencial a 7043 clientes en California. En el mismo se incluyen varios datos acerca de qué clientes se han ido, se han quedado o se han registrado en su servicio. Y además varios datos demográficos importantes para cada cliente.

Se evaluarán estos datos con el objetivo de predecir el comportamiento de los clientes para, de esta manera, retenerlos en la compañía evitando que elijan otras empresas.

**Hipótesis:**

1. Hipótesis 1: ¿Los clientes con contratos a largo plazo tienen una menor tasa de churn que aquellos con contratos mensuales?
   
2. Hipótesis 2: ¿Los clientes que utilizan pagos automáticos tienen una mayor retención en comparación con los que no lo hacen?

3. Hipótesis 3: ¿Existe una relación entre el monto mensual que los clientes pagan y la probabilidad de churn?

4. Hipotesis 4: ¿Qué otros factores, como la edad, el género o la presencia de dependientes, influyen en la retención de clientes?

5. Hipotesis 5: ¿Qué servicios adicionales, como seguridad en línea o soporte técnico, impactan en la retención de clientes?

**Abstracto con Motivación y Audiencia:**

En un mercado altamente competitivo de telecomunicaciones residenciales, retener a los clientes existentes es esencial para el crecimiento y la rentabilidad de la compañía. La alta tasa de churn (abandono) representa un desafío significativo, ya que la pérdida de clientes se traduce directamente en pérdida de ingresos. En este contexto, se llevará a cabo un análisis de datos exhaustivo para comprender los factores que influyen en la decisión de los clientes de quedarse o abandonar la compañía.

Este análisis de datos está dirigido a ejecutivos y profesionales de la industria de telecomunicaciones, así como a equipos de gestión de clientes y analistas de datos interesados en mejorar la retención de clientes. Los resultados y las conclusiones de este análisis proporcionarán información valiosa para la toma de decisiones estratégicas en la retención de clientes y la implementación de estrategias efectivas.

**Definición de Objetivo:**

El objetivo principal es retener a los clientes de la compañía de telecomunicaciones y reducir la tasa de churn (abandono). Se busca comprender qué factores influyen en la decisión de los clientes de quedarse o irse. Para luego poder desarrollar estrategias de retención de clientes basadas en este análisis.

**Contexto Comercial:**

- La compañía de telecomunicaciones proporciona servicios de Internet y telefonía residencial a clientes en California.
- La retención de clientes es crucial para el crecimiento y la estabilidad de la compañía.
- La competencia en la industria es alta, por lo que es importante mantener a los clientes satisfechos y leales.

**Problema Comercial:**

El problema principal es la alta tasa de churn, representa más de 1/4 de los clientes, lo que significa que muchos clientes están abandonando la compañía.
Esto conduce a una pérdida de ingresos y una disminución en la rentabilidad. La compañía necesita identificar qué tipos de clientes son más propensos a abandonar y tomar medidas para retenerlos.

**Contexto Analítico:**

Se tiene un conjunto de datos que contiene información sobre clientes, contratos, pagos, servicios y si han abandonado o no.

Se utilizarán técnicas de análisis de datos y aprendizaje automático para comprender las relaciones y patrones en los datos. El análisis ayudará a identificar factores que contribuyen al churn y a desarrollar estrategias de retención efectivas.

### Importación de librerias
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
ruta_archivo='/content/drive/MyDrive/Data Analysis/Data science/Proyecto/TELCO1.csv'
df= pd.read_csv(ruta_archivo)
df.head()
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

from sklearn import metrics
from sklearn.metrics import roc_curve
from sklearn.metrics import recall_score, confusion_matrix, precision_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, classification_report
from xgboost import XGBClassifier

df.info()

"""## Glosario

Antes de adentrarnos en el dataset, es importante saber a que se refiere cada variable.


- **customerID:** ID del cliente
- **gender:** Género del cliente (Hombre o Mujer)
- **SeniorCitizen:** Si el cliente es un ciudadano jubilado o no (1 para Sí, 0 para No)
- **Partner:** Si el cliente tiene pareja o no (Sí o No)
- **Dependents:** Si el cliente tiene dependientes o no (Sí o No)
- **tenure:** Número de meses que el cliente ha estado con la compañía
- **PhoneService:** Si el cliente tiene servicio de teléfono o no (Sí o No)
- **MultipleLines:** Si el cliente tiene múltiples líneas o no (Sí o No, Sin servicio telefónico)
- **InternetService:** Proveedor de servicios de internet del cliente (DSL, Fibra óptica, No)
- **OnlineSecurity:** Si el cliente tiene seguridad en línea o no (Sí o No, Sin servicio de internet)
- **OnlineBackup:** Si el cliente tiene copia de seguridad en línea o no (Sí o No, Sin servicio de internet)
- **DeviceProtection:** Si el cliente tiene protección de dispositivos o no (Sí o No, Sin servicio de internet)
- **TechSupport:** Si el cliente tiene soporte técnico o no (Sí o No, Sin servicio de internet)
- **StreamingTV:** Si el cliente tiene televisión por streaming o no (Sí o No, Sin servicio de internet)
- **StreamingMovies:** Si el cliente tiene películas por streaming o no (Sí o No, Sin servicio de internet)
- **Contract:** Término del contrato del cliente (Mensual, Anual, Bienal)
- **PaperlessBilling:** Si el cliente tiene facturación electrónica o no (Sí o No)
- **PaymentMethod:** Método de pago del cliente (Cheque electrónico, Cheque por correo, Transferencia bancaria (automática), Tarjeta de crédito (automática))
- **MonthlyCharges:** Cantidad cobrada al cliente mensualmente
- **TotalCharges:** Cantidad total cobrada al cliente
- **Churn:** Si el cliente se dio de baja o no (Sí o No)

##Data Cleaning
"""

df.head()

"""Luego de ver los resultados de df.info, podemos ver que el tipo de dato de la variable Total Charges es Object. Total Charges representa los cargos totales cobrados a un cliente, claramente es una variable numérica, es por esto que debemos convertirla.

Además buscamos si hay valores nulos de esta variable:
"""

## Converir Total Charges en una variable numerica
df['TotalCharges'] = pd.to_numeric(df.TotalCharges, errors='coerce')
df.isnull().sum()

"""Se puede observar que hay 11 valores nulos de Total Charges. Se decidió reemplazar los valores nulos con el valor promedio de esta variable"""

# Rellenar los valores nulos de Total Charges con el valor promedio
df.fillna(df["TotalCharges"].mean())

# Remover Valores nulos
df.dropna(inplace = True)

"""Como se puede ver en el glosario, la variable tenure hace referencia a la cantidad de meses que un cliente está/estuvo en la compañía.

Un valor de tenure=0 es irrelevante para este informe, es por esto que se eliminarán los registros que tengan un tenure nulo.
"""

#Remover tenure igual a 0
df.drop(labels=df[df['tenure'] == 0].index, axis=0, inplace=True)
df[df['tenure'] == 0].index

#Convertir la variable Churn en una variable binaria
df['Churn'].replace(to_replace='Yes', value=1, inplace=True)
df['Churn'].replace(to_replace='No',  value=0, inplace=True)

"""##Visualizaciones

### Churn
"""

Churn_counts = df['Churn'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(Churn_counts, labels=Churn_counts.index, autopct='%1.1f%%', colors=['lightblue', 'grey'])

plt.title('Churn')
plt.tight_layout()
plt.show()

"""Se puede observar que más de 1/4 de los clientes abandonan la compañía.

### Relación entre tipo de contrato y churn
"""

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Contract', hue='Churn', palette=['Lightblue','grey'])

plt.xlabel('Tipo de Contrato')
plt.ylabel('Cantidad de Clientes')
plt.title('Relación entre Tipo de Contrato y Abandono')

plt.xticks(rotation=0)
plt.legend(title='Abandono')
plt.tight_layout()
plt.show()

"""Interpretacion grafico:

Se puede observar en este grafico que los clientes que tienen contratos de 2 años no suelen abandonar a la compañia, lo mismo pasa con los contratos de 1 año. Pero en los contratos mes a mes la diferencia entre los clientes que se quedan y los que se van es considerablemente mas chica que en los otros casos.

### Relación entre método de pago y churn
"""

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='PaymentMethod', hue='Churn', palette=['Lightblue','grey'])

plt.xlabel('Metodo de pago')
plt.ylabel('Cantidad de Clientes')
plt.title('Relación entre metodo de pago y Abandono')

plt.xticks(rotation=0)
plt.legend(title='Abandono')
plt.tight_layout()
plt.show()

"""Interpretacion grafico:

Podemos ver que los cientes que mas se van de la compañia son los que pagan atraves de cheques electronicos. Los otros metodos de pago se comportan de manera muy similar entre ellos.

### Relación entre cargos mensuales y Churn
"""

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Churn', y='MonthlyCharges', palette=['Lightblue','Grey'])

plt.xlabel('Churn')
plt.ylabel('Monto Mensual')
plt.title('Relación entre cargos mensuales y abandono')

plt.xticks([0, 1], ['No', 'Yes'])
plt.tight_layout()
plt.show()

"""Interpretacion grafico:

En este grafico se puede observar que los clientes que abandonan la compañia son en su mayoria aquellos que pagan mas dinero mensualmente.

### Relación entre género y churn
"""

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Churn', hue='gender', palette=['Lightblue','grey'])

plt.xlabel('Abandono')
plt.ylabel('Cantidad de Clientes')
plt.title('Relación entre género y Abandono')

plt.xticks(rotation=0)
plt.legend(title='Género')
plt.tight_layout()
plt.show()

"""Interpretación gráfico:

No se observa una correlación significativa entre genero y abandono

### Relación entre Servicio de internet y churn
"""

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='InternetService', hue='Churn', palette=['Lightblue','grey'])

plt.xlabel('Servicio de internet')
plt.ylabel('Cantidad de Clientes')
plt.title('Relación entre Servicio de Internet y Abandono')

plt.xticks(rotation=0)
plt.legend(title='Abandono')
plt.tight_layout()
plt.show()

"""Interpretación gráfico:

Los clientes que mas abandonan la compañía son aquellos que contrataron el servicio de fibra óptica. Aquellos que no contrataron ningun servicio de internet suelen quedarse en la compañía.

### Relación entre Servicio de seguridad y churn
"""

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='OnlineSecurity', hue='Churn', palette=['Lightblue','grey'])

plt.xlabel('Servicio de Seguridad online')
plt.ylabel('Cantidad de Clientes')
plt.title('Relación entre Servicio de seguridad y Abandono')

plt.xticks(rotation=0)
plt.legend(title='Abandono')
plt.tight_layout()
plt.show()

"""Interpretación gráfico:

Se puede concluir con este gráfico que aquellos que no contratan un servicio de seguridad online son los que más dejan la compañía.

### Conclusiones de visualizaciones

* Debido a que los clientes que mas permanecen en la compañia son aquellos con contratos a más largo plazo, la empresa debería intentar de quela mayoria de sus clientes tengan contratos a 2 años o 1, podría ser ofreciendoles promociones al ingresar con este tipo de contratos. Y además evitar los pagos por medio de cheque elecronico.

* Además debería revisar los servicios de internet que ofrece por medio de la fibra óptica. Los clientes que contratan este servicio son más propensos a abandonar la compañía. Por medio de esta base de datos no se puede conocer la razón.

* En cuanto al monto mensual que pagan los clientes, aquellos que mas pagan mensualmente son los que suelen abanadonar la compañía. La empresa podría evaluar realizarles un descuento a los clientes que más pagan, para mantenerlos por mas tiempo.

## Procesamiento de Data

Para poder aplicar ciertos modelos de machine learning es necesario convertir las variables categóricas en numéricas
"""

# Cambiar las variables que son categoricas a numeros
def object_to_int(dataframe_series):
    if dataframe_series.dtype=='object':
        dataframe_series = LabelEncoder().fit_transform(dataframe_series)
    return dataframe_series
df2 = df
df = df.apply(lambda x: object_to_int(x))
X = df.drop(columns = ['Churn'])
y = df['Churn'].values
df.head()

"""Data para entrenar el modelo y data para testearlo"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=99)

scaler= StandardScaler()

num_cols = ["tenure", 'MonthlyCharges', 'TotalCharges']

X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
X_test[num_cols] = scaler.transform(X_test[num_cols])

"""### Arbol de decision"""

dt_model = DecisionTreeClassifier()
dt_model.fit(X_train,y_train)
predictdt_y = dt_model.predict(X_test)
accuracy_dt = dt_model.score(X_test,y_test)
print("Decision Tree accuracy is :",accuracy_dt)

print(classification_report(y_test, predictdt_y))

"""Evaluacion del modelo

* Con el Arbol de decision la exactitud (Accuracy) del modelo es del 74.4%

* **Recall** =0.52 significa que en esta situación particular fuimos capaces de detectar al 52% de los clientes que abandonaron el servicio. Se esperaba un mejor resultado,  por lo que necesitamos ajustar el modelo.

* **Precision** =0.83 nos indica que cuando nuestro modelo predice a un cliente que abandonará el servicio, tenemos un 83% de probabilidad de que la predicción sea precisa.

* **F1-Score** =0.55 nos indica qué tan eficiente es nuestro modelo, teniendo en cuenta tanto la puntuación de Recuperación (Recall) como la de Precisión.

Si ambas, la precisión y el recall, están alrededor del 50%, esto sugiere que el modelo no está funcionando de manera óptima y podría estar subajustado o que no ha logrado aprender patrones distintivos en los datos.

Si ambas métricas están alrededor del 50%, podría indicar que el modelo no ha logrado un buen equilibrio entre la precisión y el recall, lo que podría deberse a varios motivos:

1. **Falta de entrenamiento**: El modelo puede no haber sido entrenado lo suficiente para comprender los patrones en los datos.

2. **Simplicidad del modelo**: El modelo elegido puede ser demasiado simple para capturar las relaciones complejas en los datos.

3. **Características insuficientes**: Puede ser que las características utilizadas para el entrenamiento no sean suficientemente informativas para hacer predicciones precisas.

4. **Desequilibrio de clases**: Si hay un desequilibrio significativo entre las clases en el conjunto de datos, esto puede afectar las métricas de manera que parezca que el modelo no está funcionando bien.

Para determinar si el modelo está subajustado o si hay otros problemas, es importante analizar más a fondo las características de los datos. Y se deben probar modelos más complejos o ajustar los hiperparámetros del modelo actual para mejorar su rendimiento.

### Regresión logística
"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión logística
logistic_model = LogisticRegression()

# Ajustar (entrenar) el modelo en los datos de entrenamiento
logistic_model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
predict_logistic_y = logistic_model.predict(X_test)

# Calcular la precisión del modelo
accuracy_logistic = accuracy_score(y_test, predict_logistic_y)
print("Logistic Regression accuracy is:", accuracy_logistic)

# Mostrar un informe de clasificación con métricas adicionales
print(classification_report(y_test, predict_logistic_y))

"""Evalución de modelo:

-  **Precision**: Para la clase 0, la precisión es del 84%. Esto significa que cuando el modelo predice que un cliente no se va a dar de baja, acierta el 84% de las veces. Para la clase 1, la precisión es del 62%, lo que indica que cuando el modelo predice que un cliente se dará de baja, acierta el 62% de las veces.

-  **Recall**: Para la clase 0, la recuperación es del 88%. Esto significa que el modelo identifica correctamente al 88% de los clientes que realmente no se darán de baja. Para la clase 1, la recuperación es del 52%, lo que indica que el modelo detecta el 52% de los clientes que realmente se darán de baja.

- **F1-Score**: El puntaje F1 es una métrica que combina precisión y recuperación. Para la clase 0, el puntaje F1 es del 86%, y para la clase 1, el puntaje F1 es del 57%. Un puntaje F1 más alto indica un equilibrio entre precisión y recuperación.

- **Support**: El soporte muestra la cantidad de muestras en cada clase. En este caso, hay 1,033 muestras de la clase 0 y 374 muestras de la clase 1.

-  **Accuracy**: La exactitud general del modelo es del 78.75%. Esto significa que el modelo clasifica correctamente el 78.75% de las muestras en el conjunto de prueba.

### XG Boost
"""

# Crea un modelo XGBoost
model = XGBClassifier()

# Entrena el modelo en el conjunto de entrenamiento
model.fit(X_train, y_train)

# Realiza predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcula la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

# Imprime un informe de clasificación para obtener más métricas
print(classification_report(y_test, y_pred))

"""Evaluación del modelo

- **Accuracy**: La precisión global del modelo es del 77,97%. Esto significa que el 77,97% de las predicciones son correctas en el conjunto de prueba.

- **Precision**: Para la clase 0, la precisión es del 83%. Esto significa que, de todas las predicciones hechas para la clase 0, el 83% son verdaderas. Para la clase 1, la precisión es del 61%. Esto significa que, de todas las predicciones hechas para la clase 1, el 61% son verdaderas.

- **Recall**: Para la clase 0, el recall es del 89%. Esto significa que el modelo detecta el 89% de todos los casos verdaderos de la clase 0. Para la clase 1, el recall es del 48%, lo que indica que el modelo detecta el 48% de todos los casos verdaderos de la clase 1.

- **F1-Score**: El F1-score es una métrica que combina la precisión y el recall en una sola puntuación. Para la clase 0, el F1-score es 0.86, y para la clase 1, el F1-score es 0.54.

- **Support**: El número de muestras reales en cada clase en el conjunto de prueba. Hay 1033 muestras de la clase 0 y 374 muestras de la clase 1.

- **Macro Avg**: Esto es un promedio de las métricas (precision, recall, F1-score) calculadas para cada clase por separado. En este caso, el promedio macro de estas métricas es del 72%, lo que sugiere cómo el modelo se comporta en promedio en todas las clases.

- **Weighted Avg**: Esto es un promedio ponderado de las métricas, donde cada clase se pondera por su número de muestras en el conjunto de prueba. El promedio ponderado es del 77%, lo que muestra cómo se desempeña el modelo teniendo en cuenta la distribución de las clases en el conjunto de prueba.

"""