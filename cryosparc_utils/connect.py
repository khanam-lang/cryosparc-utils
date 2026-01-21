# %% CryoSPARC location -- Note: need at least vpn access to CofC

# Since I'm planning on sharing this, I'm not going to ship any email/pswd combo 



import os
from cryosparc.tools import CryoSPARC

def connect():
    try:
        return CryoSPARC(
            license=os.environ["CRYOSPARC_LICENSE"],
            host=os.environ.get("CRYOSPARC_HOST", "localhost"),
            base_port=int(os.environ.get("CRYOSPARC_BASE_PORT", 61000)),
            email=os.environ["CRYOSPARC_EMAIL"],
            password=os.environ["CRYOSPARC_PASSWORD"],
        )

    except KeyError as e:
        raise RuntimeError(
            f"Missing CryoSPARC environment variable: {e.args[0]}"
        )

cs = connect()
assert cs.test_connection()
