class Invoice(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    service_date = models.DateField()

    due_date = models.DateField()

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_due_date(self):

        return self.service_date + timedelta(days=30)

    def generate_invoice_number(self):

        return f"INV-{self.id}/{self.service_date.year}"

    def send_invoice_email(self):

        # Email sending logic here

        pass
