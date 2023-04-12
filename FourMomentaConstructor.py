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

    def __init__(self, pT: float, eta: float, phi: float, m: float, E=None):
        self.pT = pT
        self.eta = eta
        self.phi = phi
        self.m = m
        # if E is not given, calculate it from pT, eta, phi and m
        self.E = np.sqrt((pT / np.sin(eta)) ** 2 + m ** 2) if E is None else E

    def __str__(self):
        return "pT: {}, eta: {}, phi: {}, m: {}, E: {}".format(self.pT, self.eta, self.phi, self.m, self.E)


# # define photon objects
# class Photon(Particle):
#     pass
#
#
# # define electron objects
# class Electron(Particle):
#     pass
#
#
# # define muon objects
# class Muon(Particle):
#     pass
#
#
# # define jet objects
# class Jet(Particle):
#     pass


# define a list of all particles
Particles = ['Jet', 'Photon', 'Electron', 'Muon']


class ParticleList:
    def __init__(self, name):
        self.name = name
        self.list: list[Particle] = []

    def __str__(self):
        return "{}List".format(self.name)

    def getPT(self):
        return [particle.pT for particle in self.list]

    def getEta(self):
        return [particle.eta for particle in self.list]

    def getPhi(self):
        return [particle.phi for particle in self.list]

    def getE(self):
        return [particle.E for particle in self.list]


# define a list of all particle lists
ParticleLists = [ParticleList(particle) for particle in Particles]
print(ParticleLists)

for particle in ParticleLists:
    for i in range(Number):
        Entry = File.GetEntry(i)
        ParticleFromBranch = eval('File.' + particle.name + '.GetEntries()')

        # if particle is undefined, skip this event
        if ParticleFromBranch == 0:
            continue

        else:
            for j in range(ParticleFromBranch):
                # get particle properties from the branch
                if particle.name == 'Photon':
                    # photon energy given in ROOT file
                    ParticleEntity = Particle(pT=File.GetLeaf(str(particle.name) + '.PT').GetValue(j),
                                              eta=File.GetLeaf(str(particle.name) + '.Eta').GetValue(j),
                                              phi=File.GetLeaf(str(particle.name) + '.Phi').GetValue(j),
                                              m=0,
                                              E=File.GetLeaf(str(particle.name) + '.E').GetValue(j))
                elif particle.name == 'Electron':
                    ParticleEntity = Particle(pT=File.GetLeaf(str(particle.name) + '.PT').GetValue(j),
                                              eta=File.GetLeaf(str(particle.name) + '.Eta').GetValue(j),
                                              phi=File.GetLeaf(str(particle.name) + '.Phi').GetValue(j),
                                              m=0.000511)
                elif particle.name == 'Muon':
                    ParticleEntity = Particle(pT=File.GetLeaf(str(particle.name) + '.PT').GetValue(j),
                                              eta=File.GetLeaf(str(particle.name) + '.Eta').GetValue(j),
                                              phi=File.GetLeaf(str(particle.name) + '.Phi').GetValue(j),
                                              m=0.105658)
                elif particle.name == 'Jet':
                    ParticleEntity = Particle(pT=File.GetLeaf(str(particle.name) + '.PT').GetValue(j),
                                              eta=File.GetLeaf(str(particle.name) + '.Eta').GetValue(j),
                                              phi=File.GetLeaf(str(particle.name) + '.Phi').GetValue(j),
                                              m=File.GetLeaf(str(particle.name) + '.Mass').GetValue(j))
                else:
                    continue
                particle.list.append(ParticleEntity)

# draw histograms
for particle in ParticleLists:
    plt.figure(particle.name)
    plt.hist(particle.getPT(), bins=100)
    plt.xlabel('pT')
    plt.ylabel('Number of particles')
    plt.title(str(particle))
plt.show()
