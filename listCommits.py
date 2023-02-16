
# AMARJOT SINGH     CEQ508


# List commits

import requests

base_url="https://api.github.com/"
token="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"



def list_commit(owner,repo):
    url = base_url + "repos/" + owner + "/" + repo + "/commits"
    print(url)
    req = requests.get(url, auth=(token,''))
    print(req)
    return req.json()
print(list_commit("veenakaushik132000","Terraform_assignment"))


# https://api.github.com/repos/veenakaushik132000/Terraform_assignment/commits
# <Response [200]>
# [{'sha': '374c6220347f6e24a3964e071a39c91bb663ee0c', 'node_id': 'C_kwDOI5RiB9oAKDM3NGM2MjIwMzQ3ZjZlMjRhMzk2NGUwNzFhMzljOTFiYjY2M2VlMGM', 'commit': {'author': {'name': 'veenakaushik132000', 'email': '124338410+veenakaushik132000@users.noreply.github.com', 'date': '2023-02-03T11:18:44Z'}, 'committer': {'name': 'GitHub', 'email': 'noreply@github.com', 'date': '2023-02-03T11:18:44Z'}, 'message': 'Add files via upload', 'tree': {'sha': '67de196e0d8b729c09380115ca6bbd2612a4b8ec', 'url': 'https://api.github.com/repos/veenakaushik132000/Terraform_assignment/git/trees/67de196e0d8b729c09380115ca6bbd2612a4b8ec'}, 'url': 'https://api.github.com/repos/veenakaushik132000/Terraform_assignment/git/commits/374c6220347f6e24a3964e071a39c91bb663ee0c', 'comment_count': 0, 'verification': {'verified': True, 'reason': 'valid', 'signature': '-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJj3O2UCRBK7hj4Ov3rIwAAP/kIAGpvg2bVb627jXEmqKy6oj59\nHO3WmizqkWCC2C34CWvonc5KwsRvwP3NNarij8+hOEaYK9OugIYcFtfPQ6OpuVG6\nsFJ8noGK8TGnKavX28fdGnOycVflif5N/z4O43GBxf8iAhkvHs4KBCFpKnJCAjZm\nNxv+UPgqdVgrSuXT1YrkRAZ8GUXyC/bVu1SeLK1p+OLEObqsyLJGG8iTOdEeKFQs\nq6V8Pfvz7NNIx7cvZJBHePovA78Tf5D8EzjfR8OVwSp/c2wijIQrsxiGCZ4o2Pjs\nQsJ9W1+2zNZqGJqx0wt88SeVzpWPVzxXaPZHtapTmmqoGLCJCBo223Av06Anc4U=\n=4pQb\n-----END PGP SIGNATURE-----\n', 'payload': 'tree 67de196e0d8b729c09380115ca6bbd2612a4b8ec\nauthor veenakaushik132000 <124338410+veenakaushik132000@users.noreply.github.com> 1675423124 +0530\ncommitter GitHub <noreply@github.com> 1675423124 +0530\n\nAdd files via upload'}}, 'url': 'https://api.github.com/repos/veenakaushik132000/Terraform_assignment/commits/374c6220347f6e24a3964e071a39c91bb663ee0c', 'html_url': 'https://github.com/veenakaushik132000/Terraform_assignment/commit/374c6220347f6e24a3964e071a39c91bb663ee0c', 'comments_url': 'https://api.github.com/repos/veenakaushik132000/Terraform_assignment/commits/374c6220347f6e24a3964e071a39c91bb663ee0c/comments', 'author': {'login': 'veenakaushik132000', 'id': 124338410, 
# 'node_id': 'U_kgDOB2lA6g', 'avatar_url': 'https://avatars.githubusercontent.com/u/124338410?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/veenakaushik132000', 'html_url': 'https://github.com/veenakaushik132000', 'followers_url': 'https://api.github.com/users/veenakaushik132000/followers', 'following_url': 'https://api.github.com/users/veenakaushik132000/following{/other_user}', 'gists_url': 'https://api.github.com/users/veenakaushik132000/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/veenakaushik132000/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/veenakaushik132000/subscriptions', 'organizations_url': 'https://api.github.com/users/veenakaushik132000/orgs', 'repos_url': 'https://api.github.com/users/veenakaushik132000/repos', 'events_url': 'https://api.github.com/users/veenakaushik132000/events{/privacy}', 'received_events_url': 'https://api.github.com/users/veenakaushik132000/received_events', 'type': 'User', 'site_admin': False}, 'committer': {'login': 'web-flow', 'id': 19864447, 'node_id': 'MDQ6VXNlcjE5ODY0NDQ3', 'avatar_url': 'https://avatars.githubusercontent.com/u/19864447?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/web-flow', 'html_url': 'https://github.com/web-flow', 'followers_url': 'https://api.github.com/users/web-flow/followers', 'following_url': 'https://api.github.com/users/web-flow/following{/other_user}', 'gists_url': 'https://api.github.com/users/web-flow/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/web-flow/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/web-flow/subscriptions', 'organizations_url': 'https://api.github.com/users/web-flow/orgs', 'repos_url': 
# 'https://api.github.com/users/web-flow/repos', 'events_url': 'https://api.github.com/users/web-flow/events{/privacy}', 'received_events_url': 'https://api.github.com/users/web-flow/received_events', 'type': 'User', 'site_admin': False}, 'parents': []}]