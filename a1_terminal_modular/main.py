#!/usr/bin/env python3
"""
A1 Terminal - Modular Version
Main Entry Point
"""

import customtkinter as ctk
import platform

# Configure appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Platform-specific UI scaling for better appearance
system = platform.system()
if system == "Linux":
    # Linux/Ubuntu needs better scaling for modern high-DPI displays
    ctk.set_widget_scaling(1.15)  # 15% larger widgets
    ctk.set_window_scaling(1.1)   # 10% larger windows
elif system == "Windows":
    ctk.set_widget_scaling(1.0)   # Default scaling
    ctk.set_window_scaling(1.0)
elif system == "Darwin":  # macOS
    ctk.set_widget_scaling(1.0)
    ctk.set_window_scaling(1.0)

from src.core.a1_terminal import A1Terminal

if __name__ == "__main__":
    app = A1Terminal()
    app.run()
