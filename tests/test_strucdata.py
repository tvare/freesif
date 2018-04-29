# -*- coding: utf-8 -*-
"""Test StrucData public methods
"""

import unittest
import numpy as np
import h5py
import freesif as fs


class TestStrucDataCase01(unittest.TestCase):
    """1st order triangular plate elements, element results
    """

    @classmethod
    def setUpClass(cls):
        # establish StrucData instances and associated verification data
        cls._data = fs.open_sif('files/struc/single_super_elem/test01_1stord_linstat_R1.SIU')
        cls._f_verified = h5py.File('files/verified_testdata.h5', 'r')
        cls._gr_verified = cls._f_verified['test01_1stord_linstat_R1/LD_plates/elemres']

    @classmethod
    def tearDownClass(cls):
        cls._data.close()
        cls._f_verified.close()

    def test_get_nodes(self):
        nodes = self._data.get_nodes(sets='LD_plates', kind='shell', disconnected=True)
        nodes_verified = self._gr_verified['nodes']
        self.assertTrue(np.allclose(nodes, nodes_verified))

    def test_get_elements(self):
        elems = self._data.get_elements(sets='LD_plates', kind='shell', disconnected=True)
        connectivity = self._gr_verified['connectivity']
        offset = self._gr_verified['offset']
        eltyp = self._gr_verified['eltyp']
        self.assertTrue(np.allclose(elems[0], connectivity))
        self.assertTrue(np.allclose(elems[1], offset))
        self.assertTrue(np.allclose(elems[2], eltyp))

    def test_get_elementresults_generalstress(self):
        res = self._data.get_elementresults('generalstress', rescases=1, sets='LD_plates')
        res_verified = self._gr_verified['generalstress']
        self.assertTrue(np.allclose(res, res_verified))


class TestStrucDataCase02(unittest.TestCase):
    """1st order triangular plate elements, node results
    """

    @classmethod
    def setUpClass(cls):
        # establish StrucData instances and associated verification data
        cls._data = fs.open_sif('files/struc/single_super_elem/test01_1stord_linstat_R1.SIU')
        cls._f_verified = h5py.File('files/verified_testdata.h5', 'r')
        cls._gr_verified = cls._f_verified['test01_1stord_linstat_R1/LD_plates/noderes']

    @classmethod
    def tearDownClass(cls):
        cls._data.close()
        cls._f_verified.close()

    def test_get_nodes(self):
        nodes = self._data.get_nodes(sets='LD_plates', kind='shell', disconnected=False)
        nodes_verified = self._gr_verified['nodes']
        self.assertTrue(np.allclose(nodes, nodes_verified))

    def test_get_elements(self):
        elems = self._data.get_elements(sets='LD_plates', kind='shell', disconnected=False)
        connectivity = self._gr_verified['connectivity']
        offset = self._gr_verified['offset']
        eltyp = self._gr_verified['eltyp']
        self.assertTrue(np.allclose(elems[0], connectivity))
        self.assertTrue(np.allclose(elems[1], offset))
        self.assertTrue(np.allclose(elems[2], eltyp))

    def test_get_noderesults_displacement(self):
        res = self._data.get_noderesults('displacement', rescases=1,
                                         sets='LD_plates', disconnected=False)
        res_verified = self._gr_verified['displacement']
        self.assertTrue(np.allclose(res, res_verified))


class TestStrucDataCase03(unittest.TestCase):
    """1st order beam elements, element results
    """

    @classmethod
    def setUpClass(cls):
        # establish StrucData instances and associated verification data
        cls._data = fs.open_sif('files/struc/single_super_elem/test01_1stord_linstat_R1.SIU')
        cls._f_verified = h5py.File('files/verified_testdata.h5', 'r')
        cls._gr_verified = cls._f_verified['test01_1stord_linstat_R1/LD_beams/elemres']
        cls._sets = ['LD_chords', 'LD_beams']

    @classmethod
    def tearDownClass(cls):
        cls._data.close()
        cls._f_verified.close()

    def test_get_nodes(self):
        nodes = self._data.get_nodes(sets=self._sets, kind='beam', disconnected=True)
        nodes_verified = self._gr_verified['nodes']
        self.assertTrue(np.allclose(nodes, nodes_verified))

    def test_get_elements(self):
        elems = self._data.get_elements(sets=self._sets, kind='beam', disconnected=True)
        connectivity = self._gr_verified['connectivity']
        offset = self._gr_verified['offset']
        eltyp = self._gr_verified['eltyp']
        self.assertTrue(np.allclose(elems[0], connectivity))
        self.assertTrue(np.allclose(elems[1], offset))
        self.assertTrue(np.allclose(elems[2], eltyp))

    def test_get_elementresults_beamforce(self):
        res = self._data.get_elementresults('beamforce', rescases=1, sets=self._sets)
        res_verified = self._gr_verified['beamforce']
        self.assertTrue(np.allclose(res, res_verified))


if __name__ == '__main__':
    unittest.main()