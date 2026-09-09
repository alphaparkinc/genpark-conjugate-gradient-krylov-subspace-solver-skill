"""
Autonomous Agent Conjugate Gradient Solver Skill
Pure Python Standard Library implementation.
"""
import math
from typing import List, Dict, Any

class ConjugateGradient:
    """
    Conjugate Gradient Krylov Subspace solver for Ax = b (SPD systems).
    """
    @staticmethod
    def solve(A: List[List[float]], b: List[float], tol: float = 1e-6, max_iters: int = 100) -> List[float]:
        n = len(b)
        x = [0.0] * n
        r = list(b)
        p = list(r)
        rs_old = sum(val**2 for val in r)

        for _ in range(max_iters):
            Ap = [sum(A[i][j] * p[j] for j in range(n)) for i in range(n)]
            pAp = sum(p[i] * Ap[i] for i in range(n))
            if abs(pAp) < 1e-12:
                break
            alpha = rs_old / pAp
            x = [x[i] + alpha * p[i] for i in range(n)]
            r = [r[i] - alpha * Ap[i] for i in range(n)]
            rs_new = sum(val**2 for val in r)
            if math.sqrt(rs_new) < tol:
                break
            p = [r[i] + (rs_new / rs_old) * p[i] for i in range(n)]
            rs_old = rs_new

        return [round(val, 6) for val in x]
