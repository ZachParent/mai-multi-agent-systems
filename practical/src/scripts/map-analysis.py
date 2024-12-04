# %%
import osmnx as ox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from pypalettes import load_cmap

airnomads = load_cmap("AirNomads")

plt.style.use("default")

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "../reports")
FIGURES_DIR = os.path.join(REPORTS_DIR, "figures")

# %%
places = [
    "Barcelona, Spain",
    "Seville, Spain",
    "Salamanca, Spain",
    "Tossa de Mar, Spain",
    "Lloret de Mar, Spain",
    "New York, NY, USA",
]
mapps = []
for place in places:
    mapps.append(ox.graph_from_place(place, network_type="drive"))

# %%
fig, axs = plt.subplots(2, len(places) // 2, figsize=(20, 16))
for i, (mapp, ax, place) in enumerate(zip(mapps, axs.flatten(), places)):
    ox.plot_graph(
        mapp, ax=ax, show=False, close=False, edge_color="grey", node_color="black"
    )
    ax.set_title(f"#{i+1}: {place}", fontsize=20)

ax = axs.flatten()[places.index("Lloret de Mar, Spain")]
ax.set_facecolor((0, 1, 0, 0.1))
ax.text(
    0.6,
    0.75,
    "Selected City",
    transform=ax.transAxes,
    ha="center",
    va="center",
    fontweight="bold",
    fontsize=24,
    color="green",
)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, "maps_of_candidate_cities.png"), dpi=300)
plt.show()

# %%
fig, ax = plt.subplots(figsize=(12, 10))
ox.plot_graph(
    mapps[places.index("Lloret de Mar, Spain")],
    ax=ax,
    show=False,
    close=False,
    edge_color="grey",
    node_color="black",
)
plt.savefig(os.path.join(FIGURES_DIR, "map_of_selected_city.png"), dpi=300)
plt.show()


# %%
mapp_stats = []
for mapp, place in zip(mapps, places):
    map_proj = ox.project_graph(mapp)
    nodes_proj = ox.graph_to_gdfs(map_proj, edges=False)
    graph_area_m = nodes_proj.unary_union.convex_hull.area
    stats = ox.basic_stats(map_proj, area=graph_area_m, clean_int_tol=15)
    mapp_stats.append(stats)
df = pd.DataFrame(mapp_stats, index=places)


# %%
df

# %%
columns = [
    "n",
    "m",
    "k_avg",
    "edge_length_total",
    "edge_length_avg",
    "streets_per_node_avg",
    "intersection_count",
    "edge_density_km",
    "street_density_km",
    "clean_intersection_density_km",
]

colors = airnomads(np.linspace(0, 1, len(df)))
color_dict = dict(zip(df.index, colors))

fig, axs = plt.subplots(2, len(columns) // 2, figsize=(20, 10))
for ax, col in zip(axs.flatten(), columns):
    sorted_df = df.sort_values(by=col)
    ax.bar(
        sorted_df.index, sorted_df[col], color=[color_dict[i] for i in sorted_df.index]
    )
    ax.set_title(col)
    ax.set_xticks(sorted_df.index)
    ax.set_xticklabels(sorted_df.index, rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, "map_complexity_statistics.png"), dpi=300)
plt.show()


# %%
rankings_df = df.copy().drop(columns=set(df.columns) - set(columns))
for col in columns:
    rankings_df[col] = rankings_df[col].rank(ascending=False).astype("int64")
rankings_df

# %%
rank_sums = rankings_df.sum(axis=1)
rank_sums = rank_sums.sort_values(ascending=True)
inverse_rank_sums = ((1 / rank_sums) / (max(1 / rank_sums))).sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(
    range(len(inverse_rank_sums)),
    inverse_rank_sums.values,
    color=[color_dict[i] for i in inverse_rank_sums.index],
)
ax.set_xlabel("City", fontsize=14, fontweight="bold")
ax.set_xticks(range(len(inverse_rank_sums)))
ax.set_xticklabels(inverse_rank_sums.index, rotation=45, ha="right", fontsize=14)
ax.set_ylabel("Relative Map Complexity", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, "relative_map_complexity.png"), dpi=300)
plt.show()

# %%
