import pytest
from tests.to_test import Bank, BankAccount


def test_BankAccount():
    account = BankAccount()
    account.deposit(300)
    assert account.balance == 300
    account.deposit(-200)
    assert account.balance == 300
    account.withdraw(100)
    assert account.balance == 200
    account.withdraw(300)
    assert account.balance == 200
def test_Bank():
    banca = Bank()

    banca.deposit(300)
    assert banca.account.balance == 300
    banca.deposit(-200)
    assert banca.account.balance == 300
    banca.withdraw(100)
    assert banca.account.balance == 200
    banca.withdraw(300)
    assert banca.account.balance == 200

   # savings_account
    banca.deposit_savings(300)
    assert banca.savings_account.balance == 300

    banca.deposit_savings(-200)
    assert banca.savings_account.balance == 300

    banca.withdraw_savings(100)
    assert banca.savings_account.balance == 200

    banca.withdraw_savings(300)
    assert banca.savings_account.balance == 200


