from django import template

register = template.Library()


@register.simple_tag
def query_transform(request, **kwargs):
    updated = request.GET.copy()
    updated.update({key: value for key, value in kwargs.items() if value is not None})
    for key, value in list(updated.items()):
        if value == 0:
            del updated[key]

    return updated.urlencode()
