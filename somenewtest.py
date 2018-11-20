import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


pc = mpimg.imread('pc.png')
router = mpimg.imread("router.jpg")
server = mpimg.imread("server.png")

G = nx.Graph()

G.add_node("192.168.10.1")
G.add_node("178.10.10.15")
for i in range(2, 16):
    G.add_edge("192.168.10.{}".format(i), "192.168.10.1", image=pc, size=0.1)

G.add_edge("192.168.10.25", "192.168.10.1", image=server, size=0.1)

# G.add_node("178.10.10.15", image=router, size = 0.2)
G.add_edge("192.168.10.1", "178.10.10.15", image=router, size=0.2)

# !!!Остался один вопрос!!!
# Строчка кода, которая выше должна добавлять в вершину 192.168.10.1 картинку router, а она добавляет наоборот
# в вершину 178.10.10.15, что не понятно мне. Такая же херня была и когда я добавлял пк, но эта проблема испарилась сама
# собой.
G.add_node("192.168.11.1")
G.add_edge("192.168.11.10", "192.168.11.1", image=pc, size=0.1)
G.add_edge("192.168.11.12", "192.168.11.1", image=pc, size=0.1)

G.add_edge("192.168.11.1", "178.10.10.15", image=router, size=0.2)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

# add images on edges
ax = plt.gca()
fig = plt.gcf()
label_pos = 0  # middle of edge, halfway between nodes
trans = ax.transData.transform
trans2 = fig.transFigure.inverted().transform
imsize = 0.2  # this is the image size
for (n1,n2) in G.edges():
    (x1,y1) = pos[n1]
    (x2,y2) = pos[n2]
    (x,y) = (x1 * label_pos + x2 * (1.0 - label_pos),
             y1 * label_pos + y2 * (1.0 - label_pos))
    xx,yy = trans((x,y)) # figure coordinates
    xa,ya = trans2((xx,yy)) # axes coordinates
    imsize = G[n1][n2]['size']
    img =  G[n1][n2]['image']
    a = plt.axes([xa-imsize/2.0,ya-imsize/2.0, imsize, imsize ])
    a.imshow(img)
    a.set_aspect('equal')
    a.axis('off')
plt.savefig('save.png')
plt.axis('off')
plt.show()
