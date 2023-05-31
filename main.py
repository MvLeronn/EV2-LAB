from database import Database
from TeacherCRUD import TeacherCRUD

# Exercicio 1 - respostas:
# a) MATCH (u:Usuario{nome:'Bob'})-[:AMIGO]-(t:Usuario) RETURN t.nome   (Charlie e Alice)
# b) MATCH (u:Usuario)-[:POSTOU]->(p2) RETURN u.nome        (BOB)
# c) MATCH (u:Usuario)-[POSTOU]->() WHERE u.idade > 35 RETURN u.nome     (Ninguem)

# Exercicio 2 - respostas:
# a) MATCH(u:Usuario) return MAX(u.idade)
# b) MATCH(u:Usuario) WHERE u.idade > 30 return COUNT(u.idade)
# c) MATCH(u:Usuario) return AVG(u.idade)

teacher = TeacherCRUD()

# Exercicio 3:
teacher.create("Chris Lima", 1956, "189.052.396-66")
print(teacher.read("Chris Lima"))
teacher.update("Chris Lima", "162.052.777-77")
