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
    ws = cs.find_workspace("W1")
    project = ws.find_project("P4")
    job = project.find_job("J11")
    
    templates_selected = job.load_output("templates_selected", slots=["blob"])
    unique_mrc_paths = set(templates_selected["blob/path"])
    all_templates_blobs = {path: project.download_mrc(path)[1] for path in unique_mrc_paths}
    