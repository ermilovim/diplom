import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fileWithIps = open("ipList.txt", "r")


def getIpList(file):
    clients = []
    servers = []
    routers = []
    connections = []
    for line in file:
        if line[0:1] == "0" and line[1] == ":":
            nonZeroLine = line.split(":")
            nonZeroLine.pop(0)
            nonZeroLine = str(nonZeroLine)
            zeroLine = nonZeroLine.split(".")
            zeroLine[0] = zeroLine[0][2:]
            zeroLine[3] = zeroLine[3][:-4]

            x = zeroLine[3].find("-")

            if x != -1:
                lastIpNumbers = zeroLine[3].split("-")
                for i in range(int(lastIpNumbers[0]), int(lastIpNumbers[1]) + 1):
                    ip_i = str(zeroLine[0] + "." + zeroLine[1] + "." + zeroLine[2] + "." + str(i))
                    clients.append(ip_i)
            else:
                s = ".".join(zeroLine)
                clients.append(s)

        if line[0] == "1" and line[1] == ":":
            nonZeroLine = line.split(":")
            nonZeroLine.pop(0)
            nonZeroLine = str(nonZeroLine)
            zeroLine = nonZeroLine.split(".")
            zeroLine[0] = zeroLine[0][2:]
            zeroLine[3] = zeroLine[3][:-4]

            x = zeroLine[3].find("-")

            if x != -1:
                lastIpNumbers = zeroLine[3].split("-")
                for i in range(int(lastIpNumbers[0]), int(lastIpNumbers[1]) + 1):
                    ip_i = str(zeroLine[0] + "." + zeroLine[1] + "." + zeroLine[2] + "." + str(i))
                    servers.append(ip_i)
            else:
                s = ".".join(zeroLine)
                servers.append(s)

        if line[0] == "2" and line[1] == ":":
            nonZeroLine = line.split(":")
            nonZeroLine.pop(0)
            nonZeroLine = str(nonZeroLine)
            zeroLine = nonZeroLine.split(".")
            zeroLine[0] = zeroLine[0][2:]
            zeroLine[3] = zeroLine[3][:-4]

            x = zeroLine[3].find("-")

            if x != -1:
                lastIpNumbers = zeroLine[3].split("-")
                for i in range(int(lastIpNumbers[0]), int(lastIpNumbers[1]) + 1):
                    ip_i = str(zeroLine[0] + "." + zeroLine[1] + "." + zeroLine[2] + "." + str(i))
                    routers.append(ip_i)
            else:
                s = ".".join(zeroLine)
                routers.append(s)

        isConn = line.find("--")
        if isConn > 0:
            connectionLine = line.split("--")
            connectionLine[1] = connectionLine[1][:-2]
            connections.append((connectionLine[0], connectionLine[1]))

    return clients, servers, routers, connections


def buildGraph(mainArray):
    pc = mpimg.imread('pc.png')
    router = mpimg.imread("router.jpg")
    server = mpimg.imread("server.png")

    G = nx.Graph
    for router in range(len(mainArray[2])):
        routerIP = mainArray[2][router].split(".")
        print(routerIP)
        for j in range(len(mainArray[0])):
            clientIP = mainArray[0][j].split(".")
            if clientIP[0] == routerIP[0] and clientIP[1] == routerIP[1] and clientIP[2] == routerIP[2]:
                clientIPstr = ".".join(clientIP)
                routerIPstr = ".".join(routerIP)
                G.add_edge("192.168.11.10", "192.168.11.1", image=pc, size=0.1)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)

    # add images on edges
    ax = plt.gca()
    fig = plt.gcf()
    label_pos = 0  # middle of edge, halfway between nodes
    trans = ax.transData.transform
    trans2 = fig.transFigure.inverted().transform
    imsize = 0.2  # this is the image size
    for (n1, n2) in G.edges():
        (x1, y1) = pos[n1]
        (x2, y2) = pos[n2]
        (x, y) = (x1 * label_pos + x2 * (1.0 - label_pos),
                  y1 * label_pos + y2 * (1.0 - label_pos))
        xx, yy = trans((x, y))  # figure coordinates
        xa, ya = trans2((xx, yy))  # axes coordinates
        imsize = G[n1][n2]['size']
        img = G[n1][n2]['image']
        a = plt.axes([xa - imsize / 2.0, ya - imsize / 2.0, imsize, imsize])
        a.imshow(img)
        a.set_aspect('equal')
        a.axis('off')
    plt.savefig('save.png')
    plt.axis('off')
    plt.show()


buildGraph(getIpList(fileWithIps))
