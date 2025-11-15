NAME=trading-bot

all:
	docker build --no-cache -t $(NAME) .
	docker run --rm -t $(NAME)

remove:
