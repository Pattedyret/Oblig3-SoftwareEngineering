import pytest
from leapyear import isLeapYear


def test1_leap_years(): #For alle årene som er delbare med 4 med ikke med 100 
    assert isLeapYear(2004) == True
    assert isLeapYear(2008) == True
    assert isLeapYear(2012) == True

def test2_century_leap_years(): #For alle årene som er delbare med 400
    assert isLeapYear(1600) == True
    assert isLeapYear(2000) == True
    assert isLeapYear(2400) == True

def test3_century_non_leap_years(): #For alle årene som er delbare med 100 men ikke med 4
    assert isLeapYear(1700) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1900) == False
    assert isLeapYear(2100) == False

def test4_non_leap_years(): #For alle årene som ikke er delbare med noen deler
    assert isLeapYear(2001) == False
    assert isLeapYear(2002) == False
    assert isLeapYear(2003) == False