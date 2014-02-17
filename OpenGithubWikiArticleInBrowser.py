import sublime, sublime_plugin
import re, subprocess, os, shlex

class OpenGithubWikiArticleInBrowserCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    settings = sublime.load_settings('OpenGithubWikiArticleInBrowser.sublime-settings')
    gh_user = settings.get("github_user")
    gh_repo = settings.get("github_repo")

    if gh_user and gh_repo:
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

    else:
      print('You need to create a settings file.')