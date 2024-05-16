# import requests as re
# import time
# while True:
#     r = re.get("https://script.googleusercontent.com/macros/echo?user_content_key=z-2-1WBZl_1ExrX5GaFl9BZBv2DxwKVLgS9R532RsBCLxH7plS-Z4bUVaykYxrh9OHTdpgoDPPXyEpPQa4OayOd4Ne1ZDMdgm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnANXW9HfosQqSm-z-_0sDlh9i37mPqMmWCKx562XQySukypEfcrmYgFEwm7ZIM9qrDgWtV-qlRo-hxEGeZgHHGFKXNIuFvjpuXhmlH4XOH3v&lib=M5cS59dzb6ew8CbVcmWke-lmvmH1sd9Lq")
#     print(r.text)
#     time.sleep(5)

import certifi

cert_path = certifi.where()
print(cert_path)