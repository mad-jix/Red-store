from django import template

register=template.Library()


@register.simple_tag(name='status')
def status(status):
    status=status-1
    status_array=['order confomed','order delivered','order canceled']
    return status_array[status]