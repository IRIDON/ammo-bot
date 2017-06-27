def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]



arr = [1, 2, 3, 4, 5, 6]

import pprint
pprint.pprint(list(chunks(arr, 2)))
