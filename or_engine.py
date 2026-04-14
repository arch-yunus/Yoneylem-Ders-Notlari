"""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   ██╗   ██╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██╗     ███████╗    ║
║   ╚██╗ ██╔╝██╔═══██╗████╗  ██║██╔════╝╚██╗ ██╔╝██║     ██╔════╝    ║
║    ╚████╔╝ ██║   ██║██╔██╗ ██║█████╗   ╚████╔╝ ██║     █████╗      ║
║     ╚██╔╝  ██║   ██║██║╚██╗██║██╔══╝    ╚██╔╝  ██║     ██╔══╝      ║
║      ██║   ╚██████╔╝██║ ╚████║███████╗   ██║   ███████╗███████╗    ║
║      ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚══════╝    ║
║                                                                      ║
║          ARAŞTIRMASI  ·  OR ENGINE v3.0 · 8 FAZ DOKTRİNİ            ║
╚══════════════════════════════════════════════════════════════════════╝

  Kapsamlı Optimizasyon, Karar Bilimi & Meta-Sezgisel Ekosistemi
  "Karmaşayı basit denklemlere indirgeme sanatıdır."
"""

import os
import sys
import time

# ══════════════════════════════════════════════
# TERMINAL STILI
# ══════════════════════════════════════════════

CYAN    = "\033[96m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
RED     = "\033[91m"
MAGENTA = "\033[95m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
RESET   = "\033[0m"

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clr()
    print(f"{CYAN}{BOLD}")
    print("  ╔══════════════════════════════════════════════════════╗")
    print("  ║  ⚙️  YÖNEYLEM ARAŞTIRMASI · OR ENGINE v3.0           ║")
    print("  ║      8 Faz · 50+ Algoritma · Production-Ready        ║")
    print("  ╚══════════════════════════════════════════════════════╝")
    print(f"{RESET}")

def section(title: str):
    print(f"\n{YELLOW}{BOLD}  ── {title} {'─'*(46-len(title))}{RESET}")

def ok(msg: str):
    print(f"{GREEN}  ✅ {msg}{RESET}")

def err(msg: str):
    print(f"{RED}  ❌ {msg}{RESET}")

def info(msg: str):
    print(f"{DIM}  {msg}{RESET}")

def pause():
    input(f"\n{DIM}  ↵  Ana menüye dönmek için Enter'a basın...{RESET}")

# ══════════════════════════════════════════════
# MODÜL ÇALIŞTIRUCI
# ══════════════════════════════════════════════

def run_module(path: str, label: str = ""):
    """Python modülünü çalıştır, hata yakalamakla birlikte."""
    clr()
    full_path = os.path.join(os.path.dirname(__file__), path)
    if not os.path.exists(full_path):
        err(f"Dosya bulunamadı: {full_path}")
        pause()
        return

    section(label or path)
    print(f"{DIM}  → {full_path}{RESET}\n")

    t0 = time.perf_counter()
    exit_code = os.system(f'"{sys.executable}" "{full_path}"')
    elapsed   = time.perf_counter() - t0

    print(f"\n{DIM}  Tamamlandı ({elapsed:.2f}s) {'✅' if exit_code == 0 else '❌'}{RESET}")
    pause()

def open_readme(path: str):
    """Modül README'sini ekrana yazdır."""
    clr()
    full_path = os.path.join(os.path.dirname(__file__), path)
    if not os.path.exists(full_path):
        err("README bulunamadı")
        pause()
        return
    with open(full_path, encoding='utf-8') as f:
        print(f.read()[:3000])
    if os.path.getsize(full_path) > 3000:
        info("... (kısaltıldı, tam içerik için VS Code'da açın)")
    pause()

# ══════════════════════════════════════════════
# ALT MENÜLER
# ══════════════════════════════════════════════

def menu_lp():
    while True:
        clr()
        banner()
        section("FAZ 1 · Doğrusal Programlama")
        print("  [1] Primal-Dual Problem Üretici")
        print("  [2] Duyarlılık (Sensitivity) Analizi")
        print("  [3] Simpleks Algoritması (Notebook)")
        print("  [R] README → Teori Notları")
        print("  [B] ← Geri")
        c = input(f"\n{CYAN}  OR-LP > {RESET}").strip().upper()
        if   c == '1': run_module("01_Linear_Programming/dual_problem_generator.py",    "Primal-Dual Çözücü")
        elif c == '2': run_module("01_Linear_Programming/sensitivity_analyzer.py",      "Duyarlılık Analizi")
        elif c == '3': info("Notebook: 01_Linear_Programming/simplex_algorithm_step_by_step.ipynb"); pause()
        elif c == 'R': open_readme("01_Linear_Programming/theory_notes.md")
        elif c == 'B': break

def menu_network():
    while True:
        clr()
        banner()
        section("FAZ 2 · Ağ Optimizasyonu")
        print("  ─── Ulaştırma & Atama ───────────────────────")
        print("  [1] Ulaştırma Modeli (VAM + Simpleks)")
        print("  [2] Macar Algoritması (Atama)")
        print("  ─── Graf Algoritmaları ───────────────────────")
        print("  [3] Dijkstra  — En Kısa Yol")
        print("  [4] Ford-Fulkerson — Max Akış + Min Kesim")
        print("  [5] Kruskal/Prim  — Minimum Yayılan Ağaç")
        print("  [B] ← Geri")
        c = input(f"\n{CYAN}  OR-NET > {RESET}").strip().upper()
        if   c == '1': run_module("02_Network_Optimization/transportation_and_assignment/transportation_solver.py", "Ulaştırma (VAM)")
        elif c == '2': run_module("02_Network_Optimization/transportation_and_assignment/hungarian_algorithm.py",   "Macar Algoritması")
        elif c == '3': run_module("02_Network_Optimization/graph_algorithms/dijkstra_visualizer.py",               "Dijkstra")
        elif c == '4': run_module("02_Network_Optimization/graph_algorithms/max_flow_ford_fulkerson.py",           "Max Akış")
        elif c == '5': run_module("02_Network_Optimization/graph_algorithms/mst_kruskal.py",                       "MST (Kruskal+Prim)")
        elif c == 'B': break

def menu_integer():
    while True:
        clr()
        banner()
        section("FAZ 3 · Tamsayılı & Karma Programlama (MILP)")
        print("  [1] 0-1 Sırt Çantası (Knapsack)")
        print("  [2] Tesis Lokasyonu (Facility Location)")
        print("  [3] Dal & Sınır (Notebook)")
        print("  [B] ← Geri")
        c = input(f"\n{CYAN}  OR-ILP > {RESET}").strip().upper()
        if   c == '1': run_module("03_Integer_Programming/knapsack_solver.py",          "Knapsack (ILP)")
        elif c == '2': run_module("03_Integer_Programming/facility_location_problem.py", "Tesis Lokasyonu")
        elif c == '3': info("Notebook: 03_Integer_Programming/branch_and_bound_visualization.ipynb"); pause()
        elif c == 'B': break

def menu_stochastic():
    while True:
        clr()
        banner()
        section("FAZ 4 · Stokastik Modeller")
        print("  [1] Markov Zinciri Analizi")
        print("  [2] Kuyruk Teorisi Simülasyonu  (M/M/1, M/M/c)")
        print("  [3] Monte Carlo İntegrasyon & Risk Analizi")
        print("  [B] ← Geri")
        c = input(f"\n{CYAN}  OR-STO > {RESET}").strip().upper()
        if   c == '1': run_module("04_Stochastic_Models/markov_chain_analyzer.py",      "Markov Zinciri")
        elif c == '2': run_module("04_Stochastic_Models/queuing_theory_simulation.py",  "Kuyruk Teorisi")
        elif c == '3': run_module("04_Stochastic_Models/monte_carlo_integration.py",    "Monte Carlo")
        elif c == 'B': break

def menu_dp():
    while True:
        clr()
        banner()
        section("FAZ 5 · Dinamik Programlama")
        print("  [1] 0-1 Knapsack  — Tabulation + Backtracking")
        print("  [2] Stok Yönetimi — Wagner-Whitin DP")
        print("  [3] Bellman-Ford  — En Kısa Yol (DP)")
        print("  [R] README → Bellman Optimallik Doktrini")
        print("  [B] ← Geri")
        c = input(f"\n{CYAN}  OR-DP > {RESET}").strip().upper()
        if   c == '1': run_module("05_Dynamic_Programming/knapsack_dp.py",      "Knapsack DP")
        elif c == '2': run_module("05_Dynamic_Programming/inventory_dp.py",     "Stok Yönetimi DP")
        elif c == '3': run_module("05_Dynamic_Programming/shortest_path_dp.py", "Bellman-Ford DP")
        elif c == 'R': open_readme("05_Dynamic_Programming/README.md")
        elif c == 'B': break

