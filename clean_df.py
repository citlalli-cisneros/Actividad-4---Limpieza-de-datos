import numpy as np
import pandas as pd


#1. Carga y visualización de datos
df=pd.read_csv('data/dirty_cafe_sales.csv')
print("-----BASE DE DATOS INICIAL----\n")
print("Filas iniciles:", len(df))
print("Columnas:", len(df.columns))

print("\nValores nulos iniciales:")
print(df.isnull().sum())

print("\nTipos de datos identificados:")
print(df.dtypes)

print("\n", df.head())
#2.Estandarizar tipos de datos
variables_str = [
    "Transaction ID",
    "Item",
    "Payment Method",
    "Location"
]
print(df.head())
for variable in variables_str:
    df[variable] = df[variable].astype("string").str.strip()

df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df["Price Per Unit"] = pd.to_numeric(
    df["Price Per Unit"],
    errors="coerce"
)

df["Total Spent"] = pd.to_numeric(
    df["Total Spent"],
    errors="coerce"
)

df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"],
    errors="coerce"
)

#3. Valores nulos
valores_invalidos = ["UNKNOWN", "ERROR", "unknown", "error", ""]

df.replace(valores_invalidos, pd.NA, inplace=True)

#4. Eliminar datos duplicados
print("\nDuplicados encontrados:", df.duplicated().sum())
df = df.drop_duplicates()

#5. Rellenar espacios vacios
df["Item"] = df["Item"].fillna("Unknown")
df["Payment Method"] = df["Payment Method"].fillna("Unknown")
df["Location"] = df["Location"].fillna("Unknown")

    #Para rellenar 'Total Spent'
#1. Creamos una valiable temporal para calcular el monto final
df["Calculated Total"] = (
    df["Quantity"] * df["Price Per Unit"]
)
#2. Si 'Total Spent' está vacío o marca error, remplazamos con el calculo
df["Total Spent"] = df["Total Spent"].fillna(
    df["Calculated Total"]
)

#3. Finalmente eliminamos nuestra variable auxiliar
df.drop(columns=["Calculated Total"], inplace=True)

#9.Eliminamos registros con valores nulos
df = df.dropna(
    subset=[
        "Transaction ID",
        "Quantity",
        "Price Per Unit",
        "Total Spent",
        "Transaction Date"
    ]
)

#10. Validamos los tipos de datos
df["Quantity"] = df["Quantity"].astype(int)

df["Price Per Unit"] = df["Price Per Unit"].astype(float)

df["Total Spent"] = df["Total Spent"].astype(float)

#11. Guardamos los cambios en la base y exportamos
print("-----BASE DE DATOS LIMPIA----\n")
print("Filas finales:", len(df))
print("Columnas:", len(df.columns))

print("\nValores nulos finales:")
print(df.isnull().sum())

print("\nTipos de datos:")
print(df.dtypes)

print("\n",df.head())

df.to_csv("data/clean_data.csv", index=False)


#tabla comparativa
df_test = df.copy()

df_test["Quantity"] = pd.to_numeric(
    df_test["Quantity"], errors="coerce"
)

df_test["Price Per Unit"] = pd.to_numeric(
    df_test["Price Per Unit"], errors="coerce"
)

df_test["Total Spent"] = pd.to_numeric(
    df_test["Total Spent"], errors="coerce"
)

df_test["Total Calculado"] = (
    df_test["Quantity"] * df_test["Price Per Unit"]
)

inconsistencias = (
    df_test["Total Spent"] != df_test["Total Calculado"]
)

print("Registros con problemas de exactitud:",
      inconsistencias.sum())