def main():
    #spacecraft = {"name": "Voyager 1", "distance": 163}
    spacecraft = {"name": "James Webb Space Telescope"}
    #spacecraft["distance"] = 0.01
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ======== REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")}
    
    ==========================
"""

main()

def main():
    #spacecraft = {"name": "Voyager 1", "distance": 163}
    spacecraft = {"name": "James Webb Space Telescope"}
    #spacecraft["distance"] = 0.01
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ======== REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")}
    Oribit: {spacecraft.get("orbit", "Unknown")}
    ==========================
"""

main()