'''2'''
#2.1
def make_lambda(params, body):
    return eval("lambda " + params + ": " + body)
#2.2
def make_lambda(params, body):
    return eval(f"lambda {params}: {body}")