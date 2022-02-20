from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def is_booked(room, date):
    print(room, date)
