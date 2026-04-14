import subprocess
import tempfile
import os
import json

def run_pylint(code: str) -> list[dict]:
    with tempfile.NamedTemporaryFile(suffix=".py", mode="w", delete=False) as f:
        f.write(code)
        tmp_path = f.name

    try:
        result = subprocess.run(
            ["python", "-m", "pylint", tmp_path, "--output-format=json", "--score=no"],
            capture_output=True,
            text=True
        )

        # ✅ Handle empty output (IMPORTANT FIX)
        if not result.stdout.strip():
            return []

        try:
            issues = json.loads(result.stdout)
        except json.JSONDecodeError:
            return []

        return [
            {
                "line": i.get("line", 0),
                "message": i.get("message", ""),
                "type": i.get("type", "C"),
            }
            for i in issues
        ]

    except Exception as e:
        return [{"line": 0, "message": str(e), "type": "E"}]

    finally:
        os.unlink(tmp_path)