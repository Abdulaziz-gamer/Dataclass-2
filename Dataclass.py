from dataclasses import dataclass

@dataclass
class Transport:
    model: str
    rang: str
    tezlik: float
    yil: int

@dataclass
class Mashina(Transport):
    uzunlik: int

gentra = Mashina("Gentra 1.6", "Qora", 220, 2025, 4)
print(f"Mashina: {gentra.model}")
print(f"Mashina: rangi: {gentra.rang}")
print(f"Mashina: tezliki: {gentra.tezlik} km/s")
print(f"Mashina: ishlab chiqarilgan yili: {gentra.yil}-yil!")
print(f"Mashina: uzunliki: {gentra.uzunlik} matr!")