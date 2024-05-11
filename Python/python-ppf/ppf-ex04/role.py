user                = 1
admin               = 2
superadmin          = 4 
authorizationMask   = admin | superadmin
userRole = int(input("Enter role: "))
print("Allowed to access: ", (authorizationMask & userRole) != 0)


