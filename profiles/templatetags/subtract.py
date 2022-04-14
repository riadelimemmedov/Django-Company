from django import template

register = template.Library()

@register.filter
def subtract(value,value1):
    print(value)#execution
    print(value1)#plan
    try:
        return value - value1
    except:
        print('Error Subtract')