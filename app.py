import os
import subprocess
import re

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)

@app.route('/gitversion')
def git_version():
    #replace with relevant git repo url
    repo_url = "https://github.com/anbuselvidemo/KUBEDEMO"
    getversioncommand = "git ls-remote "+ repo_url
    process = subprocess.Popen([getversioncommand], shell=True, stdin=None, stdout=subprocess.PIPE, executable="/bin/bash")
    stdout, stderr = process.communicate()
    sha = re.split(r'\t+', stdout.decode('ascii'))[0]
    return (sha)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
