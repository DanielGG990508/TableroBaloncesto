# -*- coding: utf-8 -*-
"""
Autor: Daniel Garcia Garcia 

Descripccion: tablero de baloncesto interfaz grafica 

This is a temporary script file.
"""
import tkinter as tk

class BasketballScoreboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Marcador de Baloncesto")

        self.score_team_a = 0
        self.score_team_b = 0

        self.time_remaining = 600  # 10 minutos en segundos
        self.shot_clock = 24  # 24 segundos de tiempo de tiro

        self.direction = "Equipo A"  # Inicialmente, la dirección es para el "Equipo A"

        self.create_widgets()

    def create_widgets(self):
        self.label_team_a = tk.Label(self.root, text="Equipo A: 0", font=("Arial", 24))
        self.label_team_a.pack(pady=10)

        self.label_team_b = tk.Label(self.root, text="Equipo B: 0", font=("Arial", 24))
        self.label_team_b.pack(pady=10)

        self.label_time = tk.Label(self.root, text="Tiempo restante: 10:00", font=("Arial", 24))
        self.label_time.pack(pady=10)

        self.label_shot_clock = tk.Label(self.root, text="Tiro: 24", font=("Arial", 24))
        self.label_shot_clock.pack(pady=10)

        button_team_a_plus = tk.Button(self.root, text="+1", font=("Arial", 18), command=self.increment_score_team_a)
        button_team_a_plus.pack(side=tk.LEFT, padx=10)

        button_team_a_minus = tk.Button(self.root, text="-1", font=("Arial", 18), command=self.decrement_score_team_a)
        button_team_a_minus.pack(side=tk.LEFT, padx=10)

        button_team_b_plus = tk.Button(self.root, text="+1", font=("Arial", 18), command=self.increment_score_team_b)
        button_team_b_plus.pack(side=tk.RIGHT, padx=10)

        button_team_b_minus = tk.Button(self.root, text="-1", font=("Arial", 18), command=self.decrement_score_team_b)
        button_team_b_minus.pack(side=tk.RIGHT, padx=10)

        self.button_change_direction = tk.Button(self.root, text="Cambiar Dirección", font=("Arial", 18), command=self.change_direction)
        self.button_change_direction.pack(pady=10)

        self.button_start_time = tk.Button(self.root, text="Iniciar Tiempo", font=("Arial", 18), command=self.start_time)
        self.button_start_time.pack(pady=10)

    def increment_score_team_a(self):
        self.score_team_a += 1
        self.update_scoreboard()

    def decrement_score_team_a(self):
        if self.score_team_a > 0:
            self.score_team_a -= 1
            self.update_scoreboard()

    def increment_score_team_b(self):
        self.score_team_b += 1
        self.update_scoreboard()

    def decrement_score_team_b(self):
        if self.score_team_b > 0:
            self.score_team_b -= 1
            self.update_scoreboard()

    def change_direction(self):
        if self.direction == "Equipo A":
            self.direction = "Equipo B"
        else:
            self.direction = "Equipo A"
        self.update_direction()

    def update_direction(self):
        self.button_change_direction.config(text=f"Cambiar Dirección ({self.direction})")

    def update_scoreboard(self):
        self.label_team_a.config(text=f"Equipo A: {self.score_team_a}")
        self.label_team_b.config(text=f"Equipo B: {self.score_team_b}")

    def update_time(self):
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.label_time.config(text=f"Tiempo restante: {time_str}")

        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.root.after(1000, self.update_time)

    def update_shot_clock(self):
        self.label_shot_clock.config(text=f"Tiro: {self.shot_clock}")

        if self.shot_clock > 0:
            self.shot_clock -= 1
            self.root.after(1000, self.update_shot_clock)

    def start_time(self):
        self.update_time()
        self.update_shot_clock()

    def start(self):
        self.update_direction()
        self.root.mainloop()

root = tk.Tk()
scoreboard = BasketballScoreboard(root)
scoreboard.start()
