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

        self.periodo=1

        self.paused = False  # Variable para controlar el estado de pausa

        self.create_widgets()

    def create_widgets(self):

        self.periodoLabel = tk.Label(self.root, text="Periodo: 1", font=("Arial", 24))
        self.periodoLabel.pack(pady=10)

        self.label_team_a = tk.Label(self.root, text="Equipo A: 0", font=("Arial", 24))
        self.label_team_a.pack(pady=10)

        self.label_team_b = tk.Label(self.root, text="Equipo B: 0", font=("Arial", 24))
        self.label_team_b.pack(pady=10)

        self.label_time = tk.Label(self.root, text="Tiempo restante: 10:00", font=("Arial", 24))
        self.label_time.pack(pady=10)

        self.label_shot_clock = tk.Label(self.root, text="Tiro: 24", font=("Arial", 24))
        self.label_shot_clock.pack(pady=10)

        button_team_a_plus = tk.Button(self.root, text="+1", font=("Arial", 18),command=self.increment_score_team_a)
        button_team_a_plus.pack(side=tk.LEFT, padx=10)

        button_team_a_minus = tk.Button(self.root, text="-1", font=("Arial", 18),command=self.decrement_score_team_a)
        button_team_a_minus.pack(side=tk.LEFT, padx=10)

        button_team_b_plus = tk.Button(self.root, text="+1", font=("Arial", 18),command=self.increment_score_team_b)
        button_team_b_plus.pack(side=tk.RIGHT, padx=10)

        button_team_b_minus = tk.Button(self.root, text="-1", font=("Arial", 18),command=self.decrement_score_team_b)
        button_team_b_minus.pack(side=tk.RIGHT, padx=10)

        self.button_change_direction = tk.Button(self.root, text="Cambiar Dirección", font=("Arial", 18),command=self.change_direction)
        self.button_change_direction.pack(pady=10)

        self.button_start_time = tk.Button(self.root, text="Iniciar Tiempo", font=("Arial", 18),command=self.start_pause_timer)
        self.button_start_time.pack(pady=10)


    def start(self):
        self.change_periodo()
        self.update_direction()
        self.root.mainloop()
    #INCREMENTO DE PUNTAJE EQUIPOS
    def increment_score_team_a(self):
        self.score_team_a += 1
        self.update_scoreboard()

    def increment_score_team_b(self):
        self.score_team_b += 1
        self.update_scoreboard()

    #DECREMENTO DE PUNTAJE EQUIPOS
    def decrement_score_team_a(self):
        if self.score_team_a > 0:
            self.score_team_a -= 1
            self.update_scoreboard()

    def decrement_score_team_b(self):
        if self.score_team_b > 0:
            self.score_team_b -= 1
            self.update_scoreboard()
    #ACTUALIZACION DE SCORE
    def update_scoreboard(self):
        self.label_team_a.config(text=f"Equipo A: {self.score_team_a}")
        self.label_team_b.config(text=f"Equipo B: {self.score_team_b}")

    #DIRECCION DEL PARTIDO
    def change_direction(self):
        if self.direction == "Equipo A":
            self.direction = "Equipo B"
        else:
            self.direction = "Equipo A"
        self.update_direction()
    def update_direction(self):
        self.button_change_direction.config(text=f"Cambiar Dirección ({self.direction})")

    #PERIODO EN CURSO
    def change_periodo(self):
        if self.time_remaining==0:
            self.periodo +=1
            self.periodoLabel.config(text=f"periodo ({self.periodo})")
    #     self.update_periodo()
    # def update_periodo(self):
    #     self.config(text=f"Cambiar Dirección ({self.periodo})")

    #FUNCIONES PARA EL CRONOMETRO GLOBAL DEL PERIODO
    def start_pause_timer(self):
        if self.button_start_time["text"] == "Iniciar Tiempo" or self.button_start_time["text"] == "Reanudar Tiempo":
            self.button_start_time["text"] = "Pausa"
            self.resume_timer()
        elif self.button_start_time["text"] == "Pausa":
            self.button_start_time["text"] = "Reanudar Tiempo"
            self.paused = True  # Pausar el decremento

    def update_time(self):
        if not self.paused:  # Continuar solo si no está en pausa
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.label_time.config(text=f"Tiempo restante: {time_str}")

            if self.time_remaining > 0:
                self.time_remaining -= 1
                self.root.after(1000, self.update_time)  # Llamar recursivamente
            else:
                self.button_start_time["text"] == "Iniciar Tiempo"
                self.time_remaining=600

    def resume_timer(self):
        self.paused = False  # Reanudar el decremento
        self.update_time()  # Reiniciar la actualización del tiempo

    def stop_timer(self):
        self.paused = True  # Detener el decremento

root = tk.Tk()
scoreboard = BasketballScoreboard(root)
scoreboard.start()
