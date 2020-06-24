#!/usr/bin/python

#Python setup
#sudo pip install pytest

#Import libraries
import pytest



def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5

test_answer()



