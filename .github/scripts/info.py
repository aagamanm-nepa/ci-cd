import os
import json

print("=== GitHub Actions Information ===")

print("Repository:", os.getenv("GITHUB_REPOSITORY"))
print("Actor:", os.getenv("GITHUB_ACTOR"))
print("Event:", os.getenv("GITHUB_EVENT_NAME"))
print("Ref:", os.getenv("GITHUB_REF"))
print("Ref name:", os.getenv("GITHUB_REF_NAME"))
print("SHA:", os.getenv("GITHUB_SHA"))
print("Workflow:", os.getenv("GITHUB_WORKFLOW"))
print("Run ID:", os.getenv("GITHUB_RUN_ID"))

with open(os.environ["GITHUB_EVENT_PATH"]) as file:
    event = json.load(file)

print("\n=== Full Event Payload ===")
print(json.dumps(event, indent=2))
