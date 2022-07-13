#version one
def make_lambda(params, body):
    return eval("lambda " + params + ": " + body)

#version two
def make_lambda(params, body):
    return eval(f"lambda {params}: {body}")