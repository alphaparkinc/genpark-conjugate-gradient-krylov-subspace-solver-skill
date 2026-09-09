"""Example usage for Conjugate Gradient Solver Skill."""
from client import ConjugateGradient

def main():
    print("Executing Conjugate Gradient Solver...")
    A = [[4.0, 1.0], [1.0, 3.0]]
    b = [1.0, 2.0]
    x = ConjugateGradient.solve(A, b)
    print("Solution vector x:", x)
    assert abs(x[0] - 1.0/11.0) < 1e-4
    assert abs(x[1] - 7.0/11.0) < 1e-4
    print("Conjugate Gradient verified successfully!")

if __name__ == "__main__":
    main()
