# main.py

import tkinter as tk
from app.functions import (authenticate, create_post_login_screen, create_image_label,
                           create_core_screen, create_fantasy_screen, create_players_screen, create_teams_screen,
                           create_standings_screen, create_player_points_screen, create_top_scorers_screen,
                           create_waiver_watchlist_screen, create_gambling_screen,
                           )


def show_screen(frame):
    for f in [login_frame, post_login_frame, core_frame, fantasy_frame, players_frame, teams_frame, standings_frame,
              player_points_frame, top_scorers_frame, waiver_watchlist_frame, gambling_frame]:
        f.pack_forget()
    frame.pack()


def show_post_login_screen():
    show_screen(post_login_frame)


def show_core_screen():
    show_screen(core_frame)


def show_players_screen():
    show_screen(players_frame)


def show_teams_screen():
    show_screen(teams_frame)


def show_standings_screen():
    show_screen(standings_frame)


def show_fantasy_screen():
    show_screen(fantasy_frame)


def show_player_points_screen():
    show_screen(player_points_frame)


def show_top_scorers_screen():
    show_screen(top_scorers_frame)


def show_waiver_watchlist_screen():
    show_screen(waiver_watchlist_frame)


def show_gambling_screen():
    show_screen(gambling_frame)


def check_login():
    if authenticate(entry_username.get(), entry_password.get()):
        show_post_login_screen()
    else:
        message_label.config(text="Login Failed: Incorrect username or password.")


window = tk.Tk()
window.title("Gridiron Guru")

# Maximize the window
window.state('zoomed')

title_label = tk.Label(window, text="Gridiron Guru", font=("Helvetica", 16, "bold"))
title_label.pack()
login_frame = tk.Frame(window)
login_frame.pack()
image_label_login = create_image_label(login_frame)
image_label_login.pack()
label_username = tk.Label(login_frame, text="Username")
label_username.pack()
entry_username = tk.Entry(login_frame)
entry_username.pack()
label_password = tk.Label(login_frame, text="Password")
label_password.pack()
entry_password = tk.Entry(login_frame, show="*")
entry_password.pack()
login_button = tk.Button(login_frame, text="Login", command=check_login)
login_button.pack()
message_label = tk.Label(login_frame, text="")
message_label.pack()
post_login_frame, button_core, button_fantasy, button_gambling = create_post_login_screen(window, show_gambling_screen)


# Gambling Frame
gambling_frame = create_gambling_screen(window, show_core_screen)


# Core Frame
core_frame = create_core_screen(window, show_post_login_screen)
players_frame = create_players_screen(window, show_core_screen)
teams_frame = create_teams_screen(window, show_core_screen)
standings_frame = create_standings_screen(window, show_core_screen)
for child in core_frame.winfo_children():
    if isinstance(child, tk.Button):
        if child.cget('text') == "Players":
            child.config(command=show_players_screen)
        elif child.cget('text') == "Teams":
            child.config(command=show_teams_screen)
        elif child.cget('text') == "Standings":
            child.config(command=show_standings_screen)

# Fantasy Frame
fantasy_frame = create_fantasy_screen(window, show_post_login_screen, show_player_points_screen,
                                      show_waiver_watchlist_screen, show_waiver_watchlist_screen)
player_points_frame = create_player_points_screen(window, show_fantasy_screen)
top_scorers_frame = create_top_scorers_screen(window, show_fantasy_screen)
waiver_watchlist_frame = create_waiver_watchlist_screen(window, show_fantasy_screen)

button_core.config(command=show_core_screen)
button_fantasy.config(command=show_fantasy_screen)


window.mainloop()

