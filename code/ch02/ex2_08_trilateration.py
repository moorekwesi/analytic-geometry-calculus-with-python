# Listing 2.8: Locating a phone from its distances to three masts (trilateration)
import numpy as np

masts = np.array([[0.0, 0.0], [10.0, 0.0], [4.0, 9.0]])   # km
d = np.array([5.000, 8.062, 5.099])                       # measured distances, km

# Circle i:  x^2 + y^2 - 2 a_i x - 2 b_i y + (a_i^2 + b_i^2 - d_i^2) = 0
# Subtracting circle 1 from circles 2 and 3 removes x^2 + y^2 and leaves two LINES
# (the common chords), whose intersection is the phone.
(a1, b1), (a2, b2), (a3, b3) = masts
M = np.array([[2*(a2 - a1), 2*(b2 - b1)],
              [2*(a3 - a1), 2*(b3 - b1)]])
rhs = np.array([d[0]**2 - d[1]**2 + a2**2 - a1**2 + b2**2 - b1**2,
                d[0]**2 - d[2]**2 + a3**2 - a1**2 + b3**2 - b1**2])
phone = np.linalg.solve(M, rhs)
print("Estimated position of the phone:", np.round(phone, 3))
print("Check distances:", np.round(np.linalg.norm(masts - phone, axis=1), 3))
