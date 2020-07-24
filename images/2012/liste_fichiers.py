import os
i = 0
arr = os.listdir()
for v in arr:
    print('    - image: /images/2012/' + arr[i])
    i += 1
