SRC=$(wildcard *.c)

INCLUDE=$(wildcard *.h)

CFLAGS=-Wall -Wextra -std=c99

LDFLAGS=-lm

OBJ=$(SRC:.c=.o)

NAME=202invendus

PREPROCESSOR=$(SRC:.c=.i)

ASM=$(SRC:.c=.s)

all: $(NAME)

full: $(NAME) asm preprocessor

preprocessor:$(PREPROCESSOR)

%.i: %.c $(INCLUDE)
	gcc -E $(@:.i=.c) > $@

asm:$(ASM)

%.s: %.c $(INCLUDE)
	gcc -S $<

#linking project
$(NAME):$(OBJ)
	gcc -o $@ $^ $(LDFLAGS)

#object Generation
%.o: %.c $(INCLUDE)
	gcc -c $< $(CFLAGS)

clean:
	rm -f $(OBJ)
	@rm -f $(addsuffix .gch, $(INCLUDE))
	@rm -f $(ASM)
	@rm -f $(PREPROCESSOR)

fclean: clean
	rm -f $(NAME)

re: fclean all

backup: $(SRC) $(INCLUDE)
	tar -cf $(addsuffix .tar, $(NAME)) $^ Makefile

help:
	@echo -e make option:
	@echo -e all
	@echo -e file.c
	@echo -e file.s
	@echo -e file.i
	@echo -e file.o
	@echo -e file.h
	@echo -e preprocessor
	@echo -e asm
	@echo -e clean
	@echo -e fclean
	@echo -e cache
	@echo -e clean_cache
	@echo -e rebuild
	@echo -e backup

.PHONY: clean fclean help re
