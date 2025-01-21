from django import template

register=template.Library()

@register.filter(name='chunk')
def chunk(lst,chunk_size):
    chunk=[]
    i=0
    for x in lst:
        chunk.append(x)
        i=i+1
        if i==chunk_size:
            yield chunk
            chunk=[]
    yield chunk