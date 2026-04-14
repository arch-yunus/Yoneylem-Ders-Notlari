"""
Kuyruk Teorisi Simülasyonu (M/M/1 Bekleme Hattı)
-----------------------------------------------
Bu betik, belirli bir varış hızı (lambda) ve hizmet hızı (mu) ile çalışan 
tek sunuculu bir sistemin (örneğin bir banka veznesi) davranışını simüle eder.

Kütüphane: SimPy
"""

import simpy
import random
import numpy as np

# Parametreler
RANDOM_SEED = 42
ARRIVAL_RATE = 0.5  # Birim zamanda gelen ortalama müşteri (Lambda)
SERVICE_RATE = 0.8  # Birim zamanda hizmet verilen ortalama müşteri (Mu)
SIM_TIME = 100      # Simülasyon toplam süresi (örneğin 100 dakika)

class BankSystem:
    def __init__(self, env, service_rate):
        self.env = env
        self.teller = simpy.Resource(env, capacity=1)
        self.service_rate = service_rate
        self.wait_times = []

    def serve(self, customer):
        # Hizmet süresi üstel dağılıma uyar (Exponential Distribution)
        yield self.env.timeout(random.expovariate(self.service_rate))

def customer(env, name, bank):
    arrival_time = env.now
    # print(f"{name} bankaya geldi. Saat: {arrival_time:.2f}")

    with bank.teller.request() as request:
        yield request
        
        wait_time = env.now - arrival_time
        bank.wait_times.append(wait_time)
        # print(f"{name} hizmet almaya başladı. Bekleme süresi: {wait_time:.2f}")
        
        yield env.process(bank.serve(name))
        # print(f"{name} hizmetini tamamladı. Saat: {env.now:.2f}")

def setup(env, arrival_rate, service_rate):
    bank = BankSystem(env, service_rate)
    i = 0
    while True:
        yield env.timeout(random.expovariate(arrival_rate))
        i += 1
        env.process(customer(env, f'Musteri_{i}', bank))
    return bank # This will not be reached in while True loop but environment holds state

def run_simulation():
    # Rastgelelik sabitleme
    random.seed(RANDOM_SEED)
    
    # Ortam (Environment) oluşturma
    env = simpy.Environment()
    
    # Banka ve geliş sürecini tanımlama
    bank = BankSystem(env, SERVICE_RATE)
    
    # Geliş sürecini manuel başlatıyoruz
    def generator(env, bank):
        i = 0
        while True:
            yield env.timeout(random.expovariate(ARRIVAL_RATE))
            i += 1
            env.process(customer(env, f'Musteri_{i}', bank))

    env.process(generator(env, bank))
    
    # Simülasyonu çalıştır
    print(f"--- Simülasyon Başlatıldı (Süre: {SIM_TIME} dk) ---")
    env.run(until=SIM_TIME)
    
    # İstatistikler
    avg_wait = np.mean(bank.wait_times)
    max_wait = np.max(bank.wait_times)
    
    print("\n--- İstatistikler ---")
    print(f"Toplam Hizmet Alan Müşteri: {len(bank.wait_times)}")
    print(f"Ortalama Bekleme Süresi: {avg_wait:.2f} dakika")
    print(f"Maksimum Bekleme Süresi: {max_wait:.2f} dakika")
    
    # Teorik Bekleme Süresi (Little's Law ve M/M/1 Formülleri)
    # Wq = lambda / (mu * (mu - lambda))
    theoretical_wait = ARRIVAL_RATE / (SERVICE_RATE * (SERVICE_RATE - ARRIVAL_RATE))
    print(f"Teorik Bekleme Süresi (M/M/1): {theoretical_wait:.2f} dakika")

if __name__ == "__main__":
    run_simulation()
