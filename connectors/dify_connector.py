class DifyConnector:
    def __init__(self):
        self.name = "Dify.ai"

    def trigger_workflow(self, workflow_id):
        print(f"[{self.name}] Triggering Dify workflow: {workflow_id}")
        return "Workflow output from Dify API."
