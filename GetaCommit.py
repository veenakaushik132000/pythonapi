#Get Commit


import requests

base_url = "https://api.github.com/"
token = "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"


def get_commit(owner,repo,ref):
    url = base_url + "repos/" + owner + "/" + repo + "/commits" + "/" + ref
    print(url)
    req = requests.get(url, auth=(token,''))
    print(req)
    return req.json()
print(get_commit("amar1452001","PythonSprint2PracticeCEQ508","9d5885a"))





# <Response [200]>
# {'sha': '9d5885a1dfa129ab443f945740ecf48b6a7d23b5', 'node_id': 'C_kwDOI9J7IdoAKDlkNTg4NWExZGZhMTI5YWI0NDNmOTQ1NzQwZWNmNDhiNmE3ZDIzYjU', 'commit': {'author': {'name': 'amar1452001', 'email': 'amarjotsingh5555@gmail.com', 'date': '2023-02-13T06:23:11Z'}, 'committer': {'name': 'amar1452001', 'email': 'amarjotsingh5555@gmail.com', 'date': '2023-02-13T06:23:11Z'}, 'message': 'adding files', 'tree': {'sha': '1183758eb761fff784322661aeedfdadf540fbb3', 'url': 'https://api.github.com/repos/amar1452001/PythonSprint2PracticeCEQ508/git/trees/1183758eb761fff784322661aeedfdadf540fbb3'}, 'url': 'https://api.github.com/repos/amar1452001/PythonSprint2PracticeCEQ508/git/commits/9d5885a1dfa129ab443f945740ecf48b6a7d23b5', 'comment_count': 0, 'verification': {'verified': False, 'reason': 'unsigned', 'signature': None, 'payload': None}}, 'url': 'https://api.github.com/repos/amar1452001/PythonSprint2PracticeCEQ508/commits/9d5885a1dfa129ab443f945740ecf48b6a7d23b5', 'html_url': 'https://github.com/amar1452001/PythonSprint2PracticeCEQ508/commit/9d5885a1dfa129ab443f945740ecf48b6a7d23b5', 'comments_url': 'https://api.github.com/repos/amar1452001/PythonSprint2PracticeCEQ508/commits/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/comments', 'author': {'login': 'amar1452001', 'id': 60013210, 'node_id': 'MDQ6VXNlcjYwMDEzMjEw', 'avatar_url': 'https://avatars.githubusercontent.com/u/60013210?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/amar1452001', 'html_url': 'https://github.com/amar1452001', 'followers_url': 'https://api.github.com/users/amar1452001/followers', 'following_url': 'https://api.github.com/users/amar1452001/following{/other_user}', 'gists_url': 'https://api.github.com/users/amar1452001/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/amar1452001/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/amar1452001/subscriptions', 'organizations_url': 'https://api.github.com/users/amar1452001/orgs', 'repos_url': 'https://api.github.com/users/amar1452001/repos', 'events_url': 'https://api.github.com/users/amar1452001/events{/privacy}', 'received_events_url': 'https://api.github.com/users/amar1452001/received_events', 'type': 'User', 'site_admin': False}, 'committer': {'login': 'amar1452001', 'id': 60013210, 'node_id': 'MDQ6VXNlcjYwMDEzMjEw', 'avatar_url': 'https://avatars.githubusercontent.com/u/60013210?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/amar1452001', 'html_url': 'https://github.com/amar1452001', 'followers_url': 'https://api.github.com/users/amar1452001/followers', 'following_url': 'https://api.github.com/users/amar1452001/following{/other_user}', 'gists_url': 'https://api.github.com/users/amar1452001/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/amar1452001/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/amar1452001/subscriptions', 'organizations_url': 'https://api.github.com/users/amar1452001/orgs', 'repos_url': 'https://api.github.com/users/amar1452001/repos', 'events_url': 'https://api.github.com/users/amar1452001/events{/privacy}', 'received_events_url': 'https://api.github.com/users/amar1452001/received_events', 'type': 'User', 'site_admin': False}, 'parents': [], 'stats': {'total': 117, 'additions': 117, 'deletions': 0}, 'files': [{'sha': '879efa8cbd2a2955b4ef4743424b8d164214f827', 'filename': 'accessGithubList.py', 'status': 'added', 'additions': 16, 'deletions': 0, 'changes': 16, 'blob_url': 'https://github.com/amar1452001/PythonSprint2PracticeCEQ508/blob/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/accessGithubList.py', 'raw_url': 'https://github.com/amar1452001/PythonSprint2PracticeCEQ508/raw/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/accessGithubList.py', 'contents_url': 'https://api.github.com/repos/amar1452001/PythonSprint2PracticeCEQ508/contents/accessGithubList.py?ref=9d5885a1dfa129ab443f945740ecf48b6a7d23b5', 'patch': '@@ -0,0 +1,16 @@\n+#Code to access GITHUB Account\n+#in which i am going to LIST ALL BRANCHES\n+\n+import requests\n+\n+BASE_URL ="https://api.github.com/"\n+token ="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"\n+\n+def list_branch(owner,repo):\n+    url = BASE_URL + "repos/" + owner + "/" + repo + "/branches"\n+    print(url)\n+    req = requests.get(url, auth=(token,\'\'))\n+    print(req)\n+    return req.json()\n+\n+print(list_branch("amar1452001","portfolio")) \n\\ No newline at end of file'}, {'sha': 'b46d5380ae8abcc973071cdfc311f334974bcb37', 'filename': 'prac1.py', 'status': 'added', 'additions': 26, 'deletions': 0, 'changes': 26, 'blob_url': 'https://github.com/amar1452001/PythonSprint2PracticeCEQ508/blob/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/prac1.py', 'raw_url': 'https://github.com/amar1452001/PythonSprint2PracticeCEQ508/raw/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/prac1.py', 'contents_url': 'https://api.github.com/repos/amar1452001/PythonSprint2PracticeCEQ508/contents/prac1.py?ref=9d5885a1dfa129ab443f945740ecf48b6a7d23b5', 'patch': '@@ -0,0 +1,26 @@\n+"""\n+HTTP_METHOD    API_ENDPOINT                         DESCRIPTION\n+\n+GET            /customers                          Get a list of customers.\n+GET            /customer/<customer_id>             Get a single customer.\n+POST           /customer\n+\n+\n+\n+\n+"""\n+\n+\n+\n+\n+\n+\n+import requests\n+\n+response = requests.get("https://jsonplaceholder.typicode.com/todos/1")\n+print(response)\n+\n+print(response.json())\n+print(response.headers)\n+\n+'}, {'sha': '8d7525af39862d6b9731e97c5bddaa45d5e205d4', 'filename': 'privateGitCommit.py', 'status': 'added', 'additions': 13, 'deletions': 0, 'changes': 13, 'blob_url': 'https://github.com/amar1452001/PythonSprint2PracticeCEQ508/blob/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/privateGitCommit.py', 'raw_url': 'https://github.com/amar1452001/PythonSprint2PracticeCEQ508/raw/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/privateGitCommit.py', 'contents_url': 'https://api.github.com/repos/amar1452001/PythonSprint2PracticeCEQ508/contents/privateGitCommit.py?ref=9d5885a1dfa129ab443f945740ecf48b6a7d23b5', 'patch': '@@ -0,0 +1,13 @@\n+import requests\n+import json\n+\n+base_url = "https://api.github.com/"\n+token = "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"\n+def list_commit(owner,repo):\n+    url = base_url + "repos/" + owner + "/" + repo + "/commits"\n+    print(url)\n+    req = requests.get(url, auth=(token,\'\'))\n+    print(req)\n+    return req.json()\n+print(list_commit("amar1452001","portfolio"))\n+'}, {'sha': '04dda5f09f5edf232c28b0168630105582a3e817', 'filename': 'publicApi.py', 'status': 'added', 'additions': 62, 'deletions': 0, 'changes': 62, 'blob_url': 'https://github.com/amar1452001/PythonSprint2PracticeCEQ508/blob/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/publicApi.py', 'raw_url': 'https://github.com/amar1452001/PythonSprint2PracticeCEQ508/raw/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/publicApi.py', 'contents_url': 'https://api.github.com/repos/amar1452001/PythonSprint2PracticeCEQ508/contents/publicApi.py?ref=9d5885a1dfa129ab443f945740ecf48b6a7d23b5', 'patch': '@@ -0,0 +1,62 @@\n+import requests\n+\n+#BASE_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Tiger_King/daily/20210901/20210930"\n+\n+base_url = "https://api.github.com/"\n+token = "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"\n+\n+# def get_user():\n+#     url = base_url + "users"\n+#     print(url)\n+#     response = requests.get(url,auth=(token,\'\'))\n+#     print(response)\n+#     print(response.json())\n+# get_user()\n+\n+\n+\n+#Listing the commits of a particular repository named as PythonAssignment1cloudeqAmar\n+\n+# def list_commit(owner,repo):\n+#     url = base_url + "repos/" + owner + "/" + repo + "/commits"\n+#     print(url)\n+#     req = requests.get(url, auth=(token,\'\'))\n+#     print(req)\n+#     return req.json()\n+# print(list_commit("amar1452001","PythonAssignment1cloudeqAmar"))\n+\n+\n+\n+#listing branches for HEAD commits\n+\n+\n+# def list_head_commit(owner,repo,commit_sha):\n+#     url = base_url + "repos/" + owner + "/" + repo + "/commits" + "/" + commit_sha + "/branches-where-head"\n+#     print(url)\n+#     req = requests.get(url, auth=(token,\'\'))\n+#     print(req)\n+#     return req.json()\n+# print(list_head_commit("amar1452001","TerraformAssignment1CEQ508","commit_sha"))\n+\n+\n+#Listing pull requests associated with a commit\n+\n+# def list_pull_commit(owner,repo,commit_sha):\n+#     url = base_url + "repos/" + owner + "/" + repo + "/commits" + "/" + commit_sha + "/pulls"\n+#     print(url)\n+#     req = requests.get(url, auth=(token,\'\'))\n+#     print(req)\n+#     return req.json()\n+# print(list_pull_commit("amar1452001","PythonAssignment1cloudeqAmar","ac8f8b3b34048407ef9e6f434af891165a11959a"))\n+\n+# A Git reference ( git ref ) is a file that contains a Git commit SHA-1 hash. When referring to a Git commit, you can use the Git reference, which is an easy-to-remember name, rather than the hash. The Git reference can be rewritten to point to a new commit.\n+\n+# Get a commit\n+\n+def get_commit(owner,repo,ref):\n+    url = base_url + "repos/" + owner + "/" + repo + "/commits" + "/" + ref\n+    print(url)\n+    req = requests.get(url, auth=(token,\'\'))\n+    print(req)\n+    return req.json()\n+print(get_commit("amar1452001","PythonAssignment1cloudeqAmar","ref"))'}, {'sha': 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391', 'filename': 'requests', 'status': 'added', 'additions': 0, 'deletions': 0, 'changes': 0, 'blob_url': 'https://github.com/amar1452001/PythonSprint2PracticeCEQ508/blob/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/requests', 'raw_url': 'https://github.com/amar1452001/PythonSprint2PracticeCEQ508/raw/9d5885a1dfa129ab443f945740ecf48b6a7d23b5/requests', 'contents_url': 'https://api.github.com/repos/amar1452001/PythonSprint2PracticeCEQ508/contents/requests?ref=9d5885a1dfa129ab443f945740ecf48b6a7d23b5'}]}
