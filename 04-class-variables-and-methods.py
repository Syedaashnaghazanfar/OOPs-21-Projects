class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Create an instance of Bank
bank1 = Bank()
# Change the bank name using the class method
bank1.change_bank_name("XYZ Bank")
# Display the updated bank name
print(f"Updated Bank Name: {bank1.bank_name}")  # Output: Updated Bank Name: XYZ Bank
# The class method change_bank_name is used to modify the class variable bank_name.
# This allows all instances of the class to reflect the updated value.
# Class variables are shared among all instances of the class.
