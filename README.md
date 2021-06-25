# image-gallery
a small python script meant to display a random picture every set amount of seconds from a folder. in its very, VERY early stages.

makes use of mainly builtin libraries, with the exception of [pixcat](https://github.com/mirukana/pixcat). this means **YOU WILL NEED TO RUN THE KITTY TERMINAL ON LINUX.**

## how to use
./image-gallery \[DIRECTORY OF IMAGES - optional\]

## issues/TODO
- have to use stdscr.clear instead of stdscr.erase due to the screen not fully clearing on refresh.

 ![Why I can't use clear.](./img/okayuerror.png)

- maybe the ability to show pictures from more than one directory
- image isn't fully centered horizontally