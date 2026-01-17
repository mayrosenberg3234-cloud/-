class Invoice:
    def __init__(self, invoice_id, client_name, amount, date, is_paid=False):
        self.invoice_id = invoice_id
        self._client_name = client_name
        self.__amount = amount
        self.date = date
        self.is_paid = is_paid

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("Error: The amount must be positive, cannot be negative.")
        else:
            self.__amount = value

    def calculate_vat(self, vat_rate=0.17):
        return self.__amount * vat_rate

    def calculate_total_with_vat(self, vat_rate=0.17):
        return self.__amount * (1 + vat_rate)
    
    def mark_as_paid(self):
        self.is_paid = True
        print(f"Invoice {self.invoice_id} is paid.")

    def __str__(self):
        return f"Invoice({self.invoice_id}) for {self._client_name}: {self.__amount} on {self.date}. Paid: {self.is_paid}"


def main_section_1():
    print("Section 1: Encapsulation")
    
    inv_id = "1001"
    client = "Acme Corp"
    amt = 500.0
    date_str = "2023-10-27"

    inv = Invoice(inv_id, client, amt, date_str)


    print("\nOriginal Invoice:")
    print(inv)

    new_amt = 1000
    print(f"\nUpdating amount to {new_amt}...")
    inv.amount = new_amt
    
    print(f"New Amount is: {inv.amount}")

    print(f"VAT (17%): {inv.calculate_vat():.2f}")
    print(f"Total with VAT: {inv.calculate_total_with_vat():.2f}")

    inv.mark_as_paid()
    print("\nFinal State:")
    print(inv)


if __name__ == "__main__":
    main_section_1()
