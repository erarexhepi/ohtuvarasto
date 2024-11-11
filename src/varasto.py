"""
This module contains the Varasto class, which simulates a storage system with capacity constraints.
"""

class Varasto:
    """
    A class representing a storage with limited capacity and initial balance.
    """

    def __init__(self, tilavuus, alku_saldo=0):
        """
        Initializes the Varasto with a given capacity and optional initial balance.

        :tilavuus: Maximum capacity of the storage
        :alku_saldo: Initial balance in the storage
        """
        self.tilavuus = max(tilavuus, 0.0)
        self.saldo = max(0.0, min(alku_saldo, tilavuus))

    def paljonko_mahtuu(self):
        """Returns the available capacity in the storage."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """
        Adds a specified amount to the storage, but not more than the maximum capacity.

        :param maara: Amount to add
        """
        if maara >= 0:
            self.saldo = min(self.saldo + maara, self.tilavuus)

    def ota_varastosta(self, maara):
        """
        Removes a specified amount from the storage, if available.

        :maara: Amount to remove
        :return: Actual amount removed
        """
        if maara < 0:
            return 0.0
        otettu = min(maara, self.saldo)
        self.saldo -= otettu
        return otettu

    def __str__(self):
        """Returns a string representation of the storage status."""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
