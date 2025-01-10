import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define tasks and their dependencies
tasks = {
    "Search Related Cases": {"depends_on": [], "agent": "Archive Keeper"},
    "Draft Initial Article": {"depends_on": [], "agent": "Article Writer"},
    "Integrate Additional Information": {"depends_on": ["Search Related Cases", "Draft Initial Article"], "agent": "Article Writer"},
    "Review and Authorize Publication": {"depends_on": ["Integrate Additional Information"], "agent": "Mayor"},
    "Provide Social Media Feedback": {"depends_on": ["Integrate Additional Information"], "agent": "Social Media Commentator"},
    "Publish Final Report": {"depends_on": ["Integrate Additional Information", "Review and Authorize Publication", "Provide Social Media Feedback"], "agent": "Communication Operator"},
}

# Add nodes and edges to the graph
for task, details in tasks.items():
    G.add_node(task, agent=details["agent"])
    for dependency in details["depends_on"]:
        G.add_edge(dependency, task)

# Define colors for agents
agent_colors = {
    "Communication Operator": "skyblue",
    "Archive Keeper": "gold",
    "Article Writer": "lightgreen",
    "Mayor": "lightcoral",
    "Social Media Commentator": "plum"
}

# Get node colors based on agents
node_colors = [agent_colors[G.nodes[node]["agent"]] for node in G.nodes]

def hierarchical_layout(G, root=None):
    """
    Create a hierarchical layout for a directed graph.
    Nodes will be arranged in levels based on their distance from the root.
    """
    if not nx.is_directed(G):
        raise ValueError("Graph must be directed for a hierarchical layout.")
    
    # Use breadth-first search to determine levels
    if root is None:
        root = next(iter(G.nodes))  # Choose an arbitrary node as root
    
    levels = nx.single_source_shortest_path_length(G, root)
    pos = {}
    max_width = max(levels.values())
    
    for node, level in levels.items():
        pos[node] = (level, -list(levels.values()).count(level) + levels[node])
    
    return pos

# Draw the graph
pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
plt.figure(figsize=(10, 6))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    node_color=node_colors,
    font_size=10,
    font_color="black",
    edge_color="gray"
)


# Add legend
legend_handles = [mpatches.Patch(color=color, label=agent) for agent, color in agent_colors.items()]
plt.legend(handles=legend_handles, loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=2, fontsize=10)
plt.title("Sequential Process Flow with Agent Responsibility", fontsize=12)
plt.tight_layout()

# Save the graph as SVG
svg_path = "Public_Communication_Crew_Flow.svg"
plt.savefig(svg_path, format="svg")
plt.show()
