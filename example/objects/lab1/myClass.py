#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BankAccount:
    """
    Class for handling a banck account
    """

    def __init__(self, owner):
        """
        Constructor for BankAccount
        """
        self._balance = 0.0
        self.owner = owner

    def showBalance(self):
        """
        Returns the current balance
        """
        return "%s has %g kr" %(self.owner, self._balance)

    def depositMoney(self, amount):
        """
        Add money to account
        """
        self._balance += amount

    def withdrawMoney(self, amount):
        """
        Take money from account
        """
        self._balance -= amount

    def  __add__(self, other):
        """
        Overloading add function
        """
        return self._addOther(other)

    def  __iadd__(self, other):
        """
        Overloading iadd(+=) function
        """
        self._balance = self._addOther(other)
        return self

    def _addOther(self,other):
        """
        Used by add, iadd to add self with other
        """
        if type(other) == int or type(other) == float:
            return float("{0:.2f}".format(self._balance + float(other)))
        else:
            return float("{0:.2f}".format(self._balance + other._balance))


class Cat:
    """
    Cat class for lab1 in oopython
    """

    nrOfPaws = 4

    def __init__(self, name, eColor, evil=True):
        """
        Constructor for Cat class
        """
        self.name = name
        self.eyeColor = eColor
        self.livesLeft = -1
        self._evil = evil

    @classmethod
    def catPaws(cls):
        """
        Returns number of paws
        """
        return "Cats have %s paws" % cls.nrOfPaws

    def description(self):
        """
        Returns a string containing a description of the cat
        """
        return 'My cats name is %s, has %s eyes and has %s lives left to live.' % (self.name, self.eyeColor, self.livesLeft)

    def isEvil(self):
        """
        Returns wether the cat is evil or not
        """
        return self._evil


class Dog:
    """
    Dog class for lab1 in oopython
    """

    def __init__(self, name, eColor):
        """
        Constructor for dog class
        """
        self.name = name
        self.eyeColor = eColor
        self.livesLeft = 1

    def description(self):
        """
        Returns a string containing a description of the dog
        """
        return 'My dogs name is %s, has %s eyes and has %s lives left to live.' % (self.name, self.eyeColor, self.livesLeft)