import numpy as np

template = {
        "omnetpp": 802026, "lbm": 645741, "mcf": 777620, "perlbench": 378226, "namd": 969333, 
        "povray": 781802, "gcc": 980122, "imagick": 527218, "xz": 433957, "cactu": 484649,
    "xalancbmk": 951399, "nab": 763164, "fotonik": 764398, "x264": 490491, "blender": 22286, "leela": 915813
}


fingerprinting_data = open("mirage.log").readlines()

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

print("(MIRAGE) Accuracy: {acc}".format(acc=correct / total))
