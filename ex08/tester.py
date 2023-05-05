from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


for elem in ft_tqdm(range(333333)):
    sleep(0.0000001)
print()
for elem in tqdm(range(333333333)):
    sleep(0.00005)
print()
