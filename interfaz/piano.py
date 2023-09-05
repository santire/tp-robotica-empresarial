import tkinter as tk
import sounddevice as sd  # For generating piano sounds (cross-platform)
import numpy as np

# Define piano key frequencies
piano_keys = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88,
    "C5": 523.25,
}

# Function to play piano sound


def play_sound(frequency):
    duration = 0.5  # seconds
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, sample_rate)
    sd.wait()


# Create the main window
root = tk.Tk()
root.title("Tkinter Piano")

# Create piano keys using buttons
for key, frequency in piano_keys.items():
    btn = tk.Button(
        root, text=key, width=6, height=3, command=lambda f=frequency: play_sound(f)
    )
    btn.grid(row=0, column=list(piano_keys.keys()).index(key))

# Start the GUI event loop
root.mainloop()
