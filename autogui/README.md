### Installation

```shell
sudo pacman -S xorg-xhost
xhost +SI:localuser:<username> # access to DISPLAY
xhost -                        # revoke access to DISPLAY

```
