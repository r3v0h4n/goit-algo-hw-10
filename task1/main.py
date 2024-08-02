import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')

model += lemonade + fruit_juice, "Total Drinks"

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
model += 1 * lemonade <= 50, "Sugar"
model += 1 * lemonade <= 30, "LemonJuice"
model += 2 * fruit_juice <= 40, "FruitPuree"

model.solve()

print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade: {lemonade.varValue}")
print(f"Fruit Juice: {fruit_juice.varValue}")
print(f"Total Drinks: {pulp.value(model.objective)}")