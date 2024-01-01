from django import template

register = template.Library()


# f"<a href='{id}' class='badge badge-primary'>{str(name)}</a>"

def tags(quote_tags):
    return quote_tags.all()


register.filter('tags', tags)
