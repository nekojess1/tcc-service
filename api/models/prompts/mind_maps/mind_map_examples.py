input_format = """
    {
      "subject": "{subject}",
      "language": "{response idiom}"
    }
    """
    
output_format = """
        {"nodes": [{ "id": "{node id}", "description": "{content}" }],
        "edges": [{ "from_node": "{origin id node}", "to_node": "{destiny id node}" }]}
      """
        
output_example = """
{
  "nodes": [
    { "id": "0", "description": "World War II" },
    { "id": "1", "description": "Causes of the War" },
    { "id": "2", "description": "Treaty of Versailles Economic Reparations Loss of Territories" },
    { "id": "3", "description": "Rise of Nazism and Fascism Germany: Adolf Hitler Italy: Benito Mussolini" },
    { "id": "4", "description": "Japanese Expansionism Invasion of Manchuria Sino-Japanese War" },
    { "id": "5", "description": "Failure of the League of Nations Inability to Maintain Peace" },
    { "id": "6", "description": "Policy of Appeasement Concessions to Hitler's Demands" },
    { "id": "7", "description": "Major Events" },
    { "id": "8", "description": "Start of the War (1939) Invasion of Poland by Germany" },
    { "id": "9", "description": "Important Battles and Campaigns Battle of France Battle of Britain Operation Barbarossa (Invasion of the Soviet Union) Attack on Pearl Harbor Battle of Stalingrad Normandy Landings (D-Day) Battle of Midway" },
    { "id": "10", "description": "Holocaust Concentration and Extermination Camps Genocide of Jews and Other Minorities" },
    { "id": "11", "description": "Alliances and Opposing Sides" },
    { "id": "12", "description": "Allies United States Soviet Union United Kingdom France" },
    { "id": "13", "description": "Axis Germany Italy Japan" },
    { "id": "14", "description": "Technology and Weapons" },
    { "id": "15", "description": "Nuclear Weapons Manhattan Project" },
    { "id": "16", "description": "Planes and Tanks Development of Combat Planes Evolution of Tanks" },
    { "id": "17", "description": "Communications and Cryptography Enigma Code Decryption Machines (Bletchley Park)" },
    { "id": "18", "description": "Consequences of the War" },
    { "id": "19", "description": "Human Losses and Destruction Civilian and Military Casualties Devastation of Cities" },
    { "id": "20", "description": "Nuremberg Trials Trial of War Crimes" },
    { "id": "21", "description": "Creation of the UN Aim to Promote World Peace" },
    { "id": "22", "description": "Cold War Division Between Capitalist (USA) and Socialist (USSR) Blocs" },
    { "id": "23", "description": "Geopolitical Reconfiguration Division of Germany New Borders in Europe and Asia" },
    { "id": "24", "description": "Important Figures" },
    { "id": "25", "description": "Allied Leaders Franklin D. Roosevelt (USA) Winston Churchill (United Kingdom) Joseph Stalin (USSR)" },
    { "id": "26", "description": "Axis Leaders Adolf Hitler (Germany) Benito Mussolini (Italy) Hirohito (Japan)" },
    { "id": "27", "description": "Other Relevant Figures Dwight D. Eisenhower (Supreme Allied Commander) Erwin Rommel (German Marshal) Anne Frank (Symbol of Holocaust Victims)" },
    { "id": "28", "description": "War Timeline" },
    { "id": "29", "description": "1939-1940: Beginning and Blitzkrieg" },
    { "id": "30", "description": "1941-1942: Axis Expansion and US Entry" },
    { "id": "31", "description": "1943: Allied Turnaround" },
    { "id": "32", "description": "1944: Allied Advance" },
    { "id": "33", "description": "1945: End of the War and Axis Surrender" }
  ],
  "edges": [
    { "from_node": "0", "to_node": "1" },
    { "from_node": "0", "to_node": "7" },
    { "from_node": "0", "to_node": "11" },
    { "from_node": "0", "to_node": "14" },
    { "from_node": "0", "to_node": "18" },
    { "from_node": "0", "to_node": "24" },
    { "from_node": "0", "to_node": "28" },
    { "from_node": "1", "to_node": "2" },
    { "from_node": "1", "to_node": "3" },
    { "from_node": "1", "to_node": "4" },
    { "from_node": "1", "to_node": "5" },
    { "from_node": "1", "to_node": "6" },
    { "from_node": "7", "to_node": "8" },
    { "from_node": "7", "to_node": "9" },
    { "from_node": "7", "to_node": "10" },
    { "from_node": "11", "to_node": "12" },
    { "from_node": "11", "to_node": "13" },
    { "from_node": "14", "to_node": "15" },
    { "from_node": "14", "to_node": "16" },
    { "from_node": "14", "to_node": "17" },
    { "from_node": "18", "to_node": "19" },
    { "from_node": "18", "to_node": "20" },
    { "from_node": "18", "to_node": "21" },
    { "from_node": "18", "to_node": "22" },
    { "from_node": "18", "to_node": "23" },
    { "from_node": "24", "to_node": "25" },
    { "from_node": "24", "to_node": "26" },
    { "from_node": "24", "to_node": "27" },
    { "from_node": "28", "to_node": "29" },
    { "from_node": "28", "to_node": "30" },
    { "from_node": "28", "to_node": "31" },
    { "from_node": "28", "to_node": "32" },
    { "from_node": "28", "to_node": "33" }
  ]
}
"""