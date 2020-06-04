# recursividad_lambda
_Explicación y ejemplos de recursividad en funciones lambda en python_

## ¿Cómo funciona la recursividad en funciones lambda?
Una de las posibles formas de implementar la recursividad en las funciones lambda es mediante el uso de una variable. Esto se logra haciendo la asignación de la función en la variable y dentro de la función llamarse a sí misma bajo el nombre que se le ha asignado.
Una demostración de la estructura básica en un ejemplo usual como el del uso de la recursividad para el cálculo de un factorial es: 

```python
factorial = lambda a : 1 if a==0 else a*factorial(a-1)
print(factorial(int(input())))
```
Que vemos tiene cierta similitud con las funciones recursivas en programación funcional sin el uso de las funciones lambda, así:

```python
def factorial(a):
  if a==0:
    return 1
  else:
    return a*factorial(a-1)
print(factorial(int(input())))
```
Otra de las formas, la más compleja de comprender al principio, es una serie de funciones lambda cuyo valor de retorno pasa como parámetro a la siguiente función y devuelve un valor final al usuario sin conocer los valores de retorno que tienen las funciones lambda en su desarrollo, así: 

```python
(lambda a:lambda v:a(a,v))(lambda s,x:1 if x==0 else x*s(s,x-1))(int(input()))
```

Nombre  | Código
------------- | -------------
Juan Felipe Herrera Poveda | 20181020077
