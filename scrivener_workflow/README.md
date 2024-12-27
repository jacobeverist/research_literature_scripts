
Notes takes from the [compile.sh](compile.sh) file within each of the Scrivener directories in:
`/Users/username/projects/paper-research-title_mmd`

# Workflow Outline
- Changes from within [Scrivener] are compiled from within [Scrivener] using the Compile action
- [Scrivener] runs [Scrivomatic] which is a ruby script pasted into the Compile menu
- Calls [pandocomatic] which reads the [pandoc/pandocomatic.yaml](pandoc/pandocomatic.yaml) file for config options
- Calls [pandoc] with the constructed arguments
- Build the latex file with [xelatex] and build the bibliography with [biber]

# Tools

## Scrivener

- Go to menu `File->Compile`
- Select `Compile For:`  to be set to `MultiMarkdown`
- Select `Format` to be `Scrivomatic`
- If it exists, select `Add front matter` to compile option
- Click the `Compile` button
- Select save location
- Generates  `research_title_v1.md`


## Scrivomatic

Here is the command-line that replicates the way Scrivener calls  scrivomatic

```shell
ruby scrivomatic.rb -i "research_title_v1.md" -l -v 2>&1 >>scrivomatic.log
```

## Pandocomatic


Scrivener calls [pandocomatic] with the following command line.     

```shell
pandocomatic --debug --config pandoc/pandocomatic.yaml --data-dir pandoc research_title_v1.md
```


 You can rebuild by calling it from the command line, but only if you change the `research_title_v1.md` file that is generated

Changes from within Scrivener need to be compiled from Scrivener which are then generated into `research_title_v1.md`

All pandoc configuration and templates can be found in each paper's local pandoc directory:
`/Users/username/projects/paper-research-title_mmd/pandoc`


## Pandoc
Converts the generated markdown file into a latex file.
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

## XeLaTeX
```shell
# -shell-escape option used to render minted code sections
xelatex -shell-escape research_title_v1.tex
```

## Biber
```shell
# build bibliography
biber research_title_v1

```

## Recompile LaTeX with bibliography citations

```shell
# repeate calls after biber
xelatex -shell-escape research_title_v1.tex
xelatex -shell-escape research_title_v1.tex
```



