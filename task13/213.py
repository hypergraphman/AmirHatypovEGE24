from ipaddress import ip_network

last = None
for i in range(0, 33):
    net1 = ip_network(f'154.63.206.129/{i}', False)
    net2 = ip_network(f'154.63.100.75/{i}', False)
    if net1 != net2:
        last = net1
k = 0
for ad in last:
    t = f'{int(ad):0<32b}'
print(t, sep = '.')