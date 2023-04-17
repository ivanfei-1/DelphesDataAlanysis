import numpy as np
import matplotlib.pyplot as plt
from FourMomentaConstructor import Particle


# define a function to calculate the angle between two particles, given their four-momenta
def angle(p1, p2):
    angle = np.arccos((p1[0] * p2[0] + p1[1] * p2[1] + p1[2] * p2[2]) / (
            np.sqrt(p1[0] ** 2 + p1[1] ** 2 + p1[2] ** 2) * np.sqrt(p2[0] ** 2 + p2[1] ** 2 + p2[2] ** 2)))
    return angle


# calculate one particle's cartesian momentum from pT, eta, phi and m
class CartesianParticle:
    def __init__(self, pT: float, eta: float, phi: float, m: float, E=None):
        self.px = pT * np.cos(phi)
        self.py = pT * np.sin(phi)
        self.pz = pT / np.tan(2 * np.arctan(np.exp(-eta)))
        self.p = np.sqrt(self.px ** 2 + self.py ** 2 + self.pz ** 2)
        self.E = np.sqrt(self.p ** 2 + m ** 2) if E is None else E


# from the four-momenta of the two daughter particles, calculate their parent particle's four-momenta
def parent(p1: CartesianParticle, p2: CartesianParticle, m1: float, m2: float, m: float):
    p = np.sqrt((p1.p + p2.p) ** 2 - (p1.px + p2.px) ** 2 - (p1.py + p2.py) ** 2 - (p1.pz + p2.pz) ** 2)
    E = np.sqrt(p ** 2 + m ** 2)
    px = p1.px + p2.px
    py = p1.py + p2.py
    pz = p1.pz + p2.pz
    return CartesianParticle(px, py, pz, m, E)

