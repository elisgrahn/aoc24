with open("1.txt") as f:
    lists = ((int(v) for v in row.split()) for row in f.readlines())
    
sorted_lists = [sorted(l) for l in zip(*lists)]

distances = (abs(v1 - v2) for v1, v2 in zip(*sorted_lists))

tot_distances = sum(distances)

print(tot_distances)

def count(sorted_list: list) -> dict:
    d = {}
    i = 0
    while i < len(sorted_list):

        n = 1
        v = sorted_list[i]        
        while i+n < len(sorted_list) and v == sorted_list[i+n]:
            n += 1

        d[v] = n
        i += n
    return d

left, right = (count(l) for l in sorted_lists)

similarity = sum(n * v * right.get(v, 0) for v, n in left.items())

print(similarity)