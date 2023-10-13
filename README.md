# Geneticos-y-8-Reinas
Primer proyecto de tecnicas de IA. 

## 1. Introducción. 

## 2. Materiales y métodos.
- Python: 3.7
- Bibliotecas usadadas, pueden consultarse [aqui](wwww.google.com)
- Tabla de datos:
| Función | Asignada |
|----------|---------|
| **Inicialización** | Aleatoria |
| **Selección de padres** | Ruleta de aptitud |
| **Cruza** | Ciclica |
| **Mutación** | Inversión |
| **Remplazo** | Generacional |
A continuación damos una descripción de las funciones asiganadas para el desarrrollo de la resolución de nuestro problema.

* _Aleatoria._
  La función aleatoria se encuentra en [inicialización](https://github.com/Qntmth-uv/Geneticos-y-8-Reinas/blob/main/inicializacion.py). Esta se compone principalmente la función _initab()_.
  La función _iniTab()_ inicializa una permutación aleatoria de la lista $\left[ 0, 1 ,2, 3, 4, 5, 6, 7 \right]$. digamos $s$.
  La función _createPopulation_ tiene por entrada un número entero positivo $n$ y devuelve una lista de tamaño $n$ con $n$ _iniTab()_.
  La función _diagAtack_ tiene por entrada una permutación $s$, y calcula usando proyecciones si existe un ataque con las otras reinas en las otras coordenadas.
  La función _fitness_ tiene por entrada una permutación $s$ y evalua que tan bueno es ese tablero de ajedrez. Esto usando por formula $1$-diagAttack/28.
*_Selección de padres y remplazo._
  La función _ruleta de aptitut_ se encuentra en el archivo [selección de padres](https://github.com/Qntmth-uv/Geneticos-y-8-Reinas/blob/main/remplazo_y_seleccion.py). La ruleta de aptitud es una función que dado un $\lamda$ y una lista de listas $\gamma$, se calculan los fitnes de cada uno de los elementos de $\gamma$, se normalizan éstos valores usando el maximo fitness encontrado. Posteirormente con los fintess normalizados cálculamos la probabilidad de que sea elegida una lista. Una vez calculado la probabilidad de cada lista, calculamos la probablidad acumulada. Posteriormente se generan un $\lambda$ valores $n_r$, con $n_r\in U(0,1)$, donde $U$ es la distribución estandar del intervalo $[0,1]$ y $r\in \rbrace 0,..,\lambda$. Posteriormente se evalua las listas que está más cerca por debajo del valor $n_r$ con respecto a la probabilidad acumulada de la lista. Se guardan los indices que satisfacen lo anteior.
  La función _selectionParentsRuleta_ es nuestra función de ruleta de aptitud. Esta tiene por entradas:
  - _población_ Listas de listas, nuestra población actual.  
  - _pick_ Un número entero positivo, nuestro numero de ganadores en la ruleta de aptitud.  
  - _remplace_ Un valor booleano, si deseadomos en la selección no se repitan ganadores.
    - _False_ No permite que se repitan ganadores en el sorteo.
    - _True_ Permite que se repitan ganadores.
  Regresa una lista de listas, que contiene:
  - _ChoicenOnes_ Las listas que fueron elegidas en la ruleta.
  - _indexChoicen_ Los indices de las listas de _ChoicenOnes_ con respecto a la lista original dada.
  - _max(fitneSet)_ El máximo fitness en la lista de listas actual.
  - _fitneSet.index(max(fitneSet))_ Regresa el indice de la lista con el mejor fitness.

*_Cruza._
  La función _cruza_ se encuentra en archivo [Cruza](https://github.com/Qntmth-uv/Geneticos-y-8-Reinas/blob/main/Cruza.py). La cruza ciclica toma dos listas que son permutaciones del mismo tamaño. Posteriormente a través de un algoritmo para buscar valores en la otra lista, se puede construir otras dos listas que en general son distintas a las originales. Nuestra función que hace la cruza ciclica se llama _biSonSex_. Esta función depende de otras dos. En especifico el orden es
  -_biSonSex_
    -_sexCyclic_
      -cyclicV3_
  Las entradas de la función _biSonSex_ son:
  -_entity1_, _entity2_ Una lista que es una permutación.
Mientras que sus salidas son:
  -_son1_, _son2_ Listas a las que se les aplicado _sexCyclic_.
Si desea más información sobre el como funcionan las otras dos funciones puede leer la descripción de cada una de las funciones en el codigo.

*_Mutacion._
  La función _mutacion_ se encuentra en el archibvo [mutación](https://github.com/Qntmth-uv/Geneticos-y-8-Reinas/blob/main/mutacion.py). La mutación toma una única lista que es una permutación, posteriormente se generan dos valores aleatorios entre el cero y el largo de la lista, no repetidos. Se ordenan ambos valores aleatorios para poder crear un intervalo. Los valores que se encuentran en ese intervalo de la lista dada, se invertirán. Puede suceder que la mutación no haga nada. Nuestra función que hace la mutación se llama _mutacionUniparental_, las entradas de la función es:
  -_individio_ Una lista (no requiere que sea necesariamente una permutación)
Mientras que su salida es:
  -_mut_ Una lista a la que se le ha aplicado la inversión.

*_Remplazo._
    La función _remplazo_ se encuentra en el archivo [remplazo](https://github.com/Qntmth-uv/Geneticos-y-8-Reinas/blob/main/remplazo_y_seleccion.py). El remplazo generacional intercambia las listas que fueron cruzadas y mutadas sobre las listas que se usaron para cruzar y mutar. De esta forma la población siempre se mantiene constante y variable. Las entradas de la función _remplacementV2_ tiene por entradas:
    -_population_ Listas de lista con las que se va a mutar.  
    -_indexChoicen_ Indices de las listas ganadoras en la ruleta de aptitud con repsecto a la lista _population_.
    Regresa una lista de listas, esta es:
    -_modiPop_ Lista de listas con listas que han sido cruzadas y mutadas que han remplazado a los elemento que se usaron para crearlas.
ejemplo imagen ![grafica][graficaImagen]

*_Main_
  Se ha creado una función main que se encuentra en el archivo [main](https://github.com/Qntmth-uv/Geneticos-y-8-Reinas/blob/main/main.py). La función main junta todos los modulos anteriores para poder resolver el problema de las ocho reinas. La dependencia de esta función es la siguiente:
  -_Main_
    -_inicializacion_
      - _selección y remplazo_
        -_cruza y mutación_
  Evidentemente para poder correr una función que use todos los modulos anteiores se requieren unas ciertas entradas. Estas son:
    - _población_ Listas de listas, nuestra población actual.
    -_iter_ Número de iteraciones que se harán el algoritmo.
    - selectionNumbers_ Un número entero positivo, nuestro numero de ganadores en la ruleta de aptitud.  
    - _remplace_ Un valor booleano, si deseadomos en la selección no se repitan ganadores.
      - _False_ No permite que se repitan ganadores en el sorteo.
      - _True_ Permite que se repitan ganadores.
  Esta regresa:
    -_MaxFitPerIter_ El máximo fitness de la _población_ en cada iteración.
    -_ancientPop_ La _polacion_ original.
    -_NewPop_ La _población_ final, está es la población que ha sido seleccionada, cruzada, mutada y remplazada.
    -_bestBoard_ El mejor tablero de _Newpop_ con respecto al fitness.

[graficaImagen]: https://github.com/Qntmth-uv/Geneticos-y-8-Reinas/blob/main/Figure_1.png