def menu_meta():
    while True:
        clr()
        banner()
        section("FAZ 6 · Meta-Sezgisel Algoritmalar")
        print("  [1] Genetik Algoritma  — TSP Çözümü")
        print("  [2] Simüle Edilmiş Tavlama — Kombinatoryal Opt.")
        print("  [B] ← Geri")
        c = input(f"\n{CYAN}  OR-META > {RESET}").strip().upper()
        if   c == '1': run_module("06_Metaheuristics/genetic_algorithm_tsp.py",        "Genetik Algoritma (TSP)")
        elif c == '2': run_module("06_Metaheuristics/simulated_annealing_solver.py",   "Simüle Edilmiş Tavlama")
        elif c == 'B': break

def menu_nlp():
    while True:
        clr()
        banner()
        section("FAZ 7 · Doğrusal Olmayan Programlama")
        print("  [1] Gradyan İnişi — SGD, Momentum, Adam Variants")
        print("  [B] ← Geri")
        c = input(f"\n{CYAN}  OR-NLP > {RESET}").strip().upper()
        if   c == '1': run_module("07_Nonlinear_Programming/gradient_descent_optimizer.py", "Gradyan İnişi")
        elif c == 'B': break

def menu_game():
    while True:
        clr()
        banner()
        section("FAZ 8 · Oyun Teorisi & Strateji")
        print("  [1] Sıfır Toplamlı Oyun  — Minimax + LP + Dominance")
        print("  [2] Nash Dengesi Bulucu  — Saf & Karma Strateji")
        print("  [R] README → Oyun Teorisi Doktrini")
        print("  [B] ← Geri")
        c = input(f"\n{CYAN}  OR-GAME > {RESET}").strip().upper()
        if   c == '1': run_module("08_Game_Theory/zero_sum_game_solver.py",     "Sıfır Toplamlı Oyun")
        elif c == '2': run_module("08_Game_Theory/nash_equilibrium_finder.py",  "Nash Dengesi")
        elif c == 'R': open_readme("08_Game_Theory/README.md")
        elif c == 'B': break

# ══════════════════════════════════════════════
# ANA MENÜ
# ══════════════════════════════════════════════

MENU_ITEMS = [
    ("1", "📏", "FAZ 1", "Doğrusal Programlama (Simplex/Dual)"),
    ("2", "🕸️",  "FAZ 2", "Ağ Optimizasyonu (Dijkstra/MaxFlow/MST)"),
    ("3", "🔢", "FAZ 3", "Tamsayılı Programlama (Knapsack/FLP)"),
    ("4", "🎲", "FAZ 4", "Stokastik Modeller (Kuyruk/Markov/MC)"),
    ("5", "🧩", "FAZ 5", "Dinamik Programlama (Bellman/Wagner-Whitin)"),
    ("6", "🧬", "FAZ 6", "Meta-Sezgisel (GA/SA)"),
    ("7", "📈", "FAZ 7", "Doğrusal Olmayan Programlama (GD/KKT)"),
    ("8", "♟️",  "FAZ 8", "Oyun Teorisi & Nash Dengesi"),
    ("I", "📂", "DATA",  "Veri Setleri Hakkında Bilgi"),
    ("Q", "❌", "ÇIKIŞ", "Optimum kalın mühendis!"),
]

def show_main_menu():
    banner()
    print(f"  {BOLD}8 FAZ · KOMPLE YÖNEYLEM EKOSİSTEMİ{RESET}\n")
    for key, icon, tag, desc in MENU_ITEMS:
        print(f"  [{CYAN}{key}{RESET}] {icon}  {BOLD}{tag:<6}{RESET}  {desc}")
    print()

def data_info():
    clr()
    banner()
    section("DATA/ — Örnek Veri Setleri")
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    if not os.path.exists(data_dir):
        err("data/ klasörü bulunamadı")
    else:
        for f in sorted(os.listdir(data_dir)):
            fp = os.path.join(data_dir, f)
            size = os.path.getsize(fp)
            print(f"    📄 {f:<40} {size:>6} byte")
    pause()

def main():
    DISPATCH = {
        '1': menu_lp,
        '2': menu_network,
        '3': menu_integer,
        '4': menu_stochastic,
        '5': menu_dp,
        '6': menu_meta,
        '7': menu_nlp,
        '8': menu_game,
        'I': data_info,
    }

    while True:
        show_main_menu()
        choice = input(f"  {CYAN}{BOLD}OR-ENGINE > {RESET}").strip().upper()

        if choice == 'Q':
            clr()
            print(f"\n{CYAN}  Optimum kalın, mühendis! 🎯{RESET}\n")
            break
        elif choice in DISPATCH:
            DISPATCH[choice]()
        else:
            err(f"Geçersiz seçim: '{choice}'")
            time.sleep(0.8)


if __name__ == "__main__":
    main()
