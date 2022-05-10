# Latex

## create a makefile
```
touch makefile
chmod u+x makefile
gedit makefile
```

## makefile
- `$@` for the makefile target
- `$<` for the first prerequisite
- `$^` for names of all the prerequisites
- `$*` only for the `%` part
```
#create pdf: make simple.pdf from my_simple.tex
%.pdf : my%.tex
	rm -f my_pdf_name.pdf
	pdflatex $< -o my_$* 2>&1 | tee errors.err
	bibtex  $(basename $<) 2>&1 | tee errors.err
	pdflatex $< -o my_$* 2>&1 | tee errors.err
	pdflatex $< -o my_$* 2>&1 | tee errors.err
	cp my_$*.pdf my_pdf_name.pdf
#clean
	rm -f *.o errors.err
	rm -f *.aux *.bbl *.blg *.log *.out
	rm -f *.synctex.gz
	rm -f BUILD
	@echo
```
