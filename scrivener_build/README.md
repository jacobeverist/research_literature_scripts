

# Sequence of Events
1) Changes from within **Scrivener** are compiled from within **Scrivener**
2) During Compile, **Scrivener** runs **Scrivomatic** which is a ruby script pasted into the Compile menu
3) Calls **pandocomatic** which reads the `pandocomatic.yaml` file for config options
4) Calls **pandoc** with the constructed arguments
5) Build the resulting latex file with **xelatex** and build the bibliography with **biber**

## Equivalent shell execution of Scrivomatic from within Scrivener
```shell
ruby scrivomatic.rb -i "research_title_v1.md" -l -v 2>&1 >>scrivomatic.log
```

## Equivalent shell execution of pandocomatic from within Scrivomatic script

```shell
pandocomatic --debug --config pandoc/pandocomatic.yaml --data-dir pandoc research_title_v1.md
```
## Equivalent shell execution of pandoc from pandocomatic

```shell
# generated pandoc command
pandoc	--bibliography=research_library.bib \
	--standalone \
	--verbose \
	--citeproc \
	--lua-filter=/Users/username/projects/paper-research-title_mmd/pandoc/filters/pagebreak.lua \
	--csl=/Users/username/projects/paper-research-title_mmd/pandoc/csl/frontiers.csl \
	--citation-abbreviations=/Users/username/projects/paper-research-title_mmd/pandoc/cite-abbr.json \
	--reference-links \
	--biblatex \
	--from=markdown+pipe_tables+raw_attribute \
	--to=latex \
	--filter=/Users/username/projects/paper-research-title_mmd/pandoc/filters/assimilateMetadata \
	--template=/Users/username/projects/paper-research-title_mmd/pandoc/templates/aerospace2.latex \
	--toc \
	--toc-depth=4 \
	--shift-heading-level-by=0 \
	--log=pandoc.log \
    -i research_title_v1.md \
    -o research_title_v1.tex
```

## Build a PDF from the generated LaTeX and bibliography

```shell
# -shell-escape option used to render minted code sections
xelatex -shell-escape research_title_v1.tex

# build bibliography
biber research_title_v1

xelatex -shell-escape research_title_v1.tex
xelatex -shell-escape research_title_v1.tex
```


