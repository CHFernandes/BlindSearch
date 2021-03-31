citiesArray = [
    "Rostock",
    "Berlin",
    "Dresden",
    "Leipzig",
    "Magdeburg",
    "Lübeck",
    "Braunschweig",
    "Hannover",
    "Hamburg",
    "Bremen",
    "Munster",
    "Köln",
    "Düsseldorf",
    "München", 
    "Ulm",
    "Ingolstadt",
    "Stuttgart",
    "Baden",
    "Frankfurt",
    "Nürnberg",
    "Mainz",
    "Trier",
    "Bonn",
]

citiesRoutes = {
   "Rostock": ["Berlin", "Magdeburg", "Lübeck"],
   "Berlin": ["Rostock", "Magdeburg", "Dresden"],
   "Dresden": ["Berlin", "Leipzig"],
   "Leipzig": ["Dresden", "Magdeburg", "Nürnberg"],
   "Magdeburg": ["Rostock", "Berlin", "Leipzig", "Braunschweig", "Lübeck"],
   "Lübeck": ["Rostock", "Magdeburg", "Braunschweig", "Hannover", "Hamburg"],
   "Braunschweig": ["Lübeck", "Magdeburg", "Nürnberg", "Mainz", "Düsseldorf", "Munster", "Hannover"],
   "Hannover": ["Lübeck", "Braunschweig", "Munster", "Bremen", "Hamburg"],
   "Hamburg": ["Lübeck", "Hannover", "Bremen"],
   "Bremen": ["Hamburg", "Hannover", "Munster"],
   "Munster": ["Bremen", "Hannover", "Braunschweig", "Düsseldorf", "Köln"],
   "Köln":["Düsseldorf","Bonn","Munster" ],
   "Düsseldorf":["Munster","Köln","Mainz","Braunschweig"],
   "München":["Ulm","Ingolstadt"],
   "Ulm":["Ingolstadt","München","Stuttgart"],
   "Ingolstadt":["Ulm","München","Stuttgart","Nürnberg"],
   "Stuttgart":["Frankfurt","Baden","Ulm","Ingolstadt"],
   "Baden":[ "Frankfurt","Stuttgart"],
   "Frankfurt":["Nürnberg","Mainz","Trier","Baden","Stuttgart"],
   "Nürnberg": ["Frankfurt", "Ingolstadt","Leipzig","Braunschweig","Mainz" ],
   "Mainz": ["Frankfurt","Trier","Nürnberg","Braunschweig","Düsseldorf","Köln","Bonn" ],
   "Trier": ["Bonn","Frankfurt","Mainz"],
   "Bonn":["Trier","Mainz","Köln" ],
}

def search(graph, selectedCity, selectedEndingCity):
    queue = [] 
    visited = {}
    l = 1 
    level = {} 

    queue.append(selectedCity)
    visited[selectedCity] = l 
    level[selectedCity] = 0 

    while len(queue):
        city = queue.pop(0)
        for route in graph.get(city):
            if not visited.get(route):
                queue.append(route)
                l += 1
                visited[route] = l
                level[route] = level[city] + 1
                if route == selectedEndingCity:
                    return visited

    print("Erro, nenhuma rota foi encontrada!")
    return visited

print("Selecione uma cidade de partida \n")

i = 0

while i < len(citiesArray):
    nextItem = str(i+1)
    print(nextItem + " - " + citiesArray[i])
    i+=1

print()
selectedCityId = int(input())
selectedCityId-=1

selectedCity = citiesArray[selectedCityId]

print("Selecione uma cidade de parada \n")

i = 0

while i < len(citiesArray):
    nextItem = str(i+1)
    print(nextItem + " - " + citiesArray[i])
    i+=1

print()
selectedEndingCityId = int(input())
selectedEndingCityId-=1

selectedEndingCity = citiesArray[selectedEndingCityId]

visited = search(citiesRoutes, selectedCity, selectedEndingCity)

print(visited)
    