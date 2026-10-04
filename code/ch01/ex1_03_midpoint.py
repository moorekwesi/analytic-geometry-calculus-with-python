# Listing 1.3: Midpoints and the parallelogram PQRS
import matplotlib.pyplot as plt

def midpoint(A, B):
    return ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)

P, Q, R, S = (1, 2), (4, 4), (5, 9), (2, 7)
M1, M2 = midpoint(P, R), midpoint(Q, S)
print("Midpoint of diagonal PR:", M1)
print("Midpoint of diagonal QS:", M2)
print("Diagonals bisect each other:", M1 == M2)

xs = [P[0], Q[0], R[0], S[0], P[0]]
ys = [P[1], Q[1], R[1], S[1], P[1]]
plt.figure(figsize=(4, 4.5))
plt.plot(xs, ys, "b-o")
plt.plot([P[0], R[0]], [P[1], R[1]], "g--")
plt.plot([Q[0], S[0]], [Q[1], S[1]], "g--")
plt.plot(*M1, "rs")
for name, pt in zip("PQRS", [P, Q, R, S]):
    plt.annotate(name, pt, textcoords="offset points", xytext=(6, -10))
plt.annotate("M(3, 5.5)", M1, textcoords="offset points", xytext=(8, 0))
plt.gca().set_aspect("equal")
plt.grid(alpha=0.3)
plt.show()
