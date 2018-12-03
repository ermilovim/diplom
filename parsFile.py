import networkx as nx
import matplotlib.pyplot as plt

f = open("testfile.txt", "r")

parsFile = f.read()
parsFile = parsFile[3:]
parsFile = parsFile.split("'index'")
transactions = []

for i in range(1, len(parsFile)):
    tmpl = str(parsFile[i])
    trs = tmpl[tmpl.find("[{"):tmpl.rfind("}],")]
    trs = trs[1:]
    # print(trs)
    trs = trs.split('}, {')
    for j in range(len(trs)):
        # print(trs[j])
        trs[j] = trs[j].split("', '")
        # print(trs[j])
        for k in range(len(trs[j])):
            # print(trs[j][k])
            trs[j][k] = trs[j][k].split("': ")
            if trs[j][k][1].isdigit():
                print(trs[j][k][1])
            else:
                trs[j][k][1] = trs[j][k][1][1:]
                print(trs[j][k][1])
        for l in range(len(trs[j]) - 2):
            transactions.append((trs[j][l][1], trs[j][l + 1][1], trs[j][l + 2][1]))
print(transactions)

G = nx.Graph()

for i in range(len(transactions)):
    G.add_edge(transactions[i][0], transactions[i][1])

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
plt.savefig('trs.png')