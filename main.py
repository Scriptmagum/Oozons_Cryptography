from Oozons import caesar,otp

myotp=otp()

message="salut a tous"
tmp=myotp.chiffre(message)

print(myotp.dechiffre(tmp))

