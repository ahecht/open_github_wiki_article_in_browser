import sublime, sublime_plugin
import re, subprocess, os, shlex

class OpenGithubWikiArticleInBrowserCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    settings = sublime.load_settings('OpenGithubWikiArticleInBrowser.sublime-settings')
    gh_user = settings.get("github_user")
    gh_repo = settings.get("github_repo")

    # self.getGitOrigin()

    full_file_path = self.view.file_name()
    pattern1 = r'^.*?'+re.escape(gh_repo)+r'\.wiki/'
    is_wiki_file = re.search(pattern1, full_file_path)
    
    if is_wiki_file:
      pattern1 = r'^.*'+re.escape(gh_repo)+r'\.wiki/'
      wiki_path = re.sub(pattern1, '', full_file_path)
      wiki_path = re.sub(r'\.md$','', wiki_path)
      github_path = 'https://github.com/'+gh_user+'/'+gh_repo+'/wiki/' + wiki_path
      subprocess.Popen(["open", github_path])
    
    else:
      print('Doesn\'t look like a wiki file. Expected it to be in a directory named \''+gh_repo+'.wiki\' (which itself can be anywhere).')

  # def getGitOrigin(self):
  #   my_file = self.view.file_name()
  #   file_dir = re.sub(r'\/[^/]*?$','',my_file)
  #   print(file_dir)
  #   # construct the command line git command
  #   raw_command = 'git remote show origin'
  #   args = shlex.split(raw_command)
  #   output = subprocess.Popen(args, cwd=r''+file_dir+'', stderr=subprocess.PIPE)
  #   print(output.communicate())
