import json
import urllib.request

API_URL = "https://9db1-34-123-217-84.ngrok-free.app/infer"

def handler(event, context):
    message = event.get("message", "")

    payload = json.dumps({"message": message}).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(req) as resp:
        resp_body = resp.read()

    result = json.loads(resp_body)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "reply": result.get("reply", "")
        })
    }
