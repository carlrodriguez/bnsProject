NAME=paper
LATEX=pdflatex -interaction=nonstopmode

COMPUTEDFIGURES = $(patsubst %.gp,%.pdf,$(wildcard Figures/*.gp))
# SKETCHES = $(patsubst %.fig,%.pdf,$(wildcard Figures/*.fig))
#PREDRAWNFIGURES = $(filter-out $(COMPUTEDFIGURES) $(SKETCHES),$(wildcard Figures/*.pdf))
FIGURES=$(COMPUTEDFIGURES) 
#COLORONLYFIGURES=$(PREDRAWNFIGURES)
#IMAGES=$(wildcard Figures/*.png)
INPUTFILESFORFIGURES = $(filter-out %.pdf %.eps %.png,$(wildcard Figures/*.gp),$(wildcard Figures/Case*/*.asc),$(wildcard Figures/Case*/beta*/*.asc))
#INPUTFILESFORMISSINGBWFIGURES = $(filter-out $(wildcard Figures-bw/*), $(patsubst Figures,../Figures,$(wildcard Figures/Case*)), $(patsubst Figures,../Figures,$(wildcard Figures/*.gp)))
INPUTFILESFORMISSINGBWFIGURES = $(filter-out $(wildcard figures-bw/*), $(patsubst figures/%,figures-bw/%,$(INPUTFILESFORFIGURES)))

# pdf compression qualities (http://electron.mit.edu/~gsteele/pdf/, http://pages.cs.wisc.edu/~ghost/doc/cvs/Ps2pdf.htm#note_7)
EBOOK = << /ColorACSImageDict << /QFactor 0.76 /Blend 1 /ColorTransform 1 /HSamples [2 1 1 2] /VSamples [2 1 1 2] >> >> setdistillerparams
PRINTER = << /ColorACSImageDict << /QFactor 0.4 /Blend 1 /ColorTransform 1 /HSamples [1 1 1 1] /VSamples [1 1 1 1] >> >> setdistillerparams
PREPRINT = << /ColorACSImageDict << /QFactor 0.15 /Blend 1 /ColorTransform 1 /HSamples [1 1 1 1] /VSamples [1 1 1 1] >> >> setdistillerparams
LOSSLESS = << /AutoFilterColorImages false /ColorImageFilter /FlateEncode >> setdistillerparams
CUSTOM = << /AutoFilterGrayImages false /GrayImageFilter /FlateEncode >> setdistillerparams $(LOSSLESS)

.PHONY: clean 

$(NAME).pdf: $(NAME).tex refs.bib $(FIGURES)
	$(LATEX) $(NAME) || true
	bibtex $(NAME)
	$(LATEX) $(NAME) || true 
	bibtex $(NAME)
	$(LATEX) $(NAME) || true 
	$(LATEX) $(NAME) || true 

# create plots from gp files
Figures/%.pdf: Figures/%.gp 
	( cd $(shell dirname $<) && gnuplot-eps -d -s -t2.0 -p $(shell basename $<) )

Figures/%.eps: Figures/%.gp
	( cd $(shell dirname $<) && gnuplot-eps -d -s -t2.0 $(shell basename $<) )

Figures-bw/%.pdf: Figures/%.gp
	( cd $(shell dirname $@) && gnuplot-eps -m -d -s -t2.0 -p $(shell basename $<) )

Figures-bw/%.eps: Figures/%.gp
	( cd $(shell dirname $@) && gnuplot-eps -m -d -s -t2.0 $(shell basename $<) )

# create sketches from fig files
Figures/%.pdf: Figures/%.fig
	fig2dev -L eps $< | epstopdf --filter >$@

Figures/%.eps: Figures/%.fig
	fig2dev -L eps $< >$@

Figures-bw/%.pdf: Figures/%.fig
	fig2dev -L eps $< | epstopdf --filter >$@

Figures-bw/%.eps: Figures/%.fig
	fig2dev -L eps $< >$@

# convert bitmaps to eps
%.eps: %.png
	convert $< -resize 37% -dither $(DITHER) -colors 256 eps2:- | \
	sed '/%%EndComments/a \systemdict /setdistillerparams known {$(LOSSLESS)} if' >$@

# convert pdf only files to eps
%.eps: %.pdf
	pdftops -eps $< $@

allfigures: $(FIGURES)
allfigures: $(patsubst %.pdf,%.eps,$(FIGURES))
allfigures: $(patsubst Figures/%,Figures-bw/%,$(FIGURES))
allfigures: $(patsubst %.pdf,%.eps,$(patsubst Figures/%,Figures-bw/%,$(filter-out $(COLORONLYFIGURES),$(FIGURES))))
#allfigures: $(patsubst %.png,%.eps,$(patsubst Figures/%,Figures-bw/%,$(filter-out $(COLORONLYFIGURES),$(IMAGES))))
########################

clean:
	rm -rf *~ *.gz *.bbl *.out *.aux *.dvi *.log *.lof *.lot *.toc *.blg *.idx *.tpt paper.pdf 
	rm -f Figures{,-bw}/visitlog.py Figures{,-bw}/*.session.gui Figures{,-bw}/*.aux Figures{,-bw}/*.dvi Figures{,-bw}/*.tex Figures{,-bw}/*.eps Figures{,-bw}/*.log
