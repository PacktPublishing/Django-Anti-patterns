# Example of a Fat Model in Django


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def price(self):

        return self.item.price * self.quantity

    def update_stock(self):

        self.item.stock -= self.quantity

        self.item.save()

    def send_confirmation_email(self):

        send_mail(
            "Order Confirmation",
            "Thank you for your order.",
            "from@example.com",
            [self.user.email],
            fail_silently=False,
        )
