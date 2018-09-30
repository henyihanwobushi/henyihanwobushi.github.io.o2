NOW=`date +'%Y-%m-%d %H:%M:%S'`

deploy:
	@git add .
	@git commit -m "update at $(NOW)"
	@git push origin master

new:
	@bundle exec jekyll draft "$(filter-out $@,$(MAKECMDGOALS))"

pub:
	@bundle exec jekyll publish "$(filter-out $@,$(MAKECMDGOALS))"

