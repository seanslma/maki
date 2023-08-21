# Code Block

## Python highlighting using `minted`
- `pip install Pygments`
- In Latex
  ```latex
  \usepackage{minted}
  % set code format
  \setminted[python]{breaklines, framesep=2mm, fontsize=\footnotesize, numbersep=5pt}
  % create a code block
  \begin{minted}{python}
  if true:
    print('Hello World!')
  \end{minted}
  ```
- Invoke the `shell-escape` flag to compile the document

## another example
```latex
\newminted{py}{
    breaklines,
    framesep=2mm,
    fontsize=\scriptsize,
    numbersep=5pt,
    linenos
}

% create a code block
\begin{pycode}
if true:
print('Hello World!')
\end{pycode}
```

## custom the space before and after the code block
after loading `minted`
```latex
\AtBeginEnvironment{minted}{\vspace{-8pt}}
\AfterEndEnvironment{minted}{\vspace{-6pt}}
```