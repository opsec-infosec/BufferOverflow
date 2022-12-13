# Copyright (C) 2022  Dale Furneaux (opinfosec)
# Released under GNU GPL v2

NAME 	= server
SRCS	= ./server.c

CC		= gcc
LIB		= strip

CFLAGS	= -m32 -z execstack --static

${NAME}:
		${CC} ${CFLAGS} ${SRCS} -o ${NAME}
		${LIB} ${NAME}

all:	${NAME}

clean:
		rm ${NAME}

re:		clean all

.PHONY: all clean re
