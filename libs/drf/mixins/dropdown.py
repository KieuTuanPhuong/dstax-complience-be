from rest_framework.decorators import action


class DropdownMixin:
    dropdown_serializer_class = None

    def get_serializer_class(self):
        if self.action == "dropdown":
            return self.dropdown_serializer_class
        return super().get_serializer_class()

    @action(detail=False, methods=["get"])
    def dropdown(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
