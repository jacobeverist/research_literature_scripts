
# 1) Scrivener runs Scrivomatic which is a ruby script pasted into the Compile menu
# 2) Calls pandocomatic which reads the pandocomatic.yaml file for config options
# 3) Calls pandoc with the constructed arguments
# 4) Build the latex file with xelatex and build the bibliography with biber

#ruby scrivomatic.rb -i "research_title_v1.md" -l -v 2>&1 >>scrivomatic.log

#exit


# Scrivener calls pandocomatic with the following command line.
# you can rebuild by calling it from the command line, but only if you change the BrainBlocks.md file
# changes from within Scrivener need to be compiled from the tool
pandocomatic --debug --config pandoc/pandocomatic.yaml --data-dir pandoc research_title_v1.md

# generated pandoc command
#pandoc	--bibliography=research_library.bib \
#	--standalone \
#	--verbose \
#	--citeproc \
#	--lua-filter=/Users/username/projects/paper-research-title_mmd/pandoc/filters/pagebreak.lua \
#	--csl=/Users/username/projects/paper-research-title_mmd/pandoc/csl/frontiers.csl \
#	--citation-abbreviations=/Users/username/projects/paper-research-title_mmd/pandoc/cite-abbr.json \
#	--reference-links \
#	--biblatex \
#	--from=markdown+pipe_tables+raw_attribute \
#	--to=latex \
#	--filter=/Users/username/projects/paper-research-title_mmd/pandoc/filters/assimilateMetadata \
#	--template=/Users/username/projects/paper-research-title_mmd/pandoc/templates/aerospace2.latex \
#	--toc \
#	--toc-depth=4 \
#	--shift-heading-level-by=0 \
#	--log=pandoc.log \
#    -i research_title_v1.md \
#    -o research_title_v1.tex

# -shell-escape option used to render minted code sections
xelatex -shell-escape research_title_v1.tex

# build bibliography
biber research_title_v1

xelatex -shell-escape research_title_v1.tex
xelatex -shell-escape research_title_v1.tex
