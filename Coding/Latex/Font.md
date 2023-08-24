# Font

## some `sans serif` font example
https://tex.stackexchange.com/questions/2095/what-is-the-simplest-way-to-typeset-an-entire-document-in-sans-serif
- Fira: a little dark
- Lato: looks good
- notomath: good as well

## install noto on ubuntu
```sh
sudo apt-get update
sudo apt-get install fonts-noto
```

## install `notomath.sty` to pdfTex
```sh
# user mode
tlmgr install <package>
# for sudo use the full path of tlmgr `which tlmgr`

#all users
which tlmgr
sudo /path/to/tlmgr install <package>
```
