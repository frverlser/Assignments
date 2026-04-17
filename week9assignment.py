from dataclasses import dataclass, field

@dataclass
class Tool:
    name: str
    rate: float
    hours: int
    def cost(self):
        return round(self.rate * self.hours, 2)
@dataclass
class Workshop:
    name: str
    tools: list = field(default_factory=list)
    total_cost: float = field(init=False)
    def __post_init__(self):
        self._refresh()
    def _refresh(self):
        self.total_cost = round(sum(tool.cost() for tool in self.tools), 2)
    def add_tool(self, tool):
        self.tools.append(tool)
        self._refresh()
    def use(self, tool_name, hrs):
        for tool in self.tools:
            if tool.name == tool_name and tool.hours >= hrs:
                tool.hours -= hrs
                self._refresh()
                return True
            if tool.name == tool_name:
                return False
        return False

    def extend(self, tool_name, hrs):
        for tool in self.tools:
            if tool.name == tool_name:
                tool.hours += hrs
                self._refresh()
                return

    def report(self):
        result = f"{self.name} Rentals:\n"
        for tool in self.tools:
            result += f"  {tool.name}: {tool.hours} hrs @ ${tool.rate}/hr\n"
        result += f"Total cost: ${self.total_cost}"
        return result
    
    
t1 = Tool("Drill", 18.50, 12)
t2 = Tool("Saw", 25.99, 8)
t3 = Tool("Sander", 12.75, 20)

w = Workshop("BuildRight")
w.add_tool(t1)
w.add_tool(t2)
w.add_tool(t3)

print(w.total_cost)
print(w.use("Drill", 4))
print(w.use("Drill", 15))
w.extend("Sander", 10)
print(w.report())
