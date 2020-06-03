# recursividad_lambda
_Explicación y ejemplos de recursividad en funciones lambda en python_

## ¿Cómo funciona la recursividad en funciones lambda?
Para poder hacer uso de la recursividad en las funciones lambda es importante la asignación de la misma a una variable, con el fin de poder hacer un llamado a la función, de otra forma no habría una forma de hacer una referencia a la función en sí.
Una demostración de la estructura básica en un ejemplo usual como el del uso de la recursividad para el cálculo de un factorial es: 

```
factorial = lambda a : 1 if a==0 else a*factorial(a-1)
```
