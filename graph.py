import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("pc.png")


ipstoip0 = [("ip1", "ip0"), ("ip2", "ip0"), ("ip3", "ip0"), ("ip4", "ip0")]
ipsout = [("ip0", "ipout")]

G = nx.Graph()

for item in ipstoip0:
    G.add_edge(item[0], item[1], image=img)
for item in ipsout:
    G.add_edge(item[0], item[1])


nx.draw_circular(G,
                 with_labels=True,
                 node_size=200,
                 node_color='r',
                 node_shape='.',
                 font_size=14,
                 font_color='b',
                 font_family='monospace',
                 font_weight='book',
                 horizontalalignment='left',
                 verticalalignment='center'
                 )

plt.axis('off')
plt.show()
plt.savefig('graph.png')