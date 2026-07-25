# Encapsulation:

Bind data and methods inside class
no direct access to private data
controllec access {public, private}
public :
self.balance
private :
self.\_\_balance

used for security purposes
manages which methods and attributes are accessible to user.

PiggyBank (the capsule)
┌─────────────────────────┐
│ \_\_money = 50 │ ← hidden inside, protected
│ │
│ add_money() ← door in │ ← the only way to change it
│ check_money() ← door out│ ← the only way to read it
└─────────────────────────┘
