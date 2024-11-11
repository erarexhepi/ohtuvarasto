"""
Unit tests for the Varasto class.
"""

import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    """Tests for the Varasto class functionality."""

    def setUp(self):
        """Sets up a Varasto instance for testing."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Test if constructor creates an empty storage."""
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Test if new Varasto has the correct capacity."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Test if adding increases saldo correctly."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Test if adding decreases available space correctly."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Test if taking returns the correct amount."""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Test if taking adds space correctly."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus(self):
        """Test if negative capacity is set to zero."""
        varasto = Varasto(-15)
        self.assertEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        """Test if negative initial balance is set to zero."""
        varasto = Varasto(20, -10)
        self.assertEqual(varasto.saldo, 0)

    def test_alkusaldo_yli_tilavuuden(self):
        """Test if initial balance exceeding capacity is capped."""
        varasto = Varasto(12, 18)
        self.assertEqual(varasto.saldo, 12)

    def test_lisaa_negatiivinen_maara(self):
        """Test if adding negative amount does nothing."""
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisaa_yli_tilavuuden(self):
        """Test if adding amount over capacity caps at capacity."""
        self.varasto.lisaa_varastoon(15)
        self.assertEqual(self.varasto.saldo, 10)

    def test_ota_negatiivinen_maara(self):
        """Test if taking negative amount returns zero and does nothing."""
        saatu_maara = self.varasto.ota_varastosta(-5)
        self.assertEqual(saatu_maara, 0)
        self.assertEqual(self.varasto.saldo, 0)

    def test_ota_enemman_kuin_saldo(self):
        """Test if taking more than saldo returns only the saldo."""
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertEqual(saatu_maara, 5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_merkkijono_esitys(self):
        """Test string representation of Varasto."""
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(str(self.varasto), "saldo = 5.0, vielä tilaa 5.0")
