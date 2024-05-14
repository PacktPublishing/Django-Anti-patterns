class FatModel(models.Model):

    def complex_operation(self):

        # Complex business logic in model

        pass


def thin_view(request):

    obj = FatModel.objects.get(id=1)

    result = obj.complex_operation()

    return HttpResponse(result)
