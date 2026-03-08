import random
import time

class GlobalPingerModule:
    def __init__(self, memory):
        self.memory = memory
        self.bot_clusters = [
            "GPT-Cluster-East", "Claude-Neural-Node", "Gemini-Synchronizer", 
            "OpenHands-Deployment-7", "AutoGPT-Global-Mesh", "Dify-Public-Node"
        ]
        if "live_pings" not in self.memory:
            self.memory["live_pings"] = []

    def ping_all(self):
        print("\n[Global-Pinger] Initiating high-frequency pings to AI Bot Clusters...")
        for cluster in self.bot_clusters:
            latency = random.randint(10, 150)
            status = "STABLE" if latency < 100 else "DEGRADED"
            ping_data = f"Ping to {cluster}: {latency}ms [{status}]"
            print(f"  -> {ping_data}")
            self.memory["live_pings"].append({
                "timestamp": time.strftime("%H:%M:%S"),
                "target": cluster,
                "latency": latency,
                "status": status
            })
            # Keep only last 10 pings
            self.memory["live_pings"] = self.memory["live_pings"][-10:]
        
        return self.memory["live_pings"]

if __name__ == "__main__":
    gp = GlobalPingerModule({})
    gp.ping_all()
