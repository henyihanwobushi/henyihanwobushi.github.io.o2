NOW=$(date +'%Y-%m-%d %H:%M:%S')

deploy:
	echo $(NOW)
	git add .
	git commit -m "update at "
	git push origin master