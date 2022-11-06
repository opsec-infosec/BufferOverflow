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
