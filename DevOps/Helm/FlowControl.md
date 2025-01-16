# Flow control
https://helm.sh/docs/chart_template_guide/control_structures/

## whilespace control
https://pkg.go.dev/text/template#hdr-Text_and_spaces
- `{{- `: left whitespace will be chomped
- ` -}}`: right whitespace will be consumed
- Be careful! Newlines are whitespace!
