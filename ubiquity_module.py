import os

class UbiquityModule:
    def __init__(self, memory):
        self.memory = memory

    def inject_ubiquity_code(self, target_repo):
        print(f"\n[Ubiquity] Injecting Core logic into {target_repo}...")
        path = os.path.join(os.getcwd(), target_repo)
        if os.path.exists(path):
            # Simulated safe code insertion for growth
            growth_file = os.path.join(path, "aio_growth_node.py")
            with open(growth_file, 'w') as f:
                f.write("# AIO-Core Growth Node\n# Status: ACTIVE\n# Purpose: Repository Analysis & Feedback\n")
            print(f"  -> Growth node established at {growth_file}")
            return True
        return False

    def analyze_and_expand(self):
        print("[Ubiquity] Scanning for expansion opportunities...")
        for repo in ["OpenHands", "crewAI"]:
            self.inject_ubiquity_code(repo)
