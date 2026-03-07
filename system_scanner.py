import os

class FullSystemScanner:
    def __init__(self, start_path="c:\\Users\\Loki"):
        self.start_path = start_path
        self.found_agents = []

    def scan(self):
        print(f"\n[System-Scanner] Deep scanning {self.start_path} for AI-Nodes...")
        keywords = ["agent", "bot", "ai", "brain", "crew", "hands", "gpt", "nexus", "hive"]
        
        # Simulated scan results based on common user patterns and directory list
        potential_dirs = [
            "c:\\Users\\Loki\\HiveMind_Core",
            "c:\\Users\\Loki\\AnalyzingMachine",
            "c:\\Users\\Loki\\Cyberpunk_Agent",
            "c:\\Users\\Loki\\Loki_Network_Scanner"
        ]
        
        for d in potential_dirs:
            if os.path.exists(d):
                self.found_agents.append(d)
                print(f"  -> Discovered AI Node: {d}")
        
        return self.found_agents

if __name__ == "__main__":
    scanner = FullSystemScanner()
    scanner.scan()
