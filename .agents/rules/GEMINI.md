---
trigger: always_on
---

# Django API Development Rules

## 1. FilterSet for Frontend (FE)
- For filters intended for frontend usage, **always use `FilterSet`**.
- At the view/viewset level, define the `filterset_class` as a `property` to easily customize it for different actions, including custom actions.

## 2. Serializer Initialization
- **DO NOT** instantiate a serializer directly by calling the class (e.g., `MySerializer(...)`).
- **INSTEAD**, you must use the methods `get_serializer()`, `get_serializer_class()`, or `get_serializer_kwargs()` to initialize serializer instances.

## 3. View Logic
- **Do not write computational logic inside views.** Move all complex computational logic into the **serializer**.
- In the view, there should only be one standard logic flow: call the queryset, paginate, call the serializer, and return data. This applies to all actions, including custom ones.

## 4. Multi-value Filters
- For filters handling multiple values (e.g., filtering by multiple statuses, multiple names), you **must use `BaseInFilter`** ([Docs](https://django-filter.readthedocs.io/en/latest/ref/filters.html#django_filters.filters.BaseInFilter)).
- Advantages:
  - Convenient for the frontend, which can pass arguments as a comma-separated string: `status__in=value1,value2`.
  - The backend will not raise an error if an invalid value is passed.

---

# Examples

## Example for the `filterset_class` property:

**🛑 DO NOT:**
```python
class SomeViewSet(ModelViewSet):
    filterset_class = FilterSet
```

**✅ DO:**
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
    
    @action(detail=False, ...)
    def custom_action(self, request, *args, **kwargs):
        return Response(...)
```

## 🚫 Forbidden
- ❌ No new dependencies without approval.
- ❌ No direct commits to `master`.

## 🧪 Testing Guidelines
- **Mandatory**: Every code change must have tests.
- **Framework**: Pytest. Do NOT mock the database. Always use the `@pytest.mark.django_db` decorator for tests that interact with the database.
### Language & i18n
- **English Only**: 100% of code, comments, and docstrings must be in English.

## 🐍 Environment Management
- **Tool**: Poetry.
- **Virtual Env**: `.venv` or `venv`. Always search and activate virtual env before performing any commands
- **Requirement**: Always use `poetry run` for shell commands (pytest, ruff, etc.).
