def part(arr):
    k = ["Partridge", "PearTree", "Chat", "Dan", "Toblerone", "Lynn", "AlphaPapa", "Nomad"]
    z = [x for x in arr if x in k]
    return "Mine's a Pint" + "!"*len(z) if z else "Lynn, I've pierced my foot on a spike!!"
