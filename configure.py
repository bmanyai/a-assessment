import yaml
from jinja2 import Template

with open('config.yml') as fd:
    data = yaml.load(fd)

for k, v in data.items():
    t = Template(v)
    data[k] = t.render(**data)

print yaml.safe_dump(data, default_flow_style=False)
