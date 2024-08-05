from decimal import Decimal
from typing import Iterable
from payments import PurchasedItem
from payments.models import BasePayment
from django.db import models

class Payment(BasePayment):
    course = models.CharField(max_length=50, blank=False, default="")

    def __str__(self):
        return f"{self.id} - {self.transaction_id}"

    def get_failure_url(self) -> str:
        return ""

    def get_success_url(self) -> str:
        return ""

    def get_purchased_items(self) -> Iterable[PurchasedItem]:
        return [
            PurchasedItem(
                name=self.description,
                sku='',
                quantity=1,
                price=Decimal(self.total),
                currency=self.currency,
            )
        ]
    