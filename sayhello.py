def sayhello (name, school = "CSNHS"):
    print("Hello, {} from {}."
    .format(name, school))


sayhello("Edd")
sayhello("Edd", "CSNHS")
sayhello(name="Edd", school="ADNU")
sayhello(school="GCG", name="Edd")

