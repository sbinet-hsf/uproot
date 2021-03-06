#!/usr/bin/env python

# Copyright 2017 DIANA-HEP
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import numpy

import uproot

class TestCompression(unittest.TestCase):
    def runTest(self):
        pass
    
    def test_compression_identity(self):
        self.assertEqual(uproot.open("tests/Zmumu-zlib.root").compression.algo, "zlib")
        self.assertEqual(uproot.open("tests/Zmumu-zlib.root").compression.level, 4)

        self.assertEqual(uproot.open("tests/Zmumu-lzma.root").compression.algo, "lzma")
        self.assertEqual(uproot.open("tests/Zmumu-lzma.root").compression.level, 4)

        self.assertEqual(uproot.open("tests/Zmumu-lz4.root").compression.algo, "lz4")
        self.assertEqual(uproot.open("tests/Zmumu-lz4.root").compression.level, 4)

        self.assertEqual(uproot.open("tests/Zmumu-uncompressed.root").compression.level, 0)

        self.assertEqual(uproot.open("tests/HZZ-zlib.root").compression.algo, "zlib")
        self.assertEqual(uproot.open("tests/HZZ-zlib.root").compression.level, 4)

        self.assertEqual(uproot.open("tests/HZZ-lzma.root").compression.algo, "lzma")
        self.assertEqual(uproot.open("tests/HZZ-lzma.root").compression.level, 4)

        self.assertEqual(uproot.open("tests/HZZ-lz4.root").compression.algo, "lz4")
        self.assertEqual(uproot.open("tests/HZZ-lz4.root").compression.level, 4)

        self.assertEqual(uproot.open("tests/HZZ-uncompressed.root").compression.level, 0)

    def test_compression_keys(self):
        keys = uproot.open("tests/Zmumu-uncompressed.root").contents
        self.assertEqual(uproot.open("tests/Zmumu-zlib.root").contents, keys)
        self.assertEqual(uproot.open("tests/Zmumu-lzma.root").contents, keys)
        self.assertEqual(uproot.open("tests/Zmumu-lz4.root").contents, keys)

        keys = uproot.open("tests/HZZ-uncompressed.root").contents
        self.assertEqual(uproot.open("tests/HZZ-zlib.root").contents, keys)
        self.assertEqual(uproot.open("tests/HZZ-lzma.root").contents, keys)
        self.assertEqual(uproot.open("tests/HZZ-lz4.root").contents, keys)

    def test_compression_branches(self):
        branches = uproot.open("tests/Zmumu-uncompressed.root")["events"].branchnames
        self.assertEqual(uproot.open("tests/Zmumu-zlib.root")["events"].branchnames, branches)
        self.assertEqual(uproot.open("tests/Zmumu-lzma.root")["events"].branchnames, branches)
        self.assertEqual(uproot.open("tests/Zmumu-lz4.root")["events"].branchnames, branches)

        branches = uproot.open("tests/HZZ-uncompressed.root")["events"].branchnames
        self.assertEqual(uproot.open("tests/HZZ-zlib.root")["events"].branchnames, branches)
        self.assertEqual(uproot.open("tests/HZZ-lzma.root")["events"].branchnames, branches)
        self.assertEqual(uproot.open("tests/HZZ-lz4.root")["events"].branchnames, branches)

    def test_compression_content(self):    
        for name, array in uproot.open("tests/Zmumu-uncompressed.root")["events"].arrays().items():
            self.assertTrue(numpy.array_equal(uproot.open("tests/Zmumu-zlib.root")["events"].array(name), array))
            self.assertTrue(numpy.array_equal(uproot.open("tests/Zmumu-lzma.root")["events"].array(name), array))
            self.assertTrue(numpy.array_equal(uproot.open("tests/Zmumu-lz4.root")["events"].array(name), array))

        array = uproot.open("tests/HZZ-uncompressed.root")["events"].array("Electron_Px")
        self.assertTrue(numpy.array_equal(uproot.open("tests/HZZ-zlib.root")["events"].array("Electron_Px"), array))
        self.assertTrue(numpy.array_equal(uproot.open("tests/HZZ-lzma.root")["events"].array("Electron_Px"), array))
        self.assertTrue(numpy.array_equal(uproot.open("tests/HZZ-lz4.root")["events"].array("Electron_Px"), array))
