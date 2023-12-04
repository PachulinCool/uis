from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Generamos 1000 datos de muestra
np.random.seed()
X = np.random.normal(100, 10, 1000).reshape(-1, 1)  # Estaturas en cm
Y = (X.flatten() / 100 + np.random.normal(0, 0.03, 1000))  # Edades en años

# Dividimos nuestros datos en un conjunto de entrenamiento y un conjunto de prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Entrenamos nuestro modelo de regresión lineal con los datos de entrenamiento
model = LinearRegression()
model.fit(X_train, Y_train)

# Evaluamos el rendimiento de nuestro modelo utilizando el conjunto de prueba
Y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test, Y_pred)
print(f'Error cuadrático medio: {mse}')

# Función para predecir la edad basada en la estatura
def predecir_edad(estatura):
    edad_predicha = model.predict(np.array([[estatura]]))
    return edad_predicha[0]

# Prueba la función con una estatura de 110 cm
estatura = 110
edad_predicha = predecir_edad(estatura)
print(f'Para una estatura de {estatura} cm, la edad predicha es de {edad_predicha} años.')
