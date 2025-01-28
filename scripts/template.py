from jinja2 import Environment, FileSystemLoader
import json, os

env = Environment(loader= FileSystemLoader("scripts\\templates"))
template = env.get_template("test_report.tex.j2")

data_file = "build/results.json"

with open(data_file, "r") as file:
    data = json.load(file)

output = template.render(data)

out_dir = "build/test_report"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

with open (os.path.join(out_dir, "test_report.tex"), "w") as f:
    f.write(output)
