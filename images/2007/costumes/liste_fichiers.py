import os
i = 0
arr = os.listdir()
for v in arr:
    if 'jpg' in v and len(v) < 7:
        print('    - image: /images/2007/' + arr[i])
    i += 1
