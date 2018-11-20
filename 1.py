import networkx as nx
import matplotlib.pyplot as plt
import os


def get_tree(tree=[u"E:\Ваня\Учеба\диплом\python\diplom", ], G = nx.Graph(), itr=0, max_itr=900):
    point = tree.pop(0)
    itr = itr + 1
    sub_tree = [os.path.join(point, x) for x in os.listdir(point) if
                os.path.isdir(os.path.join(point, x)) and not is_hidden_dir(os.path.join(point, x))]
    if sub_tree:
        tree.extend(sub_tree)
        G.add_edges_from(map(lambda b: (point, b), sub_tree))
    if tree and itr <= max_itr:
        return get_tree(tree, G, itr)
    else:
        return G


def is_hidden_dir(d):
    import sys, subprocess
    if sys.platform.startswith("win"):
        p = subprocess.check_output(["attrib", d.encode('cp1251') if isinstance(d, unicode) else d])
        return True if 'H' in p[:12] else False
    else:
        return True if os.path.basename(d)[0] == '.' else False


def main():
    G = get_tree()
    nx.draw(G, with_labels=False, node_color="blue", alpha=0.6, node_size=50)
    plt.savefig("edge_colormap.png")
    plt.show()


main()
