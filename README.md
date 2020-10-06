# AirSimUAVDetectionDataset
El conjunto de datos generado se compone por imágenes de 6 entornos de AirSim: Africa, Neighborhood, City, Building99, Zhangjiajie y Blocks.

Este dataset contiene 11.510 imágenes del Ardrone generadas a través del simulador Airsim en 6 entornos diferentes: AirSim: Africa, Neighborhood, City, Building99, Zhangjiajie y Blocks. Tiene un tamaño total descomprimido de 440 GB.

El código para la generación del dataset se puede encontrar en el siguiente repositorio:

https://github.com/danifm01/airsimDronDatabaseGenerator

El dataset contiene los datos de profundidad de cada imagen para cada pixel guardado en archivos .npy. Estos archivos se deben abrir utilizando la librería numpy de python. Se encuentran los datos de profundidad tanto de perspectiva (DepthPerspective), como planar (DepthPlanner), así como imágenes para facilitar su visualización (DephtVis).

La estructura de árbol de las carpetas utilizadas en el dataset es la siguiente:

```bash
+---Imagenes
|   +---DepthPerspective
|   +---DepthPlanner
|   +---DepthVis
|   +---Scene
|   +---Segmentation
+---ImagenesBoundingBox
+---ImagenesMarcadas
+---Parametros   
```

Las imágenes fuente se encuentran en la carpeta Scene dentro de la carpeta imágenes donde también se encuentran las imágenes de segmentación y la información de profundidad.

En las carpetas ImagenesBoundingBox e ImagenesMarcadas se encuentran las imágenes de la carpeta Scene pero en el primer caso con una bounding box que encuadra al dron generada mediante la imagen de segmentación y en el segundo caso rodeando al dron con una circunferencia cuyo centro ha sido generado a partir de la posición del dron y la cámara en el entorno de simulación y el radio es proporcional a la distancia del dron a la cámara.

Por último, en la carpeta Parámetros se encuentran los archivos .csv con la información característica de cada imagen. En cada entorno se encuentra el archivo que contiene a todas las imágenes de ese entorno y todas las anteriores (a modo de copia de seguridad) con el nombre Parametros.csv y los archivos individuales de cada entorno anterior (siguiendo la numeración).

Los parámetros que se han extraído para cada imágen son: la distancia en metros de la cámara al dron (distancia), la dirección en la que se encuentra el dron según ángulos de euler (phi, theta) en grados, las coordenadas en pixeles del centro del dron (xIma, yIma), el radio en pixeles que se estima del dron (radioIma), las coordenadas del bounding box en pixeles (x1BB, y1BB, x2BB, y2BB), la orientación absoluta en forma de quaternion del dron en que se situa la cámara (orientacionVisor\_), la orientación absoluta del dron visto por la cámara (orientacionVisto\_) y la orientación relativa del dron visto según el dron visor (orientacionRelativa).
