def convolv(sign, conv):
    len1 = len(sign)
    len2 = len(conv)
    result_length = len1 + len2 - 1
    result = [0] * result_length

    for i in range(result_length):
        result[i] = 0
        for j in range(len2):
            if i - j >= 0 and i - j < len1:
                result[i] += sign[i - j] * conv[j]

    return result

print("Naive Implementation of convolution")
print("Nama : Julio Maulana Bagus Penag") 
print("5009211144")

sign = [1, 2, 3, 4, 5]
conv = [0.5, 0.25, 0.125]

hasil = convolv(sign, conv)
print("hasil convolve(signal, conv)")

import numpy as np

np_result = np.convolve(sign, conv, mode='full')
print("hasil convolve numpy:", np_result)

