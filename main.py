import networkx as nx
import matplotlib.pyplot as plt

# real lat/lon coordinates for each city
city_coords = {
    "Seattle": (47.6062, -122.3321),
    "Rockdale": (47.3910, -121.4812),
    "Ellensburg": (46.9965, -120.5478),
    "Yakima": (46.6021, -120.5059),
    "Kennewick": (46.2112, -119.1372),
    "Pendleton": (45.6721, -118.7886),
    "La Grande": (45.3249, -118.0870),
    "Baker City": (44.7743, -117.8344),
    "Ontario": (44.0266, -116.9629),
    "Boise": (43.6150, -116.2023),
    "Mountain Home": (43.1320, -115.6912),
    "Twin Falls": (42.5629, -114.4609),
    "Burley": (42.5355, -113.7928),
    "Pocatello": (42.8713, -112.4455),
    "Idaho Falls": (43.4917, -112.0339),
    "Jackson": (43.4799, -110.7624),
    "Pinedale": (42.8661, -109.8602),
    "Rock Springs": (41.5875, -109.2029),
    "Rawlins": (41.7911, -107.2387),
    "Laramie": (41.3114, -105.5911),
    "Cheyenne": (41.1400, -104.8202),
    "Denver": (39.7392, -104.9903),
    "Vantage": (46.9493, -119.9886),
    "George": (47.0793, -119.8576),
    "Ritzville": (47.1271, -118.3803),
    "Spokane": (47.6588, -117.4260),
    "Pinehurst": (47.5382, -116.2393),
    "Missoula": (46.8721, -113.9940),
    "Avon": (46.6102, -112.6031),
    "Butte": (45.9965, -112.5347),
    "Bozeman": (45.6770, -111.0429),
    "Big Timber": (45.8341, -109.9552),
    "Park City": (45.6322, -108.9154),
    "Billings": (45.7833, -108.5007),
    "Sheridan": (44.7972, -106.9562),
    "Buffalo": (44.3472, -106.6981),
    "Casper": (42.8501, -106.3252),
    "Glendo": (42.5075, -104.9727)
}

highway_connections = [
    # southern route
    ("Seattle", "Rockdale", 35),
    ("Rockdale", "Ellensburg", 69),
    ("Ellensburg", "Yakima", 37),
    ("Yakima", "Kennewick", 77),
    ("Kennewick", "Pendleton", 45),
    ("Pendleton", "La Grande", 51),
    ("La Grande", "Baker City", 41),
    ("Baker City", "Ontario", 75),
    ("Ontario", "Boise", 53),
    ("Boise", "Mountain Home", 42),
    ("Mountain Home", "Twin Falls", 83),
    ("Twin Falls", "Burley", 36),
    ("Burley", "Pocatello", 71),
    ("Pocatello", "Idaho Falls", 50),
    ("Idaho Falls", "Jackson", 88),
    ("Jackson", "Pinedale", 75),
    ("Pinedale", "Rock Springs", 98),
    ("Rock Springs", "Rawlins", 104),
    ("Rawlins", "Laramie", 96),
    ("Laramie", "Cheyenne", 49),
    ("Cheyenne", "Denver", 99),

    # northern route
    ("Ellensburg", "Vantage", 29),
    ("Vantage", "George", 15),
    ("George", "Ritzville", 85),
    ("Ritzville", "Spokane", 58),
    ("Spokane", "Pinehurst", 68),
    ("Pinehurst", "Missoula", 163),
    ("Missoula", "Avon", 39),
    ("Avon", "Butte", 47),
    ("Butte", "Bozeman", 85),
    ("Bozeman", "Big Timber", 61),
    ("Big Timber", "Park City", 71),
    ("Park City", "Billings", 21),
    ("Billings", "Sheridan", 130),
    ("Sheridan", "Buffalo", 35),
    ("Buffalo", "Casper", 113),
    ("Casper", "Glendo", 70),
    ("Glendo", "Cheyenne", 94)
]

# build graph and add edges using real distances
G = nx.Graph()
G.add_nodes_from(city_coords)
for u, v, dist in highway_connections:
    G.add_edge(u, v, weight=dist)

# run Dijkstra's algorithm
start, end = "Seattle", "Denver"
shortest_path = nx.dijkstra_path(G, start, end)
shortest_length = nx.dijkstra_path_length(G, start, end)

# plot the graph and highlight the shortest path
pos = {city: (lon, lat) for city, (lat, lon) in city_coords.items()}
plt.figure(figsize=(14, 10))
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=7)
nx.draw_networkx_edges(G, pos, edgelist=list(zip(shortest_path, shortest_path[1:])), edge_color="red", width=3)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=5)

plt.suptitle("Shortest Path from Seattle to Denver: 1307 miles", fontsize=14, y=0.98)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.subplots_adjust(top=0.93) 
plt.show()
