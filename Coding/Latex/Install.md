# Install

## ubuntu install latest tex live
https://fahim-sikder.github.io/post/installing-texlive-latest-ubuntu/

```sh
sudo apt install wget perl-tk

wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar -xzf install-tl-unx.tar.gz
cd install-tl-****
sudo ./install-tl --scheme=medium --no-interaction --no-doc-install --no-src-install

export PATH=/usr/local/texlive/2023/bin/x86_64-linux${PATH:+:${PATH}}

# as doc is not installed, these two do not exist
export MANPATH=/usr/local/texlive/2023/texmf-dist/doc/man${MANPATH:+:${MANPATH}}
export INFOPATH=/usr/local/texlive/2023/texmf-dist/doc/info${INFOPATH:+:${INFOPATH}}
```

make sure that Ubuntu thinks we have installed texlive
```sh
sudo apt install equivs --no-install-recommends freeglut3
wget -O debian-equivs-2022-ex.txt https://www.tug.org/texlive/files/debian-equivs-2022-ex.txt

equivs-build debian-equivs-2022-ex.txt
sudo dpkg -i texlive-local_2022.99999999-1_all.deb
sudo apt install -f
```
