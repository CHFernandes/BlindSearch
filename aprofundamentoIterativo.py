entryValue = 0 
exitValue = 0 
depths = {}
father = {}
levels = {}

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

def busca_em_profundidade(graph, selectedCity):
    father[selectedCity] = None
    call_to_busca_em_profundidade(graph, selectedCity, 1)

def call_to_busca_em_profundidade(graph, city, level):
    global entryValue, exitValue
    entryValue += 1
    depths[city] = [entryValue, None]
    levels[city] = level

    children = 0

    for neighbor in graph.get(city):
        if not depths.get(neighbor):
            if level + 1 > limit:
                return
            father[neighbor] = city
            children += 1
            call_to_busca_em_profundidade(graph, neighbor, level + 1)
        
    exitValue += 1
    depths[city][1] = exitValue

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

busca_em_profundidade(citiesRoutes, selectedCity)

print(depths)