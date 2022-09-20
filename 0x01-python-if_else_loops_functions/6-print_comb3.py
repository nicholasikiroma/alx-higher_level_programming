#!/usr/bin/python3
for j in range(0, 8):
    for i in range(j + 1, 10):
        print(f"{j:d}{i:d}", end= ', ')
print(f"{j+1:d}{i:d}")
