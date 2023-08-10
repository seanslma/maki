# Code Block

## Python highlighting using `minted`
- `pip install Pygments`
- In Latex
  ```latex
  \usepackage{minted}
  #set code format
  \setminted[python]{breaklines, framesep=2mm, fontsize=\footnotesize, numbersep=5pt}
  # create a code block
  \begin{minted}{python}
  if true:
    print('Hello World!')
  \end{minted}
  ```
- Invoke the `shell-escape` flag to compile the document
