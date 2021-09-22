### How does this work?

* The repo used for nicktgr15.github.io is a submodule in this project. When the static contents of the website 
are updated the submodule gets updated too.

### How to develop locally

* Clone the submodules by 
```
git submodule init 
git submodule update
```
* update the SITEURL in pelicanconf.py
* `make devserver`

### To publish
* Revert the SITEURL change in pelicanconf.py
* `make publish`
* After the new content has been generated under the output folder push changes to the submodule
  * `cd output`
  * `git add -A`
  * `git commit -m "blah""`
  * `git push origin HEAD:master`

^^ the same applies for the theme submodule

Then update the submodule versions in the main repo:
* `git add -A`
* `git commit -m "blah"`
* `git push`


Finally, push all other changes
