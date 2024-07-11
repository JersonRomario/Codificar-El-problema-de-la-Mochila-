def knapsack(capacity, weights, values):
    n = len(weights)
    # Creamos una matriz para almacenar los resultados de subproblemas
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Calculamos el valor máximo que se puede obtener para cada capacidad
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Si podemos incluir el objeto i en la mochila, decidimos si incluirlo o no
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # Si no podemos incluir el objeto i, copiamos el valor de la celda anterior
                dp[i][w] = dp[i - 1][w]

    # El valor máximo que se puede obtener estará en dp[n][capacity]
    max_value = dp[n][capacity]
    
    # Ahora determinamos qué objetos se incluyeron
    included_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i - 1)
            w -= weights[i - 1]

    # Devolvemos el valor máximo y los índices de los objetos incluidos
    return max_value, included_items

# Ejemplo de uso:
capacity = 10
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]

max_value, items = knapsack(capacity, weights, values)

print("Valor máximo obtenido:", max_value)
print("Objetos incluidos (índices):", items)
