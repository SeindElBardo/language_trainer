# language_trainer
Programa casero para practicar inglés (o lo que quieras)

# Cómo usarlo
El fichero `vocabulary.py` incluye al final una variable llamada `words_list` que contiene una lista con tuplas (<respuesta>, <pregunta>), esas tuplas serán las que pregunte el programa al ejecutar `trainer.py`.

La variable `WORDS` de `trainer.py` indica cuantas palabras son preguntadas. Éstas son seleccionadas según aquellas con mayor relación de fallos y son preguntadas aleatoriamente hasta que son acertadas.