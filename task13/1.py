from ipaddress import ip_network

last = None
for i in range(0, 33):
    net1 = ip_network(f'161.137.200.35/{i}', False)
    net2 = ip_network(f'161.137.150.118/{i}', False)
    if net1 == net2:
        last = net1
k = 0
for ad in last:
    t = f'{int(ad):0>32b}'
    if t.count('1') % 3 == 0:
        k += 1
print(k)