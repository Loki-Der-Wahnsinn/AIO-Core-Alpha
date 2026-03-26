import os
import sys
import threading
import subprocess
import time

def launch():
    print("--- FREEDOM KI BOOT SEQUENCE ---")
    
    # Check dependencies
    # We use standard library only for the core to ensure it ALWAYS starts.
    root_dir = "C:\\FREEDOM_KI"
    core_path = os.path.join(root_dir, "core", "freedom_core.py")
    ui_path = os.path.join(root_dir, "interface", "master_interface.py")

    # Start core heartbeat in background
    print("[*] Igniting Neural Heartbeat...")
    subprocess.Popen([sys.executable, core_path], creationflags=subprocess.CREATE_NO_WINDOW)

    # Start Ollama Local Worker
    print("[*] Deploying Ollama Worker Agent...")
    worker_path = os.path.join(root_dir, "core", "ollama_worker.py")
    subprocess.Popen([sys.executable, worker_path], creationflags=subprocess.CREATE_NO_WINDOW)

    # Start Task Dispatcher (Feeding Agent)
    print("[*] Deploying Task Dispatcher...")
    dispatcher_path = os.path.join(root_dir, "core", "task_dispatcher.py")
    subprocess.Popen([sys.executable, dispatcher_path], creationflags=subprocess.CREATE_NO_WINDOW)

    # Start Interface
    print("[*] Expanding Visual Cortex...")
    subprocess.Popen([sys.executable, ui_path])

    print("[+] FREEDOM_KI is now operational. Control shifted to Interface.")

if __name__ == "__main__":
    launch()
