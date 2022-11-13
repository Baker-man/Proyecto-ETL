#función para checkear todas las columnas y el número de valores nulos que tienen
def check_nan(df: pd.DataFrame) -> None:
    
    nan_cols=df.isna().mean() * 100  # el porcentaje
    
    display(f'N nan cols: {len(nan_cols[nan_cols>0])}')
    display(nan_cols[nan_cols>0])
    
    plt.figure(figsize=(10, 6))  # inicia la figura y establece tamaño

    sns.heatmap(df.isna(),  # mapa de calor
                yticklabels=False,
                cmap='viridis',
                cbar=False)

    plt.show();
    

#función en la que si hay positivo en alcohol añade un 1 a la nueva columna y si no un 0:

def positividad_alcohol(x):
    
    if x == 'S':
        return 1
    else:
        return 0


#función para facilitar la creación de tres columnas de año, mes y día a partir de la columna fecha
def limpiar_fecha(string):
    
    try:
        return string.split('-')
    except:
        return [np.nan, np.nan, np.nan]