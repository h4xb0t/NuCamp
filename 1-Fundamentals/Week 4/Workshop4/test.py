#!/usr/bin/env python
import unittest
from workshop4 import User
from workshop4 import BankUser


class UserTest(unittest.TestCase):

    def setUp(self):
        self.user = User('Bob', 1234, 'password')
        self.bank_user = BankUser('Bob', 1234, 'password')

    def test_user_name(self):
        self.assertEqual(self.user.name, 'Bob')

    def test_user_pin(self):
        self.assertEqual(self.user.pin, 1234)

    def test_user_password(self):
        self.assertEqual(self.user.password, 'password')

    def test_change_name(self):
        self.user.change_name("Robert")
        self.assertEqual(self.user.name, "Robert")

    def test_change_pin(self):
        self.user.change_pin(4567)
        self.assertEqual(self.user.pin, 4567)

    def test_change_password(self):
        self.user.change_password("newpassword")
        self.assertEqual(self.user.password, "newpassword")

    def test_bank_user_class(self):
        self.assertIsInstance(self.bank_user, User)

    def test_bank_user_balance(self):
        self.assertEqual(self.bank_user.balance, 0)

    def test_bank_user__show_balance(self):
        self.bank_user.show_balance()
        self.assertEqual(self.bank_user.show_balance(), None)

    def test_bank_user_withdraw(self):
        self.bank_user.withdraw(3)
        self.assertEqual(self.bank_user.balance, -3)

    def test_bank_user_deposit(self):
        self.bank_user.deposit(3)
        self.assertEqual(self.bank_user.balance, 3)
