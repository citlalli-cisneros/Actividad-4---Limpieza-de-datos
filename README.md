# Actividad-4---Limpieza-de-datos
Actividad práctica para el manejo y limpieza de datos empleando el lenguaje de programación Python en una base de datos diseñada para contener problemas de calidad.

# Práctica de limpieza de datos: Cafe Sales

Este repositorio contiene el proceso completo de inspección, limpieza, transformación e imputación de datos aplicado al dataset **"Cafe Sales – Dirty Data for Cleaning Training"** de Kaggle.

## Descripción
El conjunto de datos consta de 10,000 registros de ventas de una cafetería con anomalías presentes (valores faltantes, errores de sintaxis, diferencias numéricas y datos categóricos incompletos). El objetivo es limpiarlo mediante técnicas de imputación simple, clustering, entre otros.

## Algoritmo
1. **Carga de la base de datos e inspección:** Análisis de la información (tipos de datos (`df.info()`), números de registros, distribución de nulos).
2. **Estandarización de datos:** Conversión variables a tipos 'Int', 'Float' y 'Datetime'; y conversión de valores como "ERROR", "UNKNOWN" y "None" a `NaN` (df.replance(..., pd.NA)). 
3. **Imputación numérica:** Recálculo exacto entre `Quantity`, `Price Per Unit` y `Total Spent`.
4. **Rellenar espacios en blanco y eliminar datos duplicados:** Detección de valores NaN y remplazo por una nueva categoría "UNKNOWN" (df.fillna()); verificación de valores duplicados, para este caso no existían registros dobles.
5. **Eliminar valores nulos:** Remoción de valores nulos mediante df.dropna().
6. **Guardar cambios y exportación de la base de datos limpia:** Almacenamiento de la base de datos limpia en la carpeta correspondiente.

## Tabla Resumen 

| Problema encontrado | Registros afectados | Acción realizada | Justificación |
| :--- | :--- | :--- | :--- |
| **Marcadores de error y cadenas ruidosas** (`"ERROR"`, `"UNKNOWN"`, `"None"`, `""`) | ~3,500 registros con al menos una celda errónea (~35% del dataset) | Reemplazo sistemático de cadenas no numéricas y nulas por valores verdaderos `NaN` mediante `replace()`. | Evita distorsiones en el cálculo estadístico y permite la correcta conversión de datos al tipo correspondiente (`float`, `datetime`). |
| **Tipos de datos incorrectos** (`object` en lugar de `numeric` o `datetime`) | 10,000 registros en `Quantity`, `Price Per Unit`, `Total Spent` y `Transaction Date` | Conversión explícita utilizando `pd.to_numeric()` y `pd.to_datetime()`. | La presencia de texto en columnas numéricas impide realizar operaciones vectorizadas o agregaciones analíticas. |
| **Valores faltantes o inconsistentes en `Price Per Unit` e `Item`** | ~333 registros en `Item` y ~179 en `Price Per Unit` | Imputación mediante el mapa estático de precios del menú (`Coffee`: 2.0, `Tea`: 1.5, `Sandwich`: 4.0, etc.) o inferencia con `Total Spent / Quantity`. | Se conserva la integridad de las filas deduciendo el dato omitido mediante relaciones lógicas directas sin eliminar registros válidos. |
| **Valores faltantes en `Quantity` y `Total Spent`** | ~138 registros en `Quantity` y ~185 en `Total Spent` | Recálculo algebraico exacto: `Total Spent = Quantity * Price Per Unit` y `Quantity = Total Spent / Price Per Unit`. | Al existir una dependencia funcional exacta ($Total = Cantidad \times Precio$), la reconstrucción es determinista y no introduce sesgo en la muestra. |
| **Valores faltantes en variables categóricas (`Payment Method` y `Location`)** | ~2,600 registros en `Payment Method` y ~3,300 en `Location` | Imputación categórica mediante la etiqueta explícita `'Unknown'`. | Asignar la moda distorsionaría la frecuencia real de los métodos de pago o ubicaciones. Etiquetar como `'Unknown'` preserva el registro de la venta total. |
| **Formatos heterogéneos o faltantes en `Transaction Date`** | ~150 registros inconsistentes | Conversión a `datetime64[ns]` e imputación por propagación temporal (`ffill`). | Mantiene la continuidad chronológica del flujo de caja de la cafetería sin descartar transacciones. |

## Instrucciones para ejecución
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/cafe-sales-data-cleaning.git](https://github.com/TU_USUARIO/cafe-sales-data-cleaning.git)
   cd cafe-sales-data-cleaning
