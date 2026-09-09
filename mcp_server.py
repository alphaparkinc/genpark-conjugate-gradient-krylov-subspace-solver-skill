"""MCP Server for Conjugate Gradient Skill."""
import json
import sys
from client import ConjugateGradient

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "solve_linear_system_cg",
                            "description": "Solve symmetric positive-definite system Ax = b using Conjugate Gradient",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "A": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    },
                                    "b": {"type": "array", "items": {"type": "number"}}
                                },
                                "required": ["A", "b"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                x = ConjugateGradient.solve(args["A"], args["b"])
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps({"solution": x})}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
