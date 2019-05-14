from git import Repo
import os
class GitHelper():

    def __init__(self,path):
        self.path=path

    def is_dir(self,url):
        print(self.path)
        path=os.path.join(self.path,".git")
        if not os.path.exists(path):  # 判断该路径是否存在
              Repo.clone_from(url,self.path)
