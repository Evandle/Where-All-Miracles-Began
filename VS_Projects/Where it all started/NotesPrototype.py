
child = [str(i) for i in [5, 3, 2, 0, 3, 3, 0, 6, 4, 3, 0]]
waifu_tierlist = [
    "Fuuka",
    "Ichika",
    "Hina",
    "Arisu",
    "Mitsuki",
    "Hoshino",
    "Ain Orh Soph",
    "Mikayo",
    "Mika",
    "Yuuka",
    "Plana",
    "Haruka"
]

list = child.copy()
print(list)
print(
    f"{waifu_tierlist[0]} is the best wife you could ever have and its the truth!"
)
print(
    f"While {waifu_tierlist[1]} is the best waifu!"
)
print(waifu_tierlist)
waifu_tierlist.append("Seia")

print(
    f"The only list that matters {waifu_tierlist}."
)

waifu_tierlist.extend(child)
print(waifu_tierlist)

waifu_tierlist.remove(str(3))

print(
    f"The truth is only {list}"
)

