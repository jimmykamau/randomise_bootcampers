import random, math

bootcampers = [
    "Alvin Mutisya", "Boswell Gathu Wanyoike", "Mwachi Chrisant", "Tirop Anthony", "Alvin Mutisya", "Emmanuel Muthui Musyoka", "Purity Birir", "Jackline Macharia", "Clinton Gitahi", "Michael Kamau", "Sammy Ukavi", "Simon Muchina", "Rose Kariuki", "Samson Paul", "Clement Nzau", "David Njakai", "Jimnah Magira Kanyua", "Mila.Alloys@Gmail.Com", "Warenga Maina", "Malyun Muhudin", "Angela Mutava", "Odera Ochieng' Michael", "Awuor George Marvin"
]
bfas = { "Ben Kanyolo": [], "Morris Kimani": [], "Lewis Kabui": [], "Jee GIthinji": []}

bc_per_bfa = len(bootcampers)/len(bfas)
print(bc_per_bfa)
while len(bootcampers):
    temp_bfas = [bfa for bfa in bfas.keys() if len(bfas[bfa]) < bc_per_bfa] or [bfa for bfa in bfas.keys() if len(bfas[bfa]) < bc_per_bfa+1]
    bfa, bc = random.choice(temp_bfas), random.choice(bootcampers)
    bfas[bfa].append(bc), bootcampers.remove(bc)


print(bfas)
for bfa in bfas:
    print("{}: {} bootcampers".format(bfa, len(bfas[bfa])))
