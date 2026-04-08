import requests

BASE_URL = "https://pallavibs0101-viginova-env.hf.space"

def run_inference(action="test"):
    r = requests.post(f"{BASE_URL}/reset")
    reset_response = r.json()

    r = requests.post(f"{BASE_URL}/step", json={"action": action})
    step_response = r.json()

    return {
        "reset": reset_response,
        "step": step_response
    }


if __name__ == "__main__":
    print("[START]")
    result = run_inference()
    print(result)
    print("[END]")
