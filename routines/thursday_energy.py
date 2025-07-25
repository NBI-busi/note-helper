from config import thursday as cfg
from common.ui_common import render_ui
from common.draw_cftc_graph import draw_cftc_graph

#show daily procedures at upper
def run():
    render_ui(
        title=cfg.title,
        steps=cfg.steps,
        buttons=cfg.buttons,
        futures_files=cfg.futures_files,
        options_files=cfg.options_files,
        draw_func=draw_cftc_graph
    )
