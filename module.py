# %% CryoSPARC location -- Note: need at least vpn access to CofC

# Since I'm planning on sharing this, I'm not going to ship any email/pswd combo 



import os
from cryosparc.tools import CryoSPARC

cs = CryoSPARC(
    license="c5361228-3a35-11ef-86aa-cb0d66d4f604",
    host="hpc.cofc.edu",
    base_port=61000,
    email="test",
    password="test!"
)

# sanity check 
assert cs.test_connection()

# %% 