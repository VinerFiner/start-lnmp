# coding=utf-8
import os


def handler(event, context):
    if not os.path.exists("/mnt/auto/project"):
        os.system(
            "wget https://www.zblogcn.com/program/zblogphp17/ -O /mnt/auto/Z-BlogPHP_1_7_3_3290_Finch.zip")
        os.system(
            "cd /mnt/auto && unzip Z-BlogPHP_1_7_3_3290_Finch.zip && mv Z-BlogPHP_1_7_3_3290_Finch project && rm Z-BlogPHP_1_7_3_3290_Finch.zip.zip && cd -")
    return "nas init"
