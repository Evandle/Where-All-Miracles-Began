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
    "Haruka",
    "Black suit"
]
waifu = input("Your waifu: ")

print(
    f"{waifu_tierlist.index(waifu)}"
)
child = [str(i) for i in [5, 3, 2, 0, 3, 3, 0, 6, 4, 3, 0]]
child.sort()
print(
    child
)

for waifu in waifu_tierlist:
    print(waifu)
