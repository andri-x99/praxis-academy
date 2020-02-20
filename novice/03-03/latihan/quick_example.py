from jinja2 import Template

t = Template("Hello {{ something }}!")
t.render(something="World")

print(t.render())
print("")


y = Template("Nomor Favoritmu :{% for n in range(1,20) %} {{n}} " "{% endfor %}")
y.render()

print(y.render())
