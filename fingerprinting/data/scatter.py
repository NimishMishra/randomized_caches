import numpy as np

template = {
    "omnetpp": 783011, "lbm": 646983, "mcf": 785109, "perlbench": 394934, "namd": 958511,
    "povray": 765196, "gcc": 998275, "imagick": 490422, "xz": 416343, "cactu": 508592,
    "xalancbmk": 936716, "nab": 742626, "fotonik": 744025, "x264": 462308, "blender": 44308, "leela": 854725
}


fingerprinting_data = open("scatter.log").readlines()

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

print("(Scatter-cache) Accuracy: {acc}".format(acc=correct / total))
