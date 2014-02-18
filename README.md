# Open Github Wiki Article in Browser

A silly and simple attempt at a [Sublime Text](http://www.sublimetext.com/3) plugin to open a Github Wiki article in your browser.

## Usage

Use `command+shift+g` or invoke `Open Article on Github` in the Command Pallete to upload the current open file. 

## Settings

This is the dumb part: You'll have to set your username and repo in a settings file called OpenGithubWikiArticleInBrowser.sublime-settings.

```
{
    // github settings (ex: https://github.com/[USER]/[REPO])
    "github_user":"YOUR_USER_NAME",
    "github_repo":"YOUR_REPO_NAME"
}
```


## License

  Copyright (c) 2014 Anthony Hecht

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
