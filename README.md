# gfm-preview

gfm-preview is just a good enough solution to rendering github flavored
markdown documents.


## Usage

	$ export GITHUB_USERNAME=xxx	# optional
	$ export GITHUB_TOKEN=xxx		# optional
	$ gfm-preview document.md

If username and token are not given, calls github API anonymously


## Caveats

* Depends on [GitHub Markdown Rendering API](http://developer.github.com/v3/markdown/).
* No Caching; API is called every time you open a preview.
* Only supports Mac OS X.

## Thanks

HTML template is borrowed from [ghmarkdownrender](https://github.com/magnetikonline/ghmarkdownrender).