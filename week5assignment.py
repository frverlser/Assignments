servers = ["db-01", "app-01", "web-01", "cache-01"]
usages = [12.5, 88.0, 75.5, 15.0]
def update_cpu_usage(servers, usages, server_id, new_usage):
    for i in range(len(servers)):
        if servers[i] == server_id:
            usages[i] = new_usage
            print(usages)
            return True
    return False

def decommission_idle_servers(servers, usages, idle_threshold):
    relevant_usage  = []
    relevant_server = []
    for i in range(len(servers)):
        if usages[i] >= idle_threshold:
            relevant_usage.append(usages[i])
            relevant_server.append(servers[i])
    servers[:] = relevant_server
    usages[:] = relevant_usage
def flag_server_load(servers, usages, high_load_threshold):
    high_load = []
    normal_load = []
    for i in range(len(servers)):
        if usages[i] >= high_load_threshold:
            high_load.append(servers[i])
        else:
            normal_load.append(servers[i])
    return high_load, normal_load

def analyze_server_health(initial_servers, initial_usages, server_to_update, decommission_threshold, high_load_threshold):
    server_id, new_usage = server_to_update
    update_cpu_usage(initial_servers, initial_usages, server_id, new_usage)
    decommission_idle_servers(initial_servers, initial_usages, decommission_threshold)
    high_load, normal_load = flag_server_load(initial_servers, initial_usages, high_load_threshold)
    return high_load, normal_load


# Test Case 1
servers = ["db-01", "app-01", "web-01", "cache-01"]
usages = [12.5, 88.0, 75.5, 15.0]
update_info = ["db-01", 14.0]
idle_max_usage = 18.0
high_load_min_usage = 80.0

high_load, normal_load = analyze_server_health(servers, usages, update_info, idle_max_usage, high_load_min_usage)
print(f"high_load: {high_load}")
print(f"normal_load: {normal_load}")