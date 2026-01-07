TEX := lecture_02_identification_arma_wold.tex
PDF := lecture_02_identification_arma_wold.pdf

LATEX := pdflatex -interaction=nonstopmode -halt-on-error

.PHONY: all pdf clean

all: pdf

pdf: $(TEX)
	$(LATEX) $(TEX)
	$(LATEX) $(TEX)

clean:
	rm -f $(PDF) \
		lecture_02_identification_arma_wold.aux \
		lecture_02_identification_arma_wold.log \
		lecture_02_identification_arma_wold.nav \
		lecture_02_identification_arma_wold.out \
		lecture_02_identification_arma_wold.snm \
		lecture_02_identification_arma_wold.toc \
		lecture_02_identification_arma_wold.fls \
		lecture_02_identification_arma_wold.fdb_latexmk \
		lecture_02_identification_arma_wold.synctex.gz

