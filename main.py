from generator import generate
from checker import lookup

brand = "gra"
candidates = generate(brand, ["gov.gh", "com.gh"])
print(f"Generated {len(candidates)} candidate domains\n")

for domain in sorted(candidates):
    ips = lookup(domain)
    if ips:
        print(f"EXISTS: {domain} -> {ips}")