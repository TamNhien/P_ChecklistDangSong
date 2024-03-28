L = list(map(int, input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy: ").split(',')))
print(all((L[i] > L[i - 1] and L[i] > L[i + 1]) or (L[i] < L[i - 1] and L[i] < L[i + 1]) for i in range(1, len(L) - 1)))

