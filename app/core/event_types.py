from __future__ import annotations

from app.core.config import settings


def _normalize(values: list[str]) -> frozenset[str]:
    return frozenset(value.strip() for value in values if value and value.strip())


POSITIVE_EVENT_TYPES = _normalize(settings.positive_event_types)
VIEW_EVENT_TYPES = _normalize(settings.view_event_types)
INTERMEDIATE_POSITIVE_EVENT_TYPES = _normalize(settings.intermediate_positive_event_types)
TERMINAL_POSITIVE_EVENT_TYPES = _normalize(settings.terminal_positive_event_types)
