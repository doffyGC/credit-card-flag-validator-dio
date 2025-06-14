import sys
from credit_card import credit_card

card_input = sys.argv[1] 

credit_card = credit_card(card_input)
brand = credit_card.validate_brand()

print(f"The credit card brand is: {brand}")