from config import get_neo4j_config
from neo4j import GraphDatabase

config = get_neo4j_config()
driver = GraphDatabase.driver(config["uri"], auth=(config["username"], config["password"]))

# Example function to test connection
def test_connection():
    with driver.session(database=config["database"]) as session:
        result = session.run("RETURN 'Connection successful' AS message")
        print(result.single()["message"])

if __name__ == "__main__":
    test_connection()
