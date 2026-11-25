import numpy as np

class MetaTensorMilieu:
    """
    Méta-Tenseur du Milieu - Dominic Dubois
    Omega = {T, F, D, E, R}
    T: Tension, F: Flux, D: Divergence, E: Equilibre, R: Resonance
    M_AB est la matrice 5x5 d'interactions internes du pixel.
    """
    INDICES = {"T": 0, "F": 1, "D": 2, "E": 3, "R": 4}

    def __init__(self, M):
        M = np.asarray(M, dtype=float)
        if M.shape != (5, 5):
            raise ValueError("M doit être une matrice 5x5, M_AB avec A,B dans {T,F,D,E,R}")
        self.M = M

    def phi_T(self):
        """Potentiel scalaire émergent. Somme de la ligne Tension."""
        return float(np.sum(self.M[0, :]))

    def phi_F(self):
        """Potentiel vectoriel émergent. Ligne Flux, projetée en 3D."""
        return self.M[1, 0:3].copy()

    def champs_E_B(self, grad_phi_T, curl_phi_F, d_phi_F_dt=None):
        """E = - grad(phi_T) - d(phi_F)/dt, B = curl(phi_F)"""
        if d_phi_F_dt is None:
            d_phi_F_dt = np.zeros(3)
        E = -np.asarray(grad_phi_T) - np.asarray(d_phi_F_dt)
        B = np.asarray(curl_phi_F)
        return E, B

    def energie_T00(self):
        return float(np.sum(self.M ** 2))

    def metrique_emergente(self):
        return float(np.mean(self.M))

if __name__ == "__main__":
    M_exemple = np.array([
        [1.05, 0.10, 0.02, 0.00, 0.01],
        [0.10, 0.50, 1.00, 0.20, 0.05],
        [0.02, 0.10, 0.30, 0.10, 0.02],
        [0.00, 0.20, 0.10, 0.40, 0.03],
        [0.01, 0.05, 0.02, 0.03, 0.007],
    ])
    M = MetaTensorMilieu(M_exemple)
    print(f"phi_T = {M.phi_T():.4f}")
    print(f"phi_F = {M.phi_F()}")
    print(f"Energie T00 : {M.energie_T00():.4f}")
    E, B = M.champs_E_B([0.1, 0.0, 0.0], [0.0, 0.0, 0.5])
    print(f"E : {E}")
    print(f"B : {B}")
