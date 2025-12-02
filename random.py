def calculate_tickets_value(ticket_type, tickets_resolved, priority_level):
    if ticket_type == "technical":
        if priority_level == "low":
            total = 20*tickets_resolved
        elif priority_level == "medium" :
            total = 35*tickets_resolved
        elif priority_level == "high":
            total= 55*tickets_resolved
    if ticket_type == "billing":
        if priority_level == "low":
            total = 15*tickets_resolved
        elif priority_level == "medium":
            total = 25*tickets_resolved
        elif priority_level == "high":
            total = 40*tickets_resolved
    if ticket_type == "general":
        if priority_level == "low":
            total = 10*tickets_resolved
        elif priority_level == "medium":
            total = 18*tickets_resolved
        elif priority_level == "high":
            total = 28*tickets_resolved
    return total 
def calculate_resolution_efficiency(agent_quarters, baseline_tickets, resolved_tickets):
    expected_tickets= 1000 + (agent_quarters * 100)
    ticket_capacity=expected_tickets - baseline_tickets
    efficiency_percentage = (resolved_tickets - baseline_tickets) / ticket_capacity * 100
    return efficiency_percentage
def determine_performance_level(efficiency_percent):
    if efficiency_percent < 50 :
        level= "Developing level"
    if efficiency_percent <60
          
