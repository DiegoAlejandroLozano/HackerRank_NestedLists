def identificar_alumnos(records, list_scores):
    '''Función encargada de buscar en la lista anidada "records" las personas
    con la segunda calificación más baja. Las ordena y las devuelve en una lista
    
    Parámetros de entrada:
    records --> lista anidada
    list_scores --> lista ordenada de calificaciones
    
    Valor de retorno:
    lista ordenada con los nombres de las personas con la segunda
    calificación más baja'''
    list_names = list()
    second_lowest_score = list_scores[len(list_scores)-2]
    for record in records:
        if second_lowest_score in record:
            list_names.append(record[0])
    return sorted(list_names, reverse=False)


def ordenar_notas(records):
    '''Función encargada de ordenar sólo las notas de mayor a menor.
    Devuelve una lista con las notas ordenadas
    
    Parámetro de entrada:
    records --> lista anidada donde se extrae las notas
    
    Valor retorno:
    Se devuelve la lista de notas ordenadas de mayor a menor.'''
    score = list()
    for i in records:
        if i[1] not in score:
            score.append(i[1])
    return sorted(score, reverse=True)


def main():
    '''Función principal'''
    records = list()
    for n in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    list_scores = ordenar_notas(records)
    for name in identificar_alumnos(records, list_scores):
        print(name)


if __name__ == '__main__':
    main()
