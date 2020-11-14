a ={
    "A": [("B",20), ('C',15)],
    'B': [('D',12),("E",32)],
    'C': [("B",18),("D",28),("G",35)],
    'D': [("E",17),("F",45),("H",45)],
    'E': [("F",12)],
    'F':[("H",11),("I",17)],
    'G':[('H',9),('J',12)],
    'H':[("K",5),("I",8)],
    'I':[("L",7)],
    "J":[("K",7),("L",18)],
    "K":[("L",11)]
    }

def find_path(a,start, end, p=[]):
    print("starting", start, end)
    p = p + [start]
    print(p)
    if start == end:
        print("  equal returned 0")
        return p, 0
    if start not in a:
        print("   returned None")
        return None, None
    shortpath = None
    shortdist = None

    for vert, dist in a[start]:
        if vert not in p:
            newpath, dist1 = find_path(a, vert, end, p)
            if newpath is not None:
                print("   going from",start,"to", vert, dist, "+", dist1, "=", dist+dist1)
                dist1 += dist
                if not shortdist or dist1 < shortdist:
                    shortpath = newpath
                    shortdist = dist1
    print("NEWPATH IS", newpath)
    print("return", shortpath, shortdist, "when started from", start)
    return shortpath, shortdist
print("Result SHORTEST PATH", find_path(a, 'A', 'L'))
