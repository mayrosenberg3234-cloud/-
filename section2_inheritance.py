class Security:
    def __init__(self, symbol, market_price, currency):
        self.symbol = symbol
        self.market_price = market_price
        self.currency = currency

    def get_base_info(self):
        return f"{self.symbol} trading at {self.market_price} {self.currency}"

class Stock(Security):
    def __init__(self, symbol, market_price, currency, dividend_yield):
        super().__init__(symbol, market_price, currency)
        self.dividend_yield = dividend_yield

    def calculate_dividend_payout(self, shares_owned):
        return self.market_price * self.dividend_yield * shares_owned

    def get_description(self):
        return "Stocks: Ownership in a company."

class Bond(Security):
    def __init__(self, symbol, market_price, currency, coupon_rate, maturity_date):
        super().__init__(symbol, market_price, currency)
        self.coupon_rate = coupon_rate
        self.maturity_date = maturity_date

    def calculate_annual_coupon(self, face_value):
        return face_value * self.coupon_rate
    
    def get_description(self):
        return "Bond: A fixed-income loan to an entity."

class Option(Security):
    def __init__(self, symbol, market_price, currency, strike_price, expiry_date):
        super().__init__(symbol, market_price, currency)
        self.strike_price = strike_price
        self.expiry_date = expiry_date

    def is_in_the_money(self):
        if self.market_price > self.strike_price:
            return True
        return False
    
    def get_description(self):
        return "Option: A contract to buy/sell assets."

def main_section_2():
    print("Section 2: Inheritance")

    securities = []
    
    s1 = Stock("AAPL", 150.0, "USD", 0.005)
    securities.append(s1)

    b1 = Bond("US10Y", 98.0, "USD", 0.04, "2030-01-01")
    securities.append(b1)

    o1 = Option("TSLA_CALL", 50.0, "USD", 240.0, "2023-12-15")
    securities.append(o1)

    print("\n Your Portfolio ")
    for sec in securities:
        print(f"Type: {type(sec).__name__}")
        print(sec.get_base_info())
        
        if isinstance(sec, Stock):
            print(f" Est. Dividend for 100 shares: {sec.calculate_dividend_payout(100):.2f}")
        elif isinstance(sec, Bond):
            print(f" Annual Coupon for 1000 face: {sec.calculate_annual_coupon(1000):.2f}")
        elif isinstance(sec, Option):
            print(f" In the Money? {sec.is_in_the_money()}")
        print("-" * 20)


if __name__ == "__main__":
    main_section_2()

#2.	מטרת ההורשה היא לאפשר למחלקות חדשות (ילד/נגזר) לקבל (לרשת) תכונות ומתודות ממחלקות קיימות (המהוות כהורה/כבסיס) ובכך להגדיר היררכיה בין מחלקות. התוצאה היא שימוש חוזר בקוד, הפחתת כפילויות בהתאם לעקרון DRY, והיכולת להגדיר התנהגות כללית במחלקת הבסיס לצד התנהגויות ייחודיות במחלקות הנגזרות.