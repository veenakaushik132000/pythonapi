# List branches for HEAD commit

import requests

base_url = "https://api.github.com/"
token = "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"


def list_head_commit(owner,repo,commit_sha):
    url = base_url + "repos/" + owner + "/" + repo + "/commits" + "/" + commit_sha + "/branches-where-head"
    print(url)
    req = requests.get(url, auth=(token,''))
    print(req)
    print(req.json())

list_head_commit("veenakaushik132000","Terraform_assignment","9d5885a1dfa129ab443f945740ecf48b6a7d23b5")




# https://api.github.com/repos/amar1452001/PythonSprint2PracticeCEQ508/commits/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/branches-where-head
# <Response [200]>
# []