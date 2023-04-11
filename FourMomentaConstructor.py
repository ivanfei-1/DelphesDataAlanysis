# import dependencies
import ROOT as Root
import numpy as np
import matplotlib.pyplot as plt

# open the file
fileName = "tag_1_delphes_events.root"
directory = str("tag_1_delphes_events.root")
File = Root.TChain("Delphes;1")
File.Add(directory)
Number = File.GetEntries()


# create particle objects

class Particle:
    def __init__(self, pT, eta, phi, E):
        self.pT = pT
        self.eta = eta
        self.phi = phi
        self.E = E

    def __str__(self):
        return " E: {}, pT: {}, eta: {}, phi: {}".format(self.pT, self.eta, self.phi, self.E)
