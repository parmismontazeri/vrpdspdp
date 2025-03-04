import random
import numpy as np

class VehicleRoutingTS:
    def __init__(self, num_customers, num_vehicles, capacity, demand_matrix, distance_matrix):
        self.num_customers = num_customers
        self.num_vehicles = num_vehicles
        self.capacity = capacity
        self.demand_matrix = demand_matrix
        self.distance_matrix = distance_matrix
        self.solution = self.generate_initial_solution()
        self.tabu_list = []
        self.best_solution = self.solution
        self.best_cost = self.calculate_total_cost(self.solution)

    def generate_initial_solution(self):
        solution = [[] for _ in range(self.num_vehicles)]
        remaining_customers = list(range(1, self.num_customers))  
        random.shuffle(remaining_customers)
        
        for vehicle in solution:
            capacity_left = self.capacity
            while remaining_customers:
                customer = remaining_customers.pop()
                if self.demand_matrix[customer] <= capacity_left:
                    vehicle.append(customer)
                    capacity_left -= self.demand_matrix[customer]
        
        return solution

    def calculate_total_cost(self, solution):
        cost = 0
        for route in solution:
            if not route:
                continue
            cost += self.distance_matrix[0][route[0]]  
            for i in range(len(route) - 1):
                cost += self.distance_matrix[route[i]][route[i + 1]]
            cost += self.distance_matrix[route[-1]][0]  
        return cost

    def swap_move(self, solution):
        new_solution = [route[:] for route in solution]
        vehicle1, vehicle2 = random.sample(range(self.num_vehicles), 2)
        if new_solution[vehicle1] and new_solution[vehicle2]:
            idx1 = random.randint(0, len(new_solution[vehicle1]) - 1)
            idx2 = random.randint(0, len(new_solution[vehicle2]) - 1)
            new_solution[vehicle1][idx1], new_solution[vehicle2][idx2] = new_solution[vehicle2][idx2], new_solution[vehicle1][idx1]
        return new_solution

    def run_tabu_search(self, max_iterations=100, tabu_tenure=5):
        for _ in range(max_iterations):
            candidate_solutions = [self.swap_move(self.solution) for _ in range(5)]
            candidate_solutions = [sol for sol in candidate_solutions if sol not in self.tabu_list]
            
            if not candidate_solutions:
                continue
            
            best_candidate = min(candidate_solutions, key=self.calculate_total_cost)
            best_candidate_cost = self.calculate_total_cost(best_candidate)
            
            if best_candidate_cost < self.best_cost:
                self.best_solution = best_candidate
                self.best_cost = best_candidate_cost
            
            self.tabu_list.append(best_candidate)
            if len(self.tabu_list) > tabu_tenure:
                self.tabu_list.pop(0)
        
        return self.best_solution, self.best_cost

# Example usage
num_customers = 10
num_vehicles = 3
capacity = 15
demand_matrix = [0] + [random.randint(1, 5) for _ in range(num_customers - 1)]
distance_matrix = np.random.randint(5, 20, size=(num_customers, num_customers))
np.fill_diagonal(distance_matrix, 0)

vrp_solver = VehicleRoutingTS(num_customers, num_vehicles, capacity, demand_matrix, distance_matrix)
best_solution, best_cost = vrp_solver.run_tabu_search()

print("Best solution:", best_solution)
print("Best cost:", best_cost)
