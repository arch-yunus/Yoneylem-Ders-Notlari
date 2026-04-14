"""
🧬 Yoneylem-Ders-Notlari: Metaheuristic Tool
Traveling Salesman Problem (TSP) Solver using Genetic Algorithm
"""

import numpy as np
import random

class GeneticTSP:
    def __init__(self, cities, population_size=50, generations=100, mutation_rate=0.01):
        self.cities = cities
        self.n_cities = len(cities)
        self.pop_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def calculate_distance(self, route):
        dist = 0
        for i in range(self.n_cities):
            c1 = self.cities[route[i]]
            c2 = self.cities[route[(i + 1) % self.n_cities]]
            dist += np.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)
        return dist

    def create_initial_population(self):
        pop = []
        for _ in range(self.pop_size):
            route = list(range(self.n_cities))
            random.shuffle(route)
            pop.append(route)
        return pop

    def evolve(self):
        population = self.create_initial_population()
        
        for _ in range(self.generations):
            # 1. Selection (Tournament)
            population = sorted(population, key=lambda x: self.calculate_distance(x))
            best_routes = population[:self.pop_size // 2]
            
            new_population = []
            while len(new_population) < self.pop_size:
                # Crossover
                p1, p2 = random.sample(best_routes, 2)
                child = self.ordered_crossover(p1, p2)
                
                # Mutation
                if random.random() < self.mutation_rate:
                    child = self.swap_mutation(child)
                
                new_population.append(child)
            population = new_population

        best_route = min(population, key=lambda x: self.calculate_distance(x))
        return best_route, self.calculate_distance(best_route)

    def ordered_crossover(self, p1, p2):
        start, end = sorted(random.sample(range(self.n_cities), 2))
        child = [None] * self.n_cities
        child[start:end] = p1[start:end]
        
        ptr = end
        for city in p2:
            if city not in child:
                if ptr >= self.n_cities: ptr = 0
                child[ptr] = city
                ptr += 1
        return child

    def swap_mutation(self, route):
        i, j = random.sample(range(self.n_cities), 2)
        route[i], route[j] = route[j], route[i]
        return route

def main():
    print("--- ⚙️ Yöneylem Araştırması: Gezgin Satıcı Problemi (Genetik Algoritma) ---")
    
    # Random 10 cities coordinates
    cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]
    
    ga = GeneticTSP(cities, population_size=100, generations=200)
    best_route, best_dist = ga.evolve()
    
    print(f"\n✅ Evrimsel Süreç Tamamlandı:")
    print(f"🔹 En Kısa Rota (Index): {best_route}")
    print(f"🔹 Toplam Mesafe: {best_dist:.2f}")
    print("-" * 50)
    print("🚀 Gelişmiş Meta-Sezgisel Analiz — Industrial Engineering Intelligence")

if __name__ == "__main__":
    main()
