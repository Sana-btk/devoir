import statistics

def length(lst):
    """
    Retourne le nombre d'éléments dans la liste.
    """
    if not isinstance(lst, list):
        raise ValueError("L'entrée doit être une liste.")
    return len(lst)

def mean(lst):
    """
    Calcule la moyenne des éléments de la liste.
    """
    if not isinstance(lst, list):
        raise ValueError("L'entrée doit être une liste.")
    if len(lst) == 0:
        raise ValueError("La liste ne peut pas être vide.")
    try:
        return sum(lst) / len(lst)
    except TypeError:
        raise ValueError("Tous les éléments de la liste doivent être des valeurs numériques.")

def range_of_list(lst):
    """
    Retourne la différence entre le maximum et le minimum des éléments de la liste.
    """
    if not isinstance(lst, list):
        raise ValueError("L'entrée doit être une liste.")
    if len(lst) == 0:
        raise ValueError("La liste ne peut pas être vide.")
    try:
        return max(lst) - min(lst)
    except TypeError:
        raise ValueError("Tous les éléments de la liste doivent être des valeurs numériques.")

def median(lst):
    """
    Retourne la médiane des éléments de la liste.
    """
    if not isinstance(lst, list):
        raise ValueError("L'entrée doit être une liste.")
    if len(lst) == 0:
        raise ValueError("La liste ne peut pas être vide.")
    try:
        return statistics.median(lst)
    except TypeError:
        raise ValueError("Tous les éléments de la liste doivent être des valeurs numériques.")

def standard_deviation(lst):
    """
    Retourne l'écart type des éléments de la liste.
    """
    if not isinstance(lst, list):
        raise ValueError("L'entrée doit être une liste.")
    if len(lst) == 0:
        raise ValueError("La liste ne peut pas être vide.")
    try:
        return statistics.stdev(lst)
    except TypeError:
        raise ValueError("Tous les éléments de la liste doivent être des valeurs numériques.")
    except statistics.StatisticsError:
        raise ValueError("La liste doit contenir plus d'un élément pour calculer l'écart type.")

def list_statistics(lst):
    """
    Retourne un dictionnaire avec les statistiques de la liste : longueur, moyenne, plage, médiane et écart type.
    """
    stats = {}
    stats['length'] = length(lst)
    stats['mean'] = mean(lst)
    stats['range'] = range_of_list(lst)
    stats['median'] = median(lst)
    stats['standard_deviation'] = standard_deviation(lst)
    return stats

numbers = [1, 2, 3, 4, 5]
print("Statistics for list:", numbers)
print("Length:", length(numbers)) 
print("Mean:", mean(numbers))  
print("Range:", range_of_list(numbers)) 
print("Median:", median(numbers))  
print("Standard Deviation:", standard_deviation(numbers))  
print("All statistics:", list_statistics(numbers))  

numbers_with_negatives = [-1, -2, -3, -4, -5]
numbers_with_floats = [1.5, 2.5, 3.5, 4.5, 5.5]

print("\nStatistics for list with negative numbers:", numbers_with_negatives)
print("Length:", length(numbers_with_negatives))
print("Mean:", mean(numbers_with_negatives))
print("Range:", range_of_list(numbers_with_negatives))
print("Median:", median(numbers_with_negatives))
print("Standard Deviation:", standard_deviation(numbers_with_negatives))

print("\nStatistics for list with floats:", numbers_with_floats)
print("Length:", length(numbers_with_floats))
print("Mean:", mean(numbers_with_floats))
print("Range:", range_of_list(numbers_with_floats))
print("Median:", median(numbers_with_floats))
print("Standard Deviation:", standard_deviation(numbers_with_floats))

try:
    print(length([]))
except ValueError as e:
    print("Error:", e)

try:
    print(mean([1, 2, 'three', 4, 5]))
except ValueError as e:
    print("Error:", e)
