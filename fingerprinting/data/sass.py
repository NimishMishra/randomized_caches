import numpy as np

template = {
    "omnetpp": 72586, "lbm": 78263, "mcf": 10215, "perlbench": 42939, "namd": 88313,
    "povray": 55066, "gcc": 38339, "imagick": 94055, "xz": 73959, "cactu": 23249,
    "xalancbmk": 40856, "nab": 53761, "fotonik": 53975, "x264": 28662, "blender": 76586, "leela": 89023
}


fingerprinting_data = open("sass.log").readlines()

total = 0
correct = 0
for element in fingerprinting_data:
    element = element.split(":")
    true_bench = element[0].strip()
    bench_val = int(element[1].strip())

    last_diff = None
    guess = None
    for key in list(template.keys()):
        if(guess == None):
            guess = key
            last_diff = np.abs(bench_val - template[key])
        elif(np.abs(bench_val - template[key]) < last_diff):
            last_diff = np.abs(bench_val - template[key])
            guess = key
    if(guess == true_bench):
        correct = correct + 1
    total = total + 1

print("(Sass-cache) Accuracy: {acc}".format(acc=correct / total))
