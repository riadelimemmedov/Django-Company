from django import template

register = template.Library()

@register.filter
def oknok(value,value1):
    print(value)#execution
    print(value1)#plan
    
    try:
        if(value-value1)>=0:
            return 'OK'
        else:
            return 'Not OK'
    except:
        print('Error OkNot')
