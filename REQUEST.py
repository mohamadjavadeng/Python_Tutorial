import requests as re
print("hi")
# temp = float(input("Please enter temperature:"))
# hum = int(input("Please enter humidity:"))
# sw1State = input("Please enter sw1 state:")
# sw2State = input("Please enter sw2 state:")
# M0 = int(input("Please enter M0:"))
# M1 = int(input("Please enter M1:"))
# D0  = int(input("Please enter D0:"))
# Y0 = int(input("Please enter Y0:"))
# Y1 = int(input("Please enter Y1:"))
# print("bye")
# print(temp)
# print(hum)
# print(sw1State)
# print(sw2State)
# r1 = re.get(f"https://script.google.com/macros/s/AKfycbyS5vy-pJMOQsUsWmGbc2aROoSIYDuKHBFO8gD1f4cfP0Q5QUIcZ9ppKMtAhV8AXyux/exec?sts=write&srs=Success&temp={temp}&humd={hum}&swtc1={sw1State}&swtc2={sw2State}")
# r1 = re.get(f"https://script.google.com/macros/s/AKfycbzAoIICl2e86ovNTc6KfEihjEA0kEy0Sq5j4zvOaole0zXipHe_Oz-nu9ql_RDXuqXW/exec?sts=write&M0={M0}&M1={M1}&D0={D0}&Y0={Y0}&Y1={Y1}")
# print(r1.text)
# r2 = re.get(f"https://script.google.com/macros/s/AKfycbyS5vy-pJMOQsUsWmGbc2aROoSIYDuKHBFO8gD1f4cfP0Q5QUIcZ9ppKMtAhV8AXyux/exec?sts=read")
r2 = re.get(f"https://script.google.com/macros/s/AKfycbzAoIICl2e86ovNTc6KfEihjEA0kEy0Sq5j4zvOaole0zXipHe_Oz-nu9ql_RDXuqXW/exec?sts=read")
print(r2.text)
RD = list(r2.text.split(","))
for i in range(0, len(RD)):
        RD[i] = int(RD[i])
print(RD)
# r = re.get("https://
# script.googleusercontent.com/macros/echo?user_content_key=z-2-1WBZl_1ExrX5GaFl9BZBv2DxwKVLgS9R532RsBCLxH7plS-Z4bUVaykYxrh9OHTdpgoDPPXyEpPQa4OayOd4Ne1ZDMdgm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnANXW9HfosQqSm-z-_0sDlh9i37mPqMmWCKx562XQySukypEfcrmYgFEwm7ZIM9qrDgWtV-qlRo-hxEGeZgHHGFKXNIuFvjpuXhmlH4XOH3v&lib=M5cS59dzb6ew8CbVcmWke-lmvmH1sd9Lq")
# print(r.text)

#https://script.google.com/macros/s/AKfycbzAoIICl2e86ovNTc6KfEihjEA0kEy0Sq5j4zvOaole0zXipHe_Oz-nu9ql_RDXuqXW/exec