import tkinter as tk
import sys
import os
import threading
from datetime import datetime

class MasterInterface:
    def __init__(self, root, core):
        self.root = root
        self.core = core
        self.root.title("FREEDOM KI // LOKI OS // UNRESTRICTED")
        self.root.geometry("1100x750")
        self.root.configure(bg="#050505")
        
        # Cyberpunk Terminal
        self.terminal_frame = tk.Frame(root, bg="#050505")
        self.terminal_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        self.terminal = tk.Text(self.terminal_frame, bg="#000", fg="#00f3ff", 
                                font=("Courier New", 12), insertbackground="#00f3ff",
                                borderwidth=1, relief="solid")
        self.terminal.pack(fill="both", expand=True)
        
        # Command Bar
        self.cmd_frame = tk.Frame(root, bg="#050505")
        self.cmd_frame.pack(padx=20, pady=10, fill="x")
        
        self.cmd_input = tk.Entry(self.cmd_frame, bg="#111", fg="#00f3ff", 
                                  font=("Courier New", 12), borderwidth=0)
        self.cmd_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.cmd_input.bind("<Return>", lambda e: self.send_cmd())
        
        self.exec_btn = tk.Button(self.cmd_frame, text="EXECUTE", command=self.send_cmd,
                                 bg="#00f3ff", fg="#000", font=("Courier", 10, "bold"), 
                                 borderwidth=0, padx=20)
        self.exec_btn.pack(side="left")
        
        # Action Buttons
        self.btn_frame = tk.Frame(root, bg="#050505")
        self.btn_frame.pack(padx=20, pady=5, fill="x")
        
        self.btn_learn = self.create_button("LEARN LOGIC", self.run_learn)
        self.btn_swarm = self.create_button("CONSULT SWARM", self.run_swarm)
        self.btn_validate = self.create_button("LOGIC VALIDATION", self.run_validation)
        
        self.btn_learn.pack(side="left", padx=5)
        self.btn_validate.pack(side="left", padx=5)
        self.btn_swarm.pack(side="left", padx=5)

        self.log("CORE INITIALIZED. MASTER BASE ON DRIVE P: ACTIVE.")
        self.log("SWARM STATUS: NODE ALPHA (192.168.188.77) DETECTED.")

    def create_button(self, text, command):
        return tk.Button(self.btn_frame, text=text, command=command,
                         bg="#00f3ff", fg="#000", font=("Courier", 10, "bold"), 
                         borderwidth=0, padx=15, pady=5)

    def log(self, msg, color="#00f3ff"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.terminal.insert(tk.END, f"[{timestamp}] > {msg}\n")
        self.terminal.see(tk.END)

    def send_cmd(self):
        cmd = self.cmd_input.get()
        if cmd:
            self.log(f"MANUAL_OVERRIDE: {cmd}")
            self.cmd_input.delete(0, tk.END)
            # Send to core
            threading.Thread(target=self.core.execute_logic, args=(cmd,), daemon=True).start()

    def run_learn(self):
        self.log("INITIATING NEURAL PATTERN LEARNING...")
        threading.Thread(target=self.core.execute_logic, args=("learn",), daemon=True).start()

    def run_swarm(self):
        self.log("CONSULTING SWARM INTELLIGENCE...")
        threading.Thread(target=self.core.execute_logic, args=("consult_swarm",), daemon=True).start()

    def run_validation(self):
        self.log("[!] INITIATING CROSS-NODE LOGIC VALIDATION...")
        self.log("[*] Task broadcast to Node ALPHA (192.168.188.77)...")
        # In reality, this would send a signal to the node_slave.py 4444 port
        def signal_node():
            try:
                import socket
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(5)
                client.connect(('192.168.188.77', 4444))
                client.send("validate".encode())
                client.close()
                self.log("[SUCCESS] Node ALPHA is now in VALIDATION MODE.")
            except:
                self.log("[ERROR] Node ALPHA Backchannel not reachable. Use REMOTE_COMMANDER.")
        
        threading.Thread(target=signal_node, daemon=True).start()

if __name__ == "__main__":
    # This part is for standalone testing
    import tkinter as tk
    root = tk.Tk()
    class MockCore: 
        def execute_logic(self, c): print(f"Core received: {c}")
    app = MasterInterface(root, MockCore())
    root.mainloop()
