from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # تعداد راس‌ها
        self.graph = defaultdict(list)  # ساختار ذخیره گراف به شکل لیست مجاورت

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_connected(self):
        # جستجوی همبندی گراف
        visited = [False] * self.V

        # پیدا کردن اولین راسی که درجه آن بیشتر از صفر باشد
        for i in range(self.V):
            if len(self.graph[i]) > 0:
                break
        else:
            return True  # گراف تهی است و همبند محسوب می‌شود

        # جستجوی عمق اول (DFS) برای بررسی همبندی
        self.dfs(i, visited)

        # بررسی اینکه آیا همه راس‌هایی که درجه آنها بیشتر از صفر است، بازدید شده‌اند
        for i in range(self.V):
            if len(self.graph[i]) > 0 and not visited[i]:
                return False
        return True

    def dfs(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)

    def has_eulerian_circuit(self):
        # بررسی همبندی گراف
        if not self.is_connected():
            return False

        # بررسی زوج بودن درجه همه راس‌ها
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                return False
        return True

# مثال استفاده
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.add_edge(0, 4)
g.add_edge(4, 3)

if g.has_eulerian_circuit():
    print("گراف دارای دور اولری است.")
else:
    print("گراف دارای دور اولری نیست.")
