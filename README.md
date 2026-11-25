# Méta-Tenseur du Milieu

**Auteur :** Dominic Dubois  
**Référence :** DOI 10.5281/zenodo.23377236  
**Livre complet :** 163 pages sur ResearchGate

## L'idée en une phrase

Les lois de la physique ne sont pas fondamentales.  
Elles sont des projections de la dynamique interne d'un pixel du milieu.

## Les 5 composantes

`Omega = {T, F, D, E, R}`

- **T - Tension** : loi de tension interne. Donne le potentiel scalaire `phi_T`
- **F - Flux** : loi de flux. Donne le potentiel vectoriel `phi_F`
- **D - Divergence** : loi de divergence. Donne les sources, Gauss
- **E - Équilibre** : loi d'équilibre. Stabilise le milieu
- **R - Résonance** : loi de résonance. Couplage et mémoire du milieu

## Ce qui émerge

- `B = curl(phi_F)` donc `div(B) = 0`
- `E = - grad(phi_T) - d(phi_F)/dt`
- Faraday : `curl(E) + dB/dt = 0`
- Métrique : `g = <M_AB>` moyenne sur le pixel
- Énergie : `T00 = somme(M_AB^2)`

## Comment tester

```bash
python meta_tensor_milieu.py
