build_wilson:
	docker build -t telegram-wilson . 

run_wilson:
	docker run -it -d --restart=always -e BOT_TOKEN=$(BOT_TOKEN_WILSON) --name  telegram-wilson telegram-wilson 
