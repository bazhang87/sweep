import json
import time

from fastapi.testclient import TestClient

from sweepai.api import app

if __name__ == "__main__":
    client = TestClient(app)
    start_time = time.time()
    response = client.post(
        "/",
        json=json.load(open("tests/jsons/opened_pull.json", "r")),
        headers={"X-GitHub-Event": "pull_request"},
    )
    print(f"Completed in {time.time() - start_time}s")
    print(response)
    print(response.text)
