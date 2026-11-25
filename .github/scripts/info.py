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



print("::notice::GitHub Repository Information")
print(f"::notice::Repository: {os.getenv('GITHUB_REPOSITORY')}")
print(f"::notice::Actor: {os.getenv('GITHUB_ACTOR')}")
print(f"::notice::Event: {os.getenv('GITHUB_EVENT_NAME')}")