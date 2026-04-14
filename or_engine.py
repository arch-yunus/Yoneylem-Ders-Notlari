"""
🏗️ Yoneylem-Ders-Notlari: Master OR Engine
Central CLI for Operations Research Solvers and Notes.
"""

import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("""
    ========================================================
    🏗️  OPERATIONS RESEARCH MASTER ENGINE v1.0
    ========================================================
    Kapsamlı Optimizasyon ve Karar Bilimi Arşivi
    "Linearity is everywhere, optimization is the limit."
    ========================================================
    """)

def main_menu():
    while True:
        clear_screen()
        print_banner()
        print(" [1] 📏 Doğrusal Programlama (Simplex/Dual/Sensitivity)")
        print(" [2] 🕸️ Ağ Optimizasyonu (Kısa Yol/Max-Flow)")
        print(" [3] 🔢 Tamsayılı Programlama (Sırt Çantası/Lokasyon)")
        print(" [4] 🎲 Stokastik Modeller (Kuyruk/Markov)")
        print(" [5] ♟️ Oyun Teorisi & Strateji")
        print(" [Q] ❌ Çıkış")
        print("-" * 56)
        
        choice = input("Seçiminizi yapın: ").strip().upper()
        
        if choice == 'Q':
            print("Optimum kalın mühendis!")
            break
        elif choice == '1': sub_menu_lp()
        elif choice == '2': sub_menu_network()
        elif choice == '3': sub_menu_integer()
        elif choice == '4': sub_menu_stochastic()
        elif choice == '5': run_tool('05_Game_Theory_and_Simulation/README.md', is_doc=True)
        else:
            input("Geçersiz seçim. Devam etmek için Enter'a basın...")

def run_tool(path, is_doc=False):
    clear_screen()
    if is_doc:
        print(f"📖 Dökümantasyon Açılıyor: {path}\n")
        # In a real environment, this might open a browser or local viewer
        print("Döküman içeriği klasör içinde README.md olarak mevcuttur.")
    else:
        print(f"🚀 Modül başlatılıyor: {path}\n")
        os.system(f"python \"{path}\"")
    input("\nAna menüye dönmek için Enter'a basın...")

def sub_menu_lp():
    while True:
        clear_screen()
        print("📏 Doğrusal Programlama Araç Kutusu")
        print("[1] Primal-Dual Çözücü")
        print("[2] Duyarlılık (Sensitivity) Analizi")
        print("[B] Geri")
        c = input("> ").upper()
        if c == '1': run_tool('01_Linear_Programming/dual_problem_generator.py')
        elif c == '2': run_tool('01_Linear_Programming/sensitivity_analyzer.py')
        elif c == 'B': break

def sub_menu_network():
    while True:
        clear_screen()
        print("🕸️ Ağ Optimizasyonu Araç Kutusu")
        print("[1] En Kısa Yol (Dijkstra)")
        print("[2] Maksimum Akış (Max-Flow)")
        print("[B] Geri")
        c = input("> ").upper()
        if c == '1': run_tool('02_Network_Optimization/graph_algorithms/shortest_path_explorer.py')
        elif c == '2': run_tool('02_Network_Optimization/graph_algorithms/max_flow_solver.py')
        elif c == 'B': break

def sub_menu_integer():
    while True:
        clear_screen()
        print("🔢 Tamsayılı Programlama Araç Kutusu")
        print("[1] 0-1 Sırt Çantası (Knapsack)")
        print("[2] Tesis Lokasyon Seçimi")
        print("[B] Geri")
        c = input("> ").upper()
        if c == '1': run_tool('03_Integer_Programming/knapsack_solver.py')
        elif c == '2': run_tool('03_Integer_Programming/facility_location_problem.py')
        elif c == 'B': break

def sub_menu_stochastic():
    while True:
        clear_screen()
        print("🎲 Stokastik Modeller Araç Kutusu")
        print("[1] Markov Zinciri Analizi")
        print("[2] Kuyruk Teorisi Simülasyonu")
        print("[B] Geri")
        c = input("> ").upper()
        if c == '1': run_tool('04_Stochastic_Models/markov_chain_analyzer.py')
        elif c == '2': run_tool('04_Stochastic_Models/queuing_theory_simulation.py')
        elif c == 'B': break

if __name__ == "__main__":
    main_menu()
