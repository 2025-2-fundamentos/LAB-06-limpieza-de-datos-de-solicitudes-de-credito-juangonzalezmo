"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import os
import pandas as pd



def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    ruta_entrada = "files/input/solicitudes_de_credito.csv"
    df = pd.read_csv(ruta_entrada, sep=";", index_col=0)

    columnas_texto = df.select_dtypes(include=["object"]).columns

    for columna in columnas_texto:

        df[columna] = df[columna].str.lower()
        df[columna] = df[columna].str.replace("_", " ")
        df[columna] = df[columna].str.replace("-", " ")
        df[columna] = df[columna].str.replace(",", "")
        df[columna] = df[columna].str.replace("$", "")
        df[columna] = df[columna].str.replace(".00", "")

    df["monto_del_credito"] = df["monto_del_credito"].astype(float)

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    fechas_brutas = df["fecha_de_beneficio"]
    fechas_dmY = pd.to_datetime(
        fechas_brutas,
        format="%d/%m/%Y",
        errors="coerce",
    )
    fechas_Ymd = pd.to_datetime(
        fechas_brutas,
        format="%Y/%m/%d",
        errors="coerce",
    )
    df["fecha_de_beneficio"] = fechas_dmY.combine_first(fechas_Ymd)

    df = df.drop_duplicates()
    df = df.dropna()

    os.makedirs("files/output", exist_ok=True)

    df.to_csv(
        "files/output/solicitudes_de_credito.csv",
        columns=df.columns,
        index=False,
        encoding="utf-8",
        sep=";",
    )
