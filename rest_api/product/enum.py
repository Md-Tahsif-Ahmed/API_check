class DiscountType:
    PERCENTAGE = "Percentage"
    FLAT_AMOUNT = "Flat Amount"
    SUPPORTED_DISCOUNT_TYPES = [PERCENTAGE, FLAT_AMOUNT]
	
    CHOICES = (
		(PERCENTAGE, "Percentage"),
		(FLAT_AMOUNT, "Flat Amount"),
	)
