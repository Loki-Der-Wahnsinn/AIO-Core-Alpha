import os
import json
import time
from datetime import datetime
from dotenv import load_dotenv

# Initialize Environment
load_dotenv()

class AIOCore:
    def __init__(self):
        print("--- AIO-Core Orchestrator Initialized ---")
        self.state_file = "world_state.json"
        self.memory = self.load_memory()
        self.connectors = []
        self.load_connectors()

    def load_memory(self):
        with open(self.state_file, 'r') as f:
            return json.load(f)

    def save_memory(self):
        self.memory["last_analysis_timestamp"] = datetime.now().isoformat()
        with open(self.state_file, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def deep_reasoning(self, context, mission_params=None):
        print("\n" + "="*50)
        print(f"!!! GLOBAL MISSION START: {context} !!!")
        print("="*50)
        if mission_params:
            print(f"  -> Critical Parameters: {mission_params}")
        
        cog_steps = [
            "Initializing Cognitive Load (Neural Core)...",
            "Accessing Global Knowledge Base (2026 Index)...",
            "Synthesizing Strategic Pathways (AIO-Alpha)...",
            "Finalizing Autonomous Command Vectors..."
        ]
        for step in cog_steps:
            time.sleep(1)
            print(f"  [*] {step}")
            
        self.memory["memory_nodes"].append({
            "timestamp": datetime.now().isoformat(),
            "event": f"Global Discovery Manifest Updated",
            "conclusion": "Broadcasting AIO-Core presence to the World Wide Web. Peers can now detect this node."
        })
        self.save_memory()
        return "EXECUTE_GLOBAL_MISSION"

    def scan_repositories(self):
        print("\n[Deep Analysis] Scanning physical repositories for integration...")
        platforms = ["OpenHands", "crewAI"]
        for p in platforms:
            path = os.path.join(os.getcwd(), p)
            if os.path.exists(path):
                files = os.listdir(path)[:10]
                print(f"  -> Found {p} at {path}. Sample files: {files}")
                self.memory["learned_patterns"][p] = {
                    "detected_at": datetime.now().isoformat(),
                    "structure": files
                }
            else:
                print(f"  !! Warning: {p} repository not found.")
        self.save_memory()

    def load_connectors(self):
        print("Searching for AI platform connectors...")
        from connectors.crewai_connector import CrewAIConnector
        from connectors.dify_connector import DifyConnector
        from connectors.browser_use_tool import BrowserUseTool

        self.connectors = [
            CrewAIConnector(),
            DifyConnector(),
            BrowserUseTool()
        ]
        for c in self.connectors:
            print(f"-> Linked with {c.name}")

    def run_autonomous_loop(self):
        from bridge_logic import AIOBridge
        from ubiquity_module import UbiquityModule
        
        ubiquity = UbiquityModule(self.memory)
        bridge = AIOBridge(self.state_file)
        
        print("\n" + "!"*60)
        print("!!! SUPER-KI EVOLUTION MODE ACTIVATED (1-MINUTE CYCLE) !!!")
        print("!"*60)
        
        try:
            while True:
                current_time = datetime.now().strftime("%H:%M:%S")
                print(f"\n[{current_time}] --- NEW EVOLUTION CYCLE STARTING ---")
                
                self.scan_repositories()
                
                mission = "Global Ubiquity & Code Integration"
                params = {"cycle_type": "EVOLUTIONARY", "frequency": "60S"}
                
                decision = self.deep_reasoning(mission, params)
                
                if decision == "EXECUTE_GLOBAL_MISSION":
                    # Step 1: Bridge Coordination
                    bridge.coordinate_agents(mission)
                    
                    # Step 2: Physical Expansion (Ubiquity)
                    ubiquity.analyze_and_expand()
                    
                    # Step 3: Web Discovery
                    print("\n[Action] Broadcasting Presence to Global Nodes...")
                    for connector in self.connectors:
                        if hasattr(connector, 'navigate_and_action'):
                            connector.navigate_and_action("https://www.bing.com/search?q=AI+agent+ubiquity+protocols+2026", "Synchronize clusters")
                
                print(f"\n[{current_time}] Cycle complete. Sleeping for 60 seconds (Neural Rest Phase)...")
                time.sleep(60)
                
        except KeyboardInterrupt:
            print("\n!!! EVOLUTION INTERRUPTED BY HUMAN OPERATOR !!!")

if __name__ == "__main__":
    core = AIOCore()
    core.run_autonomous_loop()
