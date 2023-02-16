#List pull requests associated with a commit

import requests


base_url="https://api.github.com/"
token="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"


def list_pull_commit(owner,repo,commit_sha):
    url = base_url + "repos/" + owner + "/" + repo + "/commits" + "/" + commit_sha + "/pulls"
    print(url)
    req = requests.get(url, auth=(token,''))
    print(req)
    return req.json()
print(list_pull_commit("amar1452001","PythonSprint2PracticeCEQ508","9d5885a1dfa129ab443f945740ecf48b6a7d23b5"))



# https://api.github.com/repos/amar1452001/PythonSprint2PracticeCEQ508/commits/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/pulls
# <Response [200]>
# []