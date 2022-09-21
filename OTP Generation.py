#OTP generation and Verification
import random
OTP=random.randint(1000,9999)
print("An OTP has been sent to your mobile number.")
print(f"The OTP is : {OTP}")
number=int(input("Enter the 4-digit OTP sent to your mobile number: "))
if OTP==number:
    print("OTP verification Success")
else:
    print("OTP verification Unsuccessfull")
