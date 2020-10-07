import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Cambiar a la ruta en la que se encuentre el dataset
    absolutePath = 'C:/path/'

    # Leer archivo de parametros
    path = absolutePath + 'Data 6 Blocks/Parametros/Parametros.csv'
    data = pd.read_csv(path)
    data = data.set_index('nombre')

    # Muestra los datos de la primera imagen
    print(data.loc['0_0_Imagen_Africa'])

    # Muestra unicamente la informacion de distancia de la primera imagen
    print('La distancia es: ', data.loc['0_0_Imagen_Africa']['distancia'])

    # Mostrar informacion de profundidad como imagen
    maxDist = 300
    name = '0_1_Imagen_Africa.npy'
    depht = np.load(f'{absolutePath}Data 1 Africa/Imagenes/DepthPlanner/{name}')
    depht = np.clip(depht, 0, maxDist)
    ima = depht * 255 / maxDist
    plt.imshow(ima, cmap='gray')
    plt.show()
