# Salto_clasico_cuantico

## Autor:
***Sebastian Cardona***

En este repositorio usted encontrará unas funciones que permiten simular un sistema determinístico, uno probabilístico y otro cuántico, dichos sistemas se usan para saber la probabilidad de que una partícula o fotón se encuentre en cierta posición a partir de sistemas iniciales dados, además estará el experimento de la doble rendija cuántica y probabilística, la cual enseña un poco sobre la interferencia cuántica que hay sobre varias historias diferentes en el multiverso de una misma partícula

**La libreria principal contiene:**
- Experimento del sistema determinístico sobre las canicas, cuya matriz es booleana.
- Experimento del sistema probabilístico, vuya matriz es doblemente estocastica y vector estado con norma = 1
- Experimento clásico probabilistico de las multiples rendijas.
- Experimento del sistema probabilístico cuántico, cuya matriz es con números complejos al igual que el vector estado, las probabilidades se hallan con el modulo cuadrado
- Experimento cuántico de las multiples rendijas.
- función que muestra la gráfica de barras de un estado probabilistico en unidades de %

## Inicio:
Para iniciar, usted debe tener instalada la librería de Numpy y de matplotlib, se puede hacer en el cmd. Esto ya que con matplotlib se nos permite mostrar la gráfica de barras.
Luego debe descargar todos los programas, y guardarlos en una misma carpeta, esto para poder acceder a las demás librerias.

## Contenido
- libreria ***salto_clasico_cuantico.py*** contiene las funciones mencionadas antes que efectuaran los experimentos
- libreria ***libvecspaces.py*** contiene las operaciones de los espacios vectoriales complejos (matrices y vectores) puesto que en los experimentos se ejecutaran operaciones entre matrices y vectores complejos
- libreria ***test_cuantico.py*** contiene dos pruebas por función, es decir un total de 12 pruebas, que indican la perfecta ejecución de los experimentos, por lo tanto al ejecutar esta librería se abrirán dos gráficas de barras que se mencionaron antes y que se guardarán en su pc en la carpeta donde tenga los archivos, despúes que cierre estas gráficas aparecerá un *ok* que indica que todas las pruebas se ejecutaron efectivamente y salieron correctas
