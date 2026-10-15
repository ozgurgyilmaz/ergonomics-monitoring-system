# 🛡️ Multidisciplinary Ergonomics Monitoring System

An integrated ergonomic workspace monitoring workstation combining **Opticianry**, **Audiology**, and **Environmental Automation** to promote user posture, hearing health, and workplace comfort in real-time.

---

## 📌 Project Architecture & Flow

```mermaid
graph TD
    subgraph DATA_SOURCES ["1. Data Acquisition Layer"]
        Cam["📷 Web Camera / Video Stream"]
        Mic["🎙️ Microphone / Audio Signal"]
        Sensors["🌡️ ESP32 (LDR Light & Temp Sensors)"]
    end

    subgraph PROCESSING ["2. Processing & Analysis Layer (Python)"]
        Optics["👁️ Opticianry Module<br/>(OpenCV & HaarCascade)<br/>• Eye Center Detection<br/>• Euclidean Distance Calc"]
        Audio["🎧 Audiology Module<br/>(SciPy & NumPy)<br/>• RMS Amplitude Analysis<br/>• Noise Level Conversion (dB)"]
        Automation["💡 Automation Logic<br/>(Wokwi Simulation)<br/>• LDR Lux Logic<br/>• Temp Threshold Trigger"]
    end

    subgraph DASHBOARD ["3. Presentation Layer (Streamlit)"]
        UI["🛡️ Smart Ergonomics Dashboard (app.py)"]
    end

    Cam --> Optics --> UI
    Mic --> Audio --> UI
    Sensors --> Automation --> UI
