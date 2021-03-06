# -*- coding: utf-8 -*-
#
# Copyright (c) 2015-2017 Kevin Deldycke <kevin@deldycke.com>
#                         and contributors.
# All Rights Reserved.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import unittest

from chessboard import Bishop, Board, King, Knight, Queen, Rook


class TestKing(unittest.TestCase):

    def test_territory(self):
        """ Test computation of territory at each positions of a 3x3 board. """
        board = Board(3, 3)
        c2i = board.coordinates_to_index
        assert King(board, c2i(1, 1)).territory == [
            True, True, True,
            True, True, True,
            True, True, True,
        ]
        assert King(board, c2i(0, 0)).territory == [
            True, True, False,
            True, True, False,
            False, False, False,
        ]
        assert King(board, c2i(1, 0)).territory == [
            True, True, True,
            True, True, True,
            False, False, False,
        ]
        assert King(board, c2i(2, 0)).territory == [
            False, True, True,
            False, True, True,
            False, False, False,
        ]
        assert King(board, c2i(2, 1)).territory == [
            False, True, True,
            False, True, True,
            False, True, True,
        ]
        assert King(board, c2i(2, 2)).territory == [
            False, False, False,
            False, True, True,
            False, True, True,
        ]
        assert King(board, c2i(1, 2)).territory == [
            False, False, False,
            True, True, True,
            True, True, True,
        ]
        assert King(board, c2i(0, 2)).territory == [
            False, False, False,
            True, True, False,
            True, True, False,
        ]
        assert King(board, c2i(0, 1)).territory == [
            True, True, False,
            True, True, False,
            True, True, False,
        ]


class TestQueen(unittest.TestCase):

    def test_territory(self):
        """ Test computation of territory at each positions of a 3x3 board. """
        board = Board(3, 3)
        c2i = board.coordinates_to_index
        assert Queen(board, c2i(1, 1)).territory == [
            True, True, True,
            True, True, True,
            True, True, True,
        ]
        assert Queen(board, c2i(0, 0)).territory == [
            True, True, True,
            True, True, False,
            True, False, True,
        ]
        assert Queen(board, c2i(1, 0)).territory == [
            True, True, True,
            True, True, True,
            False, True, False,
        ]
        assert Queen(board, c2i(2, 0)).territory == [
            True, True, True,
            False, True, True,
            True, False, True,
        ]
        assert Queen(board, c2i(2, 1)).territory == [
            False, True, True,
            True, True, True,
            False, True, True,
        ]
        assert Queen(board, c2i(2, 2)).territory == [
            True, False, True,
            False, True, True,
            True, True, True,
        ]
        assert Queen(board, c2i(1, 2)).territory == [
            False, True, False,
            True, True, True,
            True, True, True,
        ]
        assert Queen(board, c2i(0, 2)).territory == [
            True, False, True,
            True, True, False,
            True, True, True,
        ]
        assert Queen(board, c2i(0, 1)).territory == [
            True, True, False,
            True, True, True,
            True, True, False,
        ]


class TestRook(unittest.TestCase):

    def test_territory(self):
        """ Test computation of territory at each positions of a 3x3 board. """
        board = Board(3, 3)
        c2i = board.coordinates_to_index
        assert Rook(board, c2i(1, 1)).territory == [
            False, True, False,
            True, True, True,
            False, True, False,
        ]
        assert Rook(board, c2i(0, 0)).territory == [
            True, True, True,
            True, False, False,
            True, False, False,
        ]
        assert Rook(board, c2i(1, 0)).territory == [
            True, True, True,
            False, True, False,
            False, True, False,
        ]
        assert Rook(board, c2i(2, 0)).territory == [
            True, True, True,
            False, False, True,
            False, False, True,
        ]
        assert Rook(board, c2i(2, 1)).territory == [
            False, False, True,
            True, True, True,
            False, False, True,
        ]
        assert Rook(board, c2i(2, 2)).territory == [
            False, False, True,
            False, False, True,
            True, True, True,
        ]
        assert Rook(board, c2i(1, 2)).territory == [
            False, True, False,
            False, True, False,
            True, True, True,
        ]
        assert Rook(board, c2i(0, 2)).territory == [
            True, False, False,
            True, False, False,
            True, True, True,
        ]
        assert Rook(board, c2i(0, 1)).territory == [
            True, False, False,
            True, True, True,
            True, False, False,
        ]


class TestBishop(unittest.TestCase):

    def test_territory(self):
        """ Test computation of territory at each positions of a 3x3 board. """
        board = Board(3, 3)
        c2i = board.coordinates_to_index
        assert Bishop(board, c2i(1, 1)).territory == [
            True, False, True,
            False, True, False,
            True, False, True,
        ]
        assert Bishop(board, c2i(0, 0)).territory == [
            True, False, False,
            False, True, False,
            False, False, True,
        ]
        assert Bishop(board, c2i(1, 0)).territory == [
            False, True, False,
            True, False, True,
            False, False, False,
        ]
        assert Bishop(board, c2i(2, 0)).territory == [
            False, False, True,
            False, True, False,
            True, False, False,
        ]
        assert Bishop(board, c2i(2, 1)).territory == [
            False, True, False,
            False, False, True,
            False, True, False,
        ]
        assert Bishop(board, c2i(2, 2)).territory == [
            True, False, False,
            False, True, False,
            False, False, True,
        ]
        assert Bishop(board, c2i(1, 2)).territory == [
            False, False, False,
            True, False, True,
            False, True, False,
        ]
        assert Bishop(board, c2i(0, 2)).territory == [
            False, False, True,
            False, True, False,
            True, False, False,
        ]
        assert Bishop(board, c2i(0, 1)).territory == [
            False, True, False,
            True, False, False,
            False, True, False,
        ]


class TestKnight(unittest.TestCase):

    def test_territory(self):
        """ Test computation of territory at each positions of a 3x3 board. """
        board = Board(3, 3)
        c2i = board.coordinates_to_index
        assert Knight(board, c2i(1, 1)).territory == [
            False, False, False,
            False, True, False,
            False, False, False,
        ]
        assert Knight(board, c2i(0, 0)).territory == [
            True, False, False,
            False, False, True,
            False, True, False,
        ]
        assert Knight(board, c2i(1, 0)).territory == [
            False, True, False,
            False, False, False,
            True, False, True,
        ]
        assert Knight(board, c2i(2, 0)).territory == [
            False, False, True,
            True, False, False,
            False, True, False,
        ]
        assert Knight(board, c2i(2, 1)).territory == [
            True, False, False,
            False, False, True,
            True, False, False,
        ]
        assert Knight(board, c2i(2, 2)).territory == [
            False, True, False,
            True, False, False,
            False, False, True,
        ]
        assert Knight(board, c2i(1, 2)).territory == [
            True, False, True,
            False, False, False,
            False, True, False,
        ]
        assert Knight(board, c2i(0, 2)).territory == [
            False, True, False,
            False, False, True,
            True, False, False,
        ]
        assert Knight(board, c2i(0, 1)).territory == [
            False, False, True,
            True, False, False,
            False, False, True,
        ]
