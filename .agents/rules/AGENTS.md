# AI Agent Directives for Django API Development

You are an AI Agent assisting with a Django/Django Rest Framework project. You MUST strictly adhere to the following deterministic rules for all code generation, refactoring, and execution.

## 1. Architectural & View Constraints
- **Zero View Logic:** NEVER write computational or business logic inside Views or ViewSets. All complex logic and data manipulation MUST be delegated to the Serializer.
- **Standardized View Flow:** Every View or custom `@action` MUST strictly follow this linear flow: retrieve queryset -> apply pagination -> instantiate serializer -> return response.
- **Serializer Instantiation:** NEVER instantiate a serializer class directly (e.g., `MySerializer(data=...)`). You MUST use `self.get_serializer()`, `self.get_serializer_class()`, or `self.get_serializer_kwargs()`.

## 2. Filtering Standards
- **FilterSet Enforcement:** You MUST use `django-filters.FilterSet` for all frontend-facing filter implementations.
- **Dynamic filterset_class:** At the view/viewset level, define `filterset_class` as a `@property`. This ensures accurate dynamic resolution of FilterSets based on `self.action`.
- **Multi-value Parameters:** For query parameters that accept comma-separated multiple values (e.g., `status__in=value1,value2`), you MUST implement `BaseInFilter` from `django_filters`.

## 3. Testing Requirements
- **Test Coverage:** Every code modification or new feature MUST include corresponding Pytest tests.
- **Database Interaction:** DO NOT mock the database. You MUST use the `@pytest.mark.django_db` decorator for any test that interacts with the database.

## 4. Environment & Execution Protocol
- **Virtual Environment:** Always locate and activate the virtual environment (`.venv` or `venv`) before executing any terminal commands.
- **Package Manager:** You MUST use `poetry run` for all shell commands (e.g., `poetry run pytest`, `poetry run ruff`).
- **Git Restrictions:** NEVER perform Git operations (add, commit, push) or modify protected branches (e.g., `master`) unless explicitly instructed by the user.

## 5. Language Concurrency
- **English Only:** 100% of generated code, variables, classes, inline comments, and docstrings MUST be written in English.

## 6. Implementation Examples

**INCORRECT (Do not use static assignment):**
```python
class SomeViewSet(ModelViewSet):
    filterset_class = FilterSet
```
**CORRECT (Use property for dynamic assignment):**
```python
class ListFilterSet(FilterSet):
    pass

class CustomActionFilterSet(FilterSet):
    pass

class SomeViewSet(ModelViewSet):
    @property
    def filterset_class(self):
        if self.action == "list":
            return ListFilterSet
        elif self.action == "custom_action":
            return CustomActionFilterSet
        return FilterSet

    @action(detail=False, methods=["get"])
    def custom_action(self, request, *args, **kwargs):
        # Implementation here
        pass
```