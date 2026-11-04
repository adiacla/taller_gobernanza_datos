"""
Remediación de pacientes_salucompleta_v1.csv -> pacientes_salucompleta_v2.csv
(simula la entrega del equipo de datos de SaluCompleta tras los hallazgos de la auditoría)
"""
import hashlib
import hmac
import os

import numpy as np
import pandas as pd

ENTRADA = "pacientes_salucompleta_v1.csv"
SALIDA = "pacientes_salucompleta_v2.csv"

# Clave de seudonimización. En producción NUNCA va en el repositorio: se lee de un gestor de secretos.
CLAVE = os.environ.get("CLAVE_SEUDONIMIZACION")
if CLAVE is None:
    CLAVE = "clave-solo-para-el-taller"
    print("AVISO: se usa la clave de demostración del taller (no apta para producción).")


def seudonimo(valor):
    return hmac.new(CLAVE.encode(), str(valor).encode(), hashlib.sha256).hexdigest()[:16]


def estandarizar_fecha(serie):
    resultado = pd.Series(pd.NaT, index=serie.index)
    for formato in ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%B %d, %Y"]:
        resultado = resultado.fillna(pd.to_datetime(serie, format=formato, errors="coerce"))
    return resultado.dt.strftime("%Y-%m-%d")


df = pd.read_csv(ENTRADA)
n_inicial = len(df)

# 1) Integridad: el mismo documento no puede corresponder a dos pacientes
df = df.drop_duplicates(subset=["numero_documento"], keep="first")

# 2) Privacidad: identificadores directos fuera; el documento se conserva solo como seudónimo
df["documento_seudonimo"] = df["numero_documento"].apply(seudonimo)
df = df.drop(columns=["numero_documento", "nombre_completo", "direccion_residencia",
                      "telefono_contacto", "correo_electronico", "medico_tratante"])

# 3) Pertinencia: variables protegidas (sin justificación técnica) e irrelevantes (ruido)
df = df.drop(columns=["etnia", "religion", "orientacion_sexual", "afiliacion_politica",
                      "color_cabello", "marca_celular", "red_social_favorita", "equipo_futbol_favorito"])

# 4) Redundancia
df = df.drop(columns=["eps_anterior_afiliacion", "imc", "fecha_nacimiento"])

# 5) Estandarización
df["genero"] = df["genero"].replace({"M": "Masculino", "masculino": "Masculino",
                                     "F": "Femenino", "femenino": "Femenino"})
df["fecha_ultima_consulta"] = estandarizar_fecha(df["fecha_ultima_consulta"])

# 6) Valores clínicamente imposibles -> nulo (no se imputan aquí)
df.loc[(df["edad"] < 0) | (df["edad"] > 110), "edad"] = np.nan
df.loc[(df["peso_kg"] <= 0) | (df["peso_kg"] > 300), "peso_kg"] = np.nan
df.loc[(df["presion_sistolica"] < 60) | (df["presion_sistolica"] > 260), "presion_sistolica"] = np.nan
df.loc[df["dias_estancia_hospitalaria"] > 90, "dias_estancia_hospitalaria"] = np.nan
for c in ["edad", "presion_sistolica", "dias_estancia_hospitalaria"]:
    df[c] = df[c].astype("Int64")

df.to_csv(SALIDA, index=False)
print(f"Remediación lista: {n_inicial} -> {len(df)} registros, {df.shape[1]} columnas -> {SALIDA}")
