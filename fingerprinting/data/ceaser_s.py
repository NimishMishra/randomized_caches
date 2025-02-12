import numpy as np

template = {
    "omnetpp": 783061, "lbm": 646773, "mcf": 785309, "perlbench": 394134, "namd": 958411, 
    "povray": 765996, "gcc": 998475, "imagick": 490222, "xz": 416743, "cactu": 508392,
    "xalancbmk": 936926, "nab": 743621, "fotonik": 741052, "x264": 462348, "blender": 43356, "leela": 851345
}


fingerprinting_data = open("ceaser_s.log").readlines()

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

print("(CEASER-S) Accuracy: {acc}".format(acc=correct / total))
