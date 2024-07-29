# %%
def longitud_cadena_mas_larga_sin_repetidos(cadena):
    mapa_caracteres = {}
    max_longitud = 0
    inicio = 0
    
    for i, char in enumerate(cadena):
        if char in mapa_caracteres and mapa_caracteres[char] >= inicio:
            inicio = mapa_caracteres[char] + 1
        mapa_caracteres[char] = i
        max_longitud = max(max_longitud, i - inicio + 1)
    
    return max_longitud

# Fragmentos de obras literarias
fragmentos = [
    "Es una verdad universalmente aceptada que un hombre soltero en posesión de una gran fortuna debe estar en busca de esposa. Sin embargo, poco se sabe sobre los sentimientos o puntos de vista de un hombre así cuando se instala por primera vez en una vecindad. Este hecho está tan bien fijado en las mentes de las familias vecinas, que es considerado como propiedad legítima de alguna de sus hijas. '¿Has oído, mi querido Mr. Bennet?', dijo su señora, 'que Netherfield Park está alquilado al fin?'. Mr. Bennet respondió que no.",
    "¡Oh, Romeo, Romeo! ¿Por qué eres tú Romeo? Niega a tu padre y rehúsa tu nombre, o si no quieres, júrame tan solo que me amas, y dejaré de ser una Capuleto.",
    "Era un principito que habitaba un planeta apenas más grande que él, y que necesitaba un amigo. Para aquellos que comprenden la vida, esto habría parecido una verdad evidente. Pero para mí, que amaba al principito, era tan valioso como la esperanza. No podía imaginarme nada mejor que un mundo en el que la amistad fuese tan importante como el agua para una flor."
]

# Aplicar la función a cada fragmento
resultados = [longitud_cadena_mas_larga_sin_repetidos(fragmento) for fragmento in fragmentos]

# Mostrar los resultados
for i, resultado in enumerate(resultados):
    print(f"Fragmento {i+1}: Longitud de la cadena más larga sin caracteres repetidos es {resultado}")

# %%
