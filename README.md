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
[ Your PC ]
   └── robot_controller/
       ├── __main__.py          ⇨ GUI entry point
       ├── ui.py                ⇨ GUI layout and control logic
       └── transmitter.py       ⇨ Communication interface

[ Your Robot ]
   └── robotlibrary/
       ├── network_control/
       │   ├── connector.py     ⇨ connects the robot to wifi 
       │   └── receiver.py      ⇨ receives information's and triggers certain actions
       └── ...