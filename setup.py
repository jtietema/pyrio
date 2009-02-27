# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
from os.path import join

setup(
    windows = [{"script":"main.py"}],
    data_files =[
        (join('assets','images','enemies','krush'), ["flat_left_1.png","flat_left_2.png","flat_left_3.png","flat_left_4.png",                                       "walk_left_1.png", "walk_left_2.png","walk_left_3.png","walk_left_4.png", "pkg.cfg"]), 
        (join("assets","images","enemies","turtle"),["shell_front.png", "shell_move_1.png", "shell_move_2.png", "shell_move_3.png", "pkg.cfg", "walk_left_1.png", "walk_left_2.png", "walk_left_3.png"]),
        (join("assets","images","game"), ["gold_m.png", "live.png", "pkg.cfg"]), 
        (join("assets","images","goldpiece","yellow"), ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png", "10.png", "pkg.cfg"]),
        (join("assets","images","map"), ["door.png", "hill_left.png", "hill_left_up.png", "left.png", "left_up.png", "middle.png", "pipe_up.png", "pipe_ver.png", "pkg.cfg", "stone.png", "up.png"]), 
        (join("assets","images","menu"), ["start.png", "controls.png", "video.png", "quit.png", "pkg.cfg"]), 
        (join("assets","images","player"), ["fall_right.png", "jump_right.png", "stand_right.png", "walk_right_1.png", "walk_right_2.png", "pkg.cfg"]),
        (join("assets","music"), ["jungle_1.ogg", "land_2.ogg", "map_finished.ogg"]), 
        (join("assets","sounds"), ["coin.ogg", "dead.ogg", "jump.ogg", "pkg.cfg"]), 
        (join("assets","sounds","krush"), ["hit.ogg", "pkg.cfg"]), 
        (join("assets","sounds","turtle"), ["hit.ogg", "hit_shell.ogg", "pkg.cfg"]),
        (join("maps","testpak"), ["map1.map", "map2.map", "pkg.cfg"])]
    )