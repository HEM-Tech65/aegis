def omissions(label):
    # gra -> ra, ga, gr
    return {label[:i] + label[i+1:] for i in range(len(label))}

def repeats(label):
    # gra -> ggra, grra, graa
    return {label[:i] + label[i] * 2 + label[i+1:] for i in range(len(label))}

def swaps(label):
    # gra -> rga, gar
    return {label[:i] + label[i+1] + label[i] + label[i+2:]
            for i in range(len(label) - 1)}

def affixes(label):
    # gra -> gra-portal, grapay, ...
    out = set()
    for word in ["portal", "pay", "verify", "online"]:
        out.add(f"{label}-{word}")
        out.add(f"{label}{word}")
    return out

def generate(label, suffixes):
    variants = omissions(label) | repeats(label) | swaps(label) | affixes(label)
    variants.discard(label)   # don't include the real name
    variants.discard("")
    return {f"{v}.{s}" for v in variants for s in suffixes}