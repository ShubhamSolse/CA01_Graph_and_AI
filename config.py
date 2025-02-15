# config.py

# Configuration for Neo4j connection
NEO4J_CONFIG = {
    "uri": "bolt://localhost:7687",  # Replace with your Neo4j instance URI
    "username": "neo4j",            # Replace with your Neo4j username
    "password": "9665131011",         # Replace with your Neo4j password
}

def get_neo4j_config():
    """
    Returns the Neo4j configuration settings.

    :return: Dictionary containing Neo4j connection details.
    """
    return NEO4J_CONFIG

# Example usage (for debugging, remove in production):
if __name__ == "__main__":
    config = get_neo4j_config()
    print("Neo4j Configuration:")
    for key, value in config.items():
        print(f"{key}: {value}")
