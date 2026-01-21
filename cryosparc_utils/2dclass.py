# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 17:47:41 2026

@author: Aasim
"""

# %% Connecting to the csparc client


from cryosparc_utils.connect import connect
from cryosparc.dataset import to_pystrs
cs = connect()

assert cs.test_connection()

# %%  main logic

def export_high_res_2d(
    cs,
    project: str,
    workspace: str,
    job: str,
    outdir: str,
    pixel_size: float = 1.0,
    dpi: int = 300,
):
    # location and loading
    # how can i find and alter dpi so that i have some extra space?
    # all copypasted from tutorial
    # TODO: 
    #   remove hard coded parameters via typer + CLI wrapper script
    #   figure out dynamic dpi sizes wrt extraction box pix size
    ws = cs.find_workspace("W1")
    project = ws.find_project("P4")
    job = project.find_job("J11")
    
    templates_selected = job.load_output("templates_selected", slots=["blob"])
    unique_mrc_paths = set(templates_selected["blob/path"])
    all_templates_blobs = {path: project.download_mrc(path)[1] for path in unique_mrc_paths}
    %matplotlib inline

    from pathlib import Path

    import matplotlib.pyplot as plt

    N = templates_selected["blob/shape"][0][0]
    scale = 100 / templates_selected["blob/psize_A"][0]  # 100 Å in pixels
    fig, axes = plt.subplots(3, 5, figsize=(5, 3), dpi=400)
    plt.margins(x=0, y=0)

    for i, template in enumerate(templates_selected.rows()):
        path = template["blob/path"]
        index = template["blob/idx"]
        blob = all_templates_blobs[path][index]
        ax = axes[i // 5, i % 5]
        ax.axis("off")
        ax.imshow(blob, cmap="gray", origin="lower")
        if i % 5 > 0:
            continue

        # Plot scale bar
        ax.plot([N // 7, N // 7], [N / 2 + scale / 2, N / 2 - scale / 2], color="white")
        ax.text(
            N // 8,
            N / 2,
            "100 Å",
            rotation=90,
            horizontalalignment="right",
            verticalalignment="center",
            fontsize=6,
            color="white",
        )

    fig.tight_layout(pad=0, h_pad=0.4, w_pad=0.4)
    fig.savefig(Path.home() / "class2d.png", bbox_inches="tight", pad_inches=0)
    fig.savefig(Path.home() / "class2d.pdf", bbox_inches="tight", pad_inches=0)