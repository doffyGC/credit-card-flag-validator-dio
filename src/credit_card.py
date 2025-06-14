import re

class credit_card:
    """
    A class to represent a credit card.
    """

    def __init__(self, number: str):
        """
        Initialize the credit card with a number.
        Args:
            number (str): The credit card number as a string.
        """
        self.number = number

    def validate_brand(self) -> str:
        """
        Validate the brand of a credit card based on its number.
        
        """
        number = re.sub(r'\D', '', self.number)

        brands = [
            ("Mastercard", r"^5[1-5][0-9]{14}$|^2(2[2-9][1-9]|2[3-9][0-9]|[3-6][0-9]{2}|7[01][0-9]|720)[0-9]{12}$"),
            ("Visa", r"^4[0-9]{15}$"),
            ("American Express", r"^3[47][0-9]{13}$"),
            ("Diners Club", r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$"),
            ("Discover", r"^6(?:011|5[0-9]{2})[0-9]{12}$"),
            ("Enroute", r"^2(014|149)[0-9]{11}$"),
            ("JCB", r"^(?:2131|1800|35\d{3})\d{11}$"),
            ("Voyager", r"^8699[0-9]{11}$"),
            ("Hipercard", r"^(606282\d{10}(\d{3})?)|(3841\d{15})$"),
            ("Aura", r"^50[0-9]{14,17}$"),
        ]

        for name, pattern in brands:
            if re.match(pattern, number):
                return name
        return "Unknown"