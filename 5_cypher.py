import os

from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph

load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE")

graph = Neo4jGraph(
    url=URI,
    username=USERNAME,
    password=PASSWORD,
    database=DATABASE
)

# graph.query(
#     """
#     MATCH (n:Team)
#     WHERE n.id IN ["보안팀", "플랫폼팀"]
#     SET n.이름 = n.id
#     RETURN n;    
#     """
# )

# graph.query(
#     """
#     MATCH
#         (kim:Person	{id: "김민수"})
#         -[r:RESPONSIBLE_FOR]->
#         (pay:Project {id: "결제 시스템 리팩터링"})

#     SET	r.source = "문서A"

#     RETURN kim, r, pay;
#     """
# )

# graph.query(
#     """
#     MERGE (improve:Entity {id: "장애율 개선 프로젝트"})	

#     SET	improve.type = "Project", 
#         improve.이름 = "장애율 개선 프로젝트"
#     SET	improve:Project

#     RETURN	improve;
#     """
# )

# graph.query(
#     """
#     MATCH (refactor:Project	{id: "결제 시스템 리팩터링"})
#     MATCH (improve:Project {id: "장애율 개선 프로젝트"})
#     MERGE (refactor)-[ct:CONTRIBUTES_TO]->(improve)
#     RETURN refactor, improve, ct;
#     """
# )

# graph.query(
#     """
#     MATCH (improve:Project {id: "장애율 개선 프로젝트"})
#     MATCH (team:Team)
#     WHERE team.id IN ["보안팀",	"플랫폼팀"]
#     MERGE (team)-[:COLLABORATES_ON]->(improve)
#     """
# )

# graph.query(
#     """
#     MATCH (refactor:Project	{id: "결제 시스템 리팩터링"})
#     MATCH (team:Team)
#     WHERE team.id IN ["보안팀",	"플랫폼팀"]
#     MATCH (team)-[old]->(refactor)
#     DELETE old
#     """
# )

graph.query(
    """
    MATCH (m:Metric	{id: "장애율"})
    DETACH DELETE m
    """
)