## Question
## These are the loads of servers in the dict. You need to distribute the load in such a way that the server with lowest load gets first.

servers = {"s1": 10, "s2": 11, "s3": 8, "s4": 12, "s5": 7}
load = 15

## when we iterate over servers dict, 


while load > 0:
    for k, v in servers.items():
        min_value = min(servers, key=servers.get)
        servers.update({min_value: servers.get(min_value)+1})
        print(f'{load} ==> {servers}')
        load = load - 1

print(servers)
