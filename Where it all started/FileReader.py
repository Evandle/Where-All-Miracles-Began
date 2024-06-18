
def file_to_dict(filename):
    mc_bio = {}
    with open(filename, "r") as file:
        for line in file:
            key, value = line.strip().split(":", 1)
            mc_bio[key] = value.strip()
    return mc_bio

my_dict = file_to_dict("test1.txt")
print(my_dict.get('Name'))
