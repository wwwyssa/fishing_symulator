fish_fields = ["image_name", "speed", "cost"]
fish_descriptions = [None for i in range(9)]
for i in range(9):
    fish_descriptions[i] = {"image_name": f"{i + 1}.png", "speed": (i + 1, -(i + 1)), "cost": (10, 100)}
print(fish_descriptions)