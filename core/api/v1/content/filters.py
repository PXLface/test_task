from ninja import Schema


class ContentFilters(Schema):
    search: str | None = None
