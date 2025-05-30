# robot_controller

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-green)
![License](https://img.shields.io/github/license/Veicm/robot_controller)
![Status](https://img.shields.io/badge/Status-Stable-green)

**robot_controller** is a modular, Python-based GUI application for controlling robots via various interfaces. It allows users to easily select robot modules, send motion commands, and view real-time status updates.

> [!IMPORTANT]  
> The [robotlibrary](https://github.com/Veicm/robotlibrary) is required to be installed on the robot.


---

## Features

✅ Intuitive graphical interface using Tkinter

✅ Support for multiple robot models (e.g. SMARS)

✅ Real-time control

✅ communication via wifi

✅ Easily extensible

✅ Dynamic GUI layout with synchronized state management

---

## Architecture

```text
robot_controller/
├── __main__.py          ⇨ Entry point launching the GUI
├── ui.py                ⇨ GUI layout and controls (Tkinter)
├── transmitter.py       ⇨ Communication handler
├── robot/               ⇨ Robot models (via robotlibrary)
└── README.md
```