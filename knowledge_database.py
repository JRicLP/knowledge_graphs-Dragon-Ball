from knowledge_graph import Knowledge_Graph

dbz_graph = Knowledge_Graph()

#Entidades - Personagens:
dbz_graph.add_entity("Goku", {"raca": "Sayajin","tecnica_principal": "Kamehameha"})
dbz_graph.add_entity("Vegeta", {"raca": "Sayajin","tecnica_principal": "Final Flash"})
dbz_graph.add_entity("Gohan", {"raca": "Híbrido Humano/Saiyajin","tecnica_principal": "Masenko"})
dbz_graph.add_entity("Piccolo", {"raca": "Namekuseijin","tecnica_principal": "Makankosappo"})
dbz_graph.add_entity("Kuririn", {"raca": "Humano","tecnica_principal": "Kienzan"})
dbz_graph.add_entity("Tenshinhan", {"raca": "Humano","tecnica_principal": "Kikoho"})
dbz_graph.add_entity("Freeza", {"raca": "Raça de Freeza","tecnica_principal": "Death Ball"})
dbz_graph.add_entity("Cell", {"raca": "Bio Android","tecnica_principal": "Solar Kamehameha"})
dbz_graph.add_entity("Majin Boo", {"raca": "Majin","tecnica_principal": "Chocolate Beam"})
dbz_graph.add_entity("Future Trunks", {"raca": "Sayajin","tecnica_principal": "Burning Attack"})
dbz_graph.add_entity("Goten", {"raca": "Sayajin","tecnica_principal": "Kamehameha"})
dbz_graph.add_entity("Gotenks", {"raca": "Sayajin","tecnica_principal": "Super Ghost Kamikaze Attack"})
dbz_graph.add_entity("Vegito", {"raca": "Sayajin","tecnica_principal": "Kamehameha"})
dbz_graph.add_entity("Ginyu", {"raca": "Alienigena","tecnica_principal": "Body Change"})
dbz_graph.add_entity("Recoome", {"raca": "Alienigena","tecnica_principal": "Recoome Eraser Gun"})
dbz_graph.add_entity("Jeice", {"raca": "Alienigena da Constelação de Tuffle","tecnica_principal": "Crusher Ball"})
dbz_graph.add_entity("Burter", {"raca": "Alienigena","tecnica_principal": "Purple Comet Attack"})
dbz_graph.add_entity("Zarbon", {"raca": "Alienigena","tecnica_principal": "Transformação Monstruosa"})
dbz_graph.add_entity("Dodoria", {"raca": "Alienigena","tecnica_principal": "Explosões de Ki"})
dbz_graph.add_entity("Dabura", {"raca": "Demonio","tecnica_principal": "Cuspe de Pedra"})

#Entidades - Planetas:

dbz_graph.add_entity("Planeta Terra", {"localizacao": "Universo 7"})
dbz_graph.add_entity("Planeta Vegeta", {"localizacao": "Universo 7"})
dbz_graph.add_entity("Planeta Namekusei", {"localizacao": "Universo 7"})
dbz_graph.add_entity("Planeta Freeza n.79", {"localizacao": "Universo 7"})
dbz_graph.add_entity("Planeta do Sr.Kaio", {"localizacao": "Universo 7"})

#Entidades - Transformações: 

#Saiyajins e hibridos:
dbz_graph.add_entity("Super Saiyajin", {"tipo": "Transformacao", "raca": "Saiyajin ou híbrido"})
dbz_graph.add_entity("Super Saiyajin 2", {"tipo": "Transformacao", "raca": "Saiyajin ou híbrido"})
dbz_graph.add_entity("Super Saiyajin 3", {"tipo": "Transformacao", "raca": "Saiyajin ou híbrido"})
dbz_graph.add_entity("Super Vegeta", {"tipo": "Transformacao", "raca": "Saiyajin"})
dbz_graph.add_entity("Ultimate Gohan", {"tipo": "Transformacao", "raca": "Híbrido Saiyajin"})
dbz_graph.add_entity("Super Saiyajin Rage", {"tipo": "Transformacao", "raca": "Híbrido Saiyajin"})
dbz_graph.add_entity("Super Vegito", {"tipo": "Transformacao", "raca": "Fusao Saiyajin"})
dbz_graph.add_entity("Super Saiyajin Gotenks", {"tipo": "Transformacao", "raca": "Fusao híbrida"})
dbz_graph.add_entity("Super Saiyajin 3 Gotenks", {"tipo": "Transformacao", "raca": "Fusao híbrida"})

#Namekuseijin:
dbz_graph.add_entity("Piccolo Fundido com Nail", {"tipo": "Fusao", "raca": "Namekuseijin"})
dbz_graph.add_entity("Piccolo Fundido com Kami", {"tipo": "Fusao", "raca": "Namekuseijin"})

#Freeza:
dbz_graph.add_entity("Freeza 1ª Forma", {"tipo": "Transformacao", "raca": "Raca de Freeza"})
dbz_graph.add_entity("Freeza 2ª Forma", {"tipo": "Transformacao", "raca": "Raca de Freeza"})
dbz_graph.add_entity("Freeza 3ª Forma", {"tipo": "Transformacao", "raca": "Raca de Freeza"})
dbz_graph.add_entity("Freeza Forma Final", {"tipo": "Transformacao", "raca": "Raca de Freeza"})
dbz_graph.add_entity("Freeza 100% Poder", {"tipo": "Transformacao", "raca": "Raca de Freeza"})

#Cell:
dbz_graph.add_entity("Cell Imperfeito", {"tipo": "Transformacao", "raca": "Bio-androide"})
dbz_graph.add_entity("Cell Semi-Perfeito", {"tipo": "Transformacao", "raca": "Bio-androide"})
dbz_graph.add_entity("Cell Perfeito", {"tipo": "Transformacao", "raca": "Bio-androide"})
dbz_graph.add_entity("Cell Super Perfeito", {"tipo": "Transformacao", "raca": "Bio-androide"})

#Majin Boo:
dbz_graph.add_entity("Fat Buu", {"tipo": "Transformacao", "raca": "Majin"})
dbz_graph.add_entity("Evil Buu", {"tipo": "Transformacao", "raca": "Majin"})
dbz_graph.add_entity("Super Buu", {"tipo": "Transformacao", "raca": "Majin"})
dbz_graph.add_entity("Super Buu (Gotenks Absorvido)", {"tipo": "Transformacao", "raca": "Majin"})
dbz_graph.add_entity("Super Buu (Gohan Absorvido)", {"tipo": "Transformacao", "raca": "Majin"})
dbz_graph.add_entity("Kid Buu", {"tipo": "Transformacao", "raca": "Majin"})

#Zarbon:
dbz_graph.add_entity("Zarbon Forma Monstruosa", {"tipo": "Transformacao", "raca": "Alienigena"})

#Relacionamentos entre as Entidades:

#Relacionamentos entre Personagens e Planetas:

dbz_graph.add_relationship("Goku", "Planeta Terra", "vive_em")
dbz_graph.add_relationship("Gohan", "Planeta Terra", "vive_em")
dbz_graph.add_relationship("Piccolo", "Planeta Terra", "vive_em")
dbz_graph.add_relationship("Kuririn", "Planeta Terra", "vive_em")
dbz_graph.add_relationship("Tenshinhan", "Planeta Terra", "vive_em")
dbz_graph.add_relationship("Future Trunks", "Planeta Terra", "visita_em")
dbz_graph.add_relationship("Goten", "Planeta Terra", "vive_em")
dbz_graph.add_relationship("Gotenks", "Planeta Terra", "atua_em")
dbz_graph.add_relationship("Vegito", "Planeta Terra", "atua_em")
dbz_graph.add_relationship("Dabura", "Planeta Terra", "invade_em")
dbz_graph.add_relationship("Goku", "Planeta Vegeta", "origem_racial")
dbz_graph.add_relationship("Vegeta", "Planeta Vegeta", "origem_racial")
dbz_graph.add_relationship("Future Trunks", "Planeta Vegeta", "origem_racial")
dbz_graph.add_relationship("Goten", "Planeta Vegeta", "origem_racial")
dbz_graph.add_relationship("Gotenks", "Planeta Vegeta", "origem_racial")
dbz_graph.add_relationship("Vegito", "Planeta Vegeta", "origem_racial")
dbz_graph.add_relationship("Piccolo", "Planeta Namekusei", "origem_racial")
dbz_graph.add_relationship("Freeza", "Planeta Freeza n.79", "comanda")
dbz_graph.add_relationship("Zarbon", "Planeta Freeza n.79", "atua_em")
dbz_graph.add_relationship("Dodoria", "Planeta Freeza n.79", "atua_em")
dbz_graph.add_relationship("Goku", "Planeta do Sr.Kaio", "treinou_em")
dbz_graph.add_relationship("Gohan", "Planeta do Sr.Kaio", "visitou")
dbz_graph.add_relationship("Piccolo", "Planeta do Sr.Kaio", "visitou")

#Relacionamentos de Fusão:

dbz_graph.add_relationship("Gotenks", "Goten", "fusao_de")
dbz_graph.add_relationship("Gotenks", "Future Trunks", "fusao_de")
dbz_graph.add_relationship("Vegito", "Goku", "fusao_de")
dbz_graph.add_relationship("Vegito", "Vegeta", "fusao_de")
dbz_graph.add_relationship("Piccolo Fundido com Nail", "Piccolo", "forma_de")
dbz_graph.add_relationship("Piccolo Fundido com Nail", "Planeta Namekusei", "origem_poder")
dbz_graph.add_relationship("Piccolo Fundido com Kami", "Piccolo", "forma_de")

#Relacionamentos entre Personagens:

dbz_graph.add_relationship("Goku", "Vegeta", "aliado_de")
dbz_graph.add_relationship("Goku", "Gohan", "pai_de")
dbz_graph.add_relationship("Goku", "Goten", "pai_de")
dbz_graph.add_relationship("Vegeta", "Future Trunks", "pai_de")
dbz_graph.add_relationship("Goku", "Kuririn", "amigo_de")
dbz_graph.add_relationship("Goku", "Piccolo", "aliado_de")
dbz_graph.add_relationship("Piccolo", "Gohan", "mentor_de")
dbz_graph.add_relationship("Freeza", "Zarbon", "comandante_de")
dbz_graph.add_relationship("Freeza", "Dodoria", "comandante_de")
dbz_graph.add_relationship("Freeza", "Ginyu", "comandante_de")
dbz_graph.add_relationship("Ginyu", "Recoome", "comandante_de")
dbz_graph.add_relationship("Ginyu", "Jeice", "comandante_de")
dbz_graph.add_relationship("Ginyu", "Burter", "comandante_de")

#Relacionamentos de Inimizade/Conflito:

dbz_graph.add_relationship("Goku", "Freeza", "inimigo_de")
dbz_graph.add_relationship("Vegeta", "Freeza", "inimigo_de")
dbz_graph.add_relationship("Goku", "Cell", "inimigo_de")
dbz_graph.add_relationship("Gohan", "Cell", "inimigo_de")
dbz_graph.add_relationship("Goku", "Majin Boo", "inimigo_de")
dbz_graph.add_relationship("Vegeta", "Majin Boo", "inimigo_de")
dbz_graph.add_relationship("Goku", "Dabura", "inimigo_de")
dbz_graph.add_relationship("Gohan", "Dabura", "inimigo_de")
dbz_graph.add_relationship("Future Trunks", "Freeza", "inimigo_de")
dbz_graph.add_relationship("Future Trunks", "Cell", "inimigo_de")

#Relacionamentos Personagem -> Transformações:

#Sayajins:
dbz_graph.add_relationship("Goku", "Super Saiyajin", "possui_transformacao")
dbz_graph.add_relationship("Goku", "Super Saiyajin 2", "possui_transformacao")
dbz_graph.add_relationship("Goku", "Super Saiyajin 3", "possui_transformacao")
dbz_graph.add_relationship("Vegeta", "Super Saiyajin", "possui_transformacao")
dbz_graph.add_relationship("Vegeta", "Super Vegeta", "possui_transformacao")
dbz_graph.add_relationship("Gohan", "Super Saiyajin", "possui_transformacao")
dbz_graph.add_relationship("Gohan", "Super Saiyajin 2", "possui_transformacao")
dbz_graph.add_relationship("Gohan", "Ultimate Gohan", "possui_transformacao")
dbz_graph.add_relationship("Future Trunks", "Super Saiyajin", "possui_transformacao")
dbz_graph.add_relationship("Future Trunks", "Super Saiyajin Rage", "possui_transformacao")
dbz_graph.add_relationship("Goten", "Super Saiyajin", "possui_transformacao")
dbz_graph.add_relationship("Gotenks", "Super Saiyajin Gotenks", "possui_transformacao")
dbz_graph.add_relationship("Gotenks", "Super Saiyajin 3 Gotenks", "possui_transformacao")
dbz_graph.add_relationship("Vegito", "Super Vegito", "possui_transformacao")

#Namekuseijin:
dbz_graph.add_relationship("Piccolo", "Piccolo Fundido com Nail", "possui_forma")
dbz_graph.add_relationship("Piccolo", "Piccolo Fundido com Kami", "possui_forma")

#Raça de Freeza:
dbz_graph.add_relationship("Freeza", "Freeza 1ª Forma", "possui_forma")
dbz_graph.add_relationship("Freeza", "Freeza 2ª Forma", "possui_forma")
dbz_graph.add_relationship("Freeza", "Freeza 3ª Forma", "possui_forma")
dbz_graph.add_relationship("Freeza", "Freeza Forma Final", "possui_forma")
dbz_graph.add_relationship("Freeza", "Freeza 100% Poder", "possui_forma")

#Bio-Android
dbz_graph.add_relationship("Cell", "Cell Imperfeito", "possui_forma")
dbz_graph.add_relationship("Cell", "Cell Semi-Perfeito", "possui_forma")
dbz_graph.add_relationship("Cell", "Cell Perfeito", "possui_forma")
dbz_graph.add_relationship("Cell", "Cell Super Perfeito", "possui_forma")

#Majin:
dbz_graph.add_relationship("Majin Boo", "Fat Buu", "possui_forma")
dbz_graph.add_relationship("Majin Boo", "Evil Buu", "possui_forma")
dbz_graph.add_relationship("Majin Boo", "Super Buu", "possui_forma")
dbz_graph.add_relationship("Majin Boo", "Super Buu (Gotenks Absorvido)", "possui_forma")
dbz_graph.add_relationship("Majin Boo", "Super Buu (Gohan Absorvido)", "possui_forma")
dbz_graph.add_relationship("Majin Boo", "Kid Buu", "possui_forma")

#Alienígena
dbz_graph.add_relationship("Zarbon", "Zarbon Forma Monstruosa", "possui_forma")
