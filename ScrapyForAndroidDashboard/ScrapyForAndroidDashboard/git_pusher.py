# -*-coding:utf-8-*-
import ConfigParser
import os
# from gittle import Gittle, GittleAuth
import time

from git import Repo, Actor

cp = ConfigParser.SafeConfigParser()
cp.read('scrapy.cfg')

repo_path = cp.get("git_pusher", "git_repo")
post_file_dir = os.path.join(repo_path, cp.get("git_pusher", "post_dir"))
post_title = cp.get("git_pusher", "post_title")
local_time = time.localtime(time.time())
local_date_str = time.strftime("%Y-%m-%d", local_time)
local_time_str = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
post_name = "%s-%s.md" % (local_date_str, post_title)


def push():
    repo = Repo.init(repo_path, bare=False)
    print repo.untracked_files
    print repo.commit(cp.get("git_pusher", "repo_branch"))
    origin = repo.remotes.origin
    index = repo.index
    index.add([os.path.join(post_file_dir, post_name)])

    username = cp.get("git_pusher", "git_username")
    email = cp.get("git_pusher", "git_email")
    commit_msg = "commit %s" % post_name
    author = Actor(username, email)
    committer = Actor(username, email)
    commit_result = index.commit(commit_msg, author=author, committer=committer)
    print type(commit_result), commit_result.committed_date, commit_result.type
    origin.pull()
    origin.push()

# new_repo = repo.init(path/for/new/repo)
# repo_url = 'git@git.coding.net:kyson/ScrapyForAndroidDashboard.git'
#
# hexo_doc_dir = os.path.join(repo_path, "tech.hikyson.cn")
# hexo_post_dir = os.path.join(hexo_doc_dir, "source/_posts")
#
# key_file = open('/Users/kysonchao/.ssh/id_rsa')
# auth = GittleAuth(pkey=key_file)
# repo = Gittle(repo_path, origin_uri=repo_url, auth=auth)
# repo.stage('file.txt')
# repo.commit(name="KysonSpider", email="kysonchao@gmail.com", message="This is a commit")
# repo.push()
