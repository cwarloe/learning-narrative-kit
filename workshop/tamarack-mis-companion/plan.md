# Plan: tamarack-mis-companion

Brief: `briefs/tamarack-mis-companion.brief.yaml` · generated 2026-10-12 · **approved** by the author

10 chapters · 264 terms · definitions: source 264, confirmed 0, proposed 0, missing 0 · 287 suggested dependencies

Most depended-on concepts (introduce them early and well): data (73), Information (55), computer (33), database (19), process (10), database management system (DBMS) (6), object (6), Business intelligence (BI) (5), server (4), decision support system (DSS) (4), data warehouse (3), Integrity (3)

## Story

- **Premise:** Dana Okafor's first year as Tamarack's business systems analyst: eleven stores, a DC and a propane division running on systems nobody chose on purpose.
- **Setting:** Tamarack Feed & Supply Company, Spokane Valley and the stores (examples/TAMARACK.md), January–October 2026
- **Cast:** From canon: Dana (POV), Ruth, Walt, Teo, Marcy, Hank, Eli. Recurring minor characters used so far but not in the canon cast table: Curtis (Colville), Karen (seed supplier AR), Arlo Nygaard (Republic), Jim Sorensen.
- **Through line:** Each fix Tamarack makes on purpose creates the next problem it didn't plan for. The inventory pilot needs reliable servers (ch02); the servers get exploited (ch05); the cleaned-up data feeds the decisions (ch08) and the AI (ch09); and by ch10 the question is no longer which system but where any of it should run, and what happens at Republic when the line goes down.

## Chapters

| # | Group | Status | Title | Terms | Builds on | Risks |
|---|---|---|---|---|---|---|
| ch01 | mis-01-information-systems | accepted | The Count That Didn't Match | 11 | 0 | 6 term(s) here depend on terms introduced later (see gaps.forward_references) |
| ch02 | mis-02-computers | accepted | The Server in the Feed Room | 29 | 2 | 3 term(s) here depend on terms introduced later (see gaps.forward_references) |
| ch03 | mis-03-data-bi | revise | One Customer, Four Records | 47 | 4 | catalog-chapter risk: 47 terms (max 30); plan two scenes with different stakes, or split; 1 term(s) here depend on terms introduced later (see gaps.forward_references) |
| ch04 | mis-04-ethics-legal | accepted | The Video From the Kettle Falls Lot | 18 | 3 |  |
| ch05 | mis-05-security | revise | The Invoice That Changed Its Bank | 49 | 6 | catalog-chapter risk: 49 terms (max 30); plan two scenes with different stakes, or split; 1 term(s) here depend on terms introduced later (see gaps.forward_references) |
| ch06 | mis-06-global | accepted | The Rep Who Couldn't Say Yes | 9 | 3 | 3 term(s) here depend on terms introduced later (see gaps.forward_references) |
| ch07 | mis-07-enterprise | accepted | Chick Days | 21 | 5 |  |
| ch08 | mis-08-decisions | accepted | Where the Twelfth Store Goes | 16 | 4 |  |
| ch09 | mis-09-ai | accepted | The Counter Assistant | 22 | 8 |  |
| ch10 | mis-10-emerging | accepted | The Closet Gets Too Hot | 42 | 5 | catalog-chapter risk: 42 terms (max 30); plan two scenes with different stakes, or split |

### ch01 · The Count That Didn't Match

- **Pov:** Dana
- **Goal:** make the register count match the pallet at Colville
- **Complication:** the system records transactions but nobody trusts its information; Curtis keeps a notebook
- **Decision:** a three-store inventory pilot instead of Walt's new software
- **Cost:** Curtis will believe the screen only after three months of matching
- **Carries forward:** the pilot needs servers that stay up (ch02)

### ch02 · The Server in the Feed Room

- **Pov:** Dana
- **Goal:** keep billing running on invoice day
- **Complication:** the billing server is failing and the tape backups have never been tested
- **Decision:** buy a NAS now; defer the billing rewrite
- **Cost:** the rewrite slips a year; the predecessor's alert addresses are everywhere
- **Carries forward:** the feed-room closet and its NAS (ch05, ch10)

### ch03 · One Customer, Four Records

- **Pov:** Dana
- **Goal:** one record per customer before the spring mailer
- **Complication:** the 2009 migration duplicated customers across models and stores
- **Decision:** a merchandising data mart now, the warehouse later
- **Cost:** the mailer goes out two weeks late, after fencing season starts
- **Carries forward:** the data mart (ch08, Excel 11); clean customer data (ch09)
- **Notes:** Revise, don't rewrite. Scenes 1-2 (Gordon's four records; Walt's whiteboard, including the author's Big data / Power BI paragraphs) stay. The last section ('Three other decisions got made during the trial, because the warehouse forced them') is a list: distributed DB, object-oriented DB, graph DB, encryption. Rework so each lands on a pressure: the web store's object database breaks the nightly ETL; Teo designs the distributed database for winter outages but it isn't funded (continuity: MIS 10 still needs edge servers in July); the graph-database pitch arrives after the Hollister merge mistake, when it would have prevented it.

### ch04 · The Video From the Kettle Falls Lot

- **Pov:** Dana
- **Goal:** answer a false video about the feed
- **Complication:** being right is not enough in public; a GDPR request arrives
- **Decision:** keep comments open, test the feed and post the results, print them for the stores
- **Cost:** about a third of ranch customers have slow or no home internet and never see the correction online (digital divide); the GDPR request stays open
- **Carries forward:** the digital divide and the open GDPR request (ch10)

### ch05 · The Invoice That Changed Its Bank

- **Pov:** Dana
- **Goal:** find out how $14,200 went to a fake account
- **Complication:** Hank's laptop was infected and the feed-room server was cryptojacked
- **Decision:** MFA tokens, a callback rule, a locked closet
- **Cost:** Hank hates the token every morning
- **Carries forward:** Hank will buy anything labeled security (ch10)
- **Notes:** Revise, don't rewrite. The phishing open, laptop forensics, and CIA memo stay. The pen-test findings (ten in a row) become the report the characters read, as a table artifact; the prose stays on the findings that change a decision (backdoor, cryptojacking, the Chewelah manager). PKI / symmetric / asymmetric / nonrepudiation was a Teo lecture: make it Hank's question (he was the victim), per schema/README.md rule 8.

### ch06 · The Rep Who Couldn't Say Yes

- **Pov:** Dana
- **Goal:** keep the fencing rep's discounts
- **Complication:** Prairie Wire's new owners route every price and order through Saskatoon
- **Decision:** work through the new approval chain; park the private-label idea
- **Cost:** the rep can no longer say yes on the phone
- **Carries forward:** the feed co-op folder (ch10 community cloud; ITM Week 7 buying group)

### ch07 · Chick Days

- **Pov:** Dana
- **Goal:** get 400 chicks to the right store
- **Complication:** four disconnected systems; the expert, Arlo, is retiring
- **Decision:** start an ERP selection with a twelve-month deadline
- **Cost:** nobody believes the deadline; Arlo's knowledge leaves with him
- **Carries forward:** the ERP vendors asking where it should run (ch10)

### ch08 · Where the Twelfth Store Goes

- **Pov:** Dana
- **Goal:** choose store twelve
- **Complication:** Walt's napkin says Sandpoint; the model says Davenport
- **Decision:** Davenport
- **Cost:** Walt's friend Jim Sorensen is told to wait a year
- **Carries forward:** Davenport (Excel 8–10)

### ch09 · The Counter Assistant

- **Pov:** Dana
- **Goal:** stop clerks giving wrong dosing answers
- **Complication:** an AI counter assistant is confident and sometimes wrong
- **Decision:** pilot it with human override
- **Cost:** correct overrides are logged as errors
- **Carries forward:** Counter Assistant lives in its own cloud (ch10 multicloud)

### ch10 · The Closet Gets Too Hot

- **Pov:** Dana
- **Goal:** recommend where Tamarack's systems should run, in two weeks, after the closet hits 97°F
- **Complication:** the ERP vendor sells only software as a service, and Republic's line fails every winter; at the expo a Republic ranch wants its feed recorded on the cattle association's blockchain, which records transactions from connected devices
- **Decision:** a hybrid: SaaS ERP in a public cloud, an edge server in each store, backup as a service; Walt does not sign with the association until the Republic edge server has been through a winter
- **Cost:** Tamarack rents its core system every month from now on; the Republic ranch moves its show-cattle feed to a dealer in Omak that signed
- **Carries forward:** the October Republic outage and eleven-hour sync; Walt's open question on the cattle association (revisit after a winter); membership in the dealers' community cloud. Author to decide: is that membership how the ITM Week 7 buying group first met?
- **Notes:** Published 2026-10-12 from the candidate (reviews r0-r4). Two scenes: the hosting decision, and Walt at the expo.

## Gaps and decisions for the author

- **Needs a definition:** none
- **Proposed definitions awaiting approval:** none
- **Conflicting definitions:** Software as a Service (software_as_a_service, software_as_a_service_saas)
- **Same definition, different terms:** on_demand_software, software_as_a_service
- **Forward references** (a term's definition relies on a term introduced later): 14
  - computer_literacy (ch01) needs computer (introduced in ch02)
  - computer_literacy (ch01) needs database (introduced in ch03)
  - information_literacy (ch01) needs business_intelligence_bi (introduced in ch03)
  - information_technologies (ch01) needs computer (introduced in ch02)
  - information_technologies (ch01) needs database (introduced in ch03)
  - information_technologies (ch01) needs radio_frequency_identification_rfid (introduced in ch07)
  - fifth_generation_languages_5gls (ch02) needs artificial_intelligence_ai (introduced in ch09)
  - fifth_generation_languages_5gls (ch02) needs natural_language_processing_nlp (introduced in ch09)
  - object_oriented_programming_oop (ch02) needs object (introduced in ch03)
  - data_model (ch03) needs integrity (introduced in ch05)
  - cryptojacking (ch05) needs cryptocurrency (introduced in ch10)
  - global_information_system_gis (ch06) needs geographic_information_system_gis (introduced in ch08)
  - global_supply_chain_management (ch06) needs supply_chain (introduced in ch07)
  - global_supply_chain_management (ch06) needs supply_chain_management_scm (introduced in ch07)
- **Introduced once, never revisited or built on:** 195 of 264 terms (not a defect by itself; a list to draw on when planning callbacks)

## Term map

| Term | Introduced | Depends on | Revisited in |
|---|---|---|---|
| Computer literacy | ch01 | computer, database |  |
| data | ch01 | information |  |
| Five Forces Model | ch01 | information |  |
| Information | ch01 | process | ch02, ch03, ch04, ch05, ch06, ch08, ch09 |
| Information literacy | ch01 | information, business_intelligence_bi |  |
| information technologies | ch01 | information, computer, database, radio_frequency_identification_rfid |  |
| management information system (MIS) | ch01 | data, information | ch02, ch03, ch04, ch05, ch06, ch07, ch08, ch09, ch10 |
| process | ch01 | information | ch03, ch04, ch05, ch06, ch07, ch08 |
| Strategic information systems (SISs) | ch01 | information |  |
| transaction-processing systems (TPSs) | ch01 | data |  |
| virtual organizations | ch01 | information |  |
| application software | ch02 | computer |  |
| arithmetic logic unit (ALU) | ch02 |  |  |
| Assembly language | ch02 | data, computer, machine_language |  |
| bus | ch02 | computer |  |
| cache RAM | ch02 | random_access_memory_ram |  |
| central processing unit (CPU) | ch02 | arithmetic_logic_unit_alu, computer, control_unit | ch05 |
| computer | ch02 | data, information | ch04, ch05, ch07, ch10 |
| control unit | ch02 | computer |  |
| CPU case | ch02 | central_processing_unit_cpu, computer |  |
| disk drive | ch02 | information |  |
| Fifth-generation languages (5GLs) | ch02 | computer, artificial_intelligence_ai, natural_language_processing_nlp |  |
| Fourth-generation languages (4GLs) | ch02 | computer |  |
| high-level languages | ch02 | computer |  |
| Input devices | ch02 | data, information, computer |  |
| machine language | ch02 | data, computer |  |
| magnetic disk | ch02 | data |  |
| Magnetic tape | ch02 | data |  |
| Main memory | ch02 | data, information, computer |  |
| motherboard | ch02 | central_processing_unit_cpu, disk_drive |  |
| Network-attached storage (NAS) | ch02 | data, computer | ch05, ch09, ch10 |
| object-oriented programming (OOP) | ch02 | object |  |
| operating system (OS) | ch02 | computer | ch05 |
| output devices | ch02 | information, computer |  |
| random access memory (RAM) | ch02 | data |  |
| read-only memory (ROM) | ch02 | data |  |
| redundant array of independent disks (RAID) | ch02 |  |  |
| Secondary memory | ch02 | data, computer |  |
| server | ch02 | computer | ch03, ch04, ch05, ch10 |
| storage area network (SAN) | ch02 |  |  |
| allocation | ch03 | data, database_management_system_dbms, fragmentation, replication |  |
| Big data | ch03 | data, process |  |
| Business analytics (BA) | ch03 | data, information |  |
| Business intelligence (BI) | ch03 |  |  |
| class | ch03 | object |  |
| create, read, update, and delete (CRUD) | ch03 | data |  |
| data dictionary | ch03 | data |  |
| Data encryption | ch03 | data |  |
| data hierarchy | ch03 | data |  |
| data lake | ch03 | data |  |
| data mart | ch03 | data, data_warehouse | ch10 |
| data model | ch03 | data, integrity |  |
| data warehouse | ch03 | data, business_intelligence_bi |  |
| data-driven Web site | ch03 | data, database |  |
| Data-mining agents | ch03 | data, information, data_warehouse |  |
| Data-mining analysis | ch03 | data |  |
| database | ch03 | data | ch06, ch07, ch08, ch09 |
| database administrator (DBA) | ch03 | database |  |
| database management system (DBMS) | ch03 | database | ch09 |
| database marketing | ch03 | database |  |
| distributed database management system (DDBMS) | ch03 | data, database, database_management_system_dbms |  |
| encapsulation | ch03 | data, class |  |
| Extraction, transformation, and loading (ETL) | ch03 | data, data_warehouse, database |  |
| foreign key | ch03 | primary_key |  |
| fragmentation | ch03 | database_management_system_dbms |  |
| graph database | ch03 | data, database |  |
| hierarchical model | ch03 |  |  |
| indexed sequential access method (ISAM) | ch03 |  |  |
| inheritance | ch03 | data |  |
| logical view | ch03 | information |  |
| network model | ch03 | hierarchical_model |  |
| normalization | ch03 | data, database |  |
| object | ch03 | data |  |
| object-oriented databases | ch03 | data, object |  |
| Online analytical processing (OLAP) | ch03 | data, information, business_intelligence_bi |  |
| online transaction processing (OLTP) | ch03 | data |  |
| physical view | ch03 | data |  |
| Power BI | ch03 | data, business_intelligence_bi |  |
| primary key | ch03 | database |  |
| query by example (QBE) | ch03 | data, database, structured_query_language_sql |  |
| random access file structure | ch03 |  |  |
| relational model | ch03 | data |  |
| replication | ch03 | data, database, database_management_system_dbms |  |
| sequential access file structure | ch03 |  |  |
| Structured Query Language (SQL) | ch03 | server, database, database_management_system_dbms |  |
| Tableau | ch03 | data, business_intelligence_bi |  |
| Text-mining analysis | ch03 | data, information, process, data_mining_analysis |  |
| acceptable use policies | ch04 |  |  |
| accountability | ch04 |  |  |
| Business networking ethics | ch04 |  |  |
| Cheap fakes | ch04 | fake_news |  |
| Cookies | ch04 |  |  |
| cybersquatting | ch04 |  |  |
| Deepfakes | ch04 |  |  |
| Digital citizenship | ch04 | information |  |
| digital divide | ch04 | information |  |
| disinformation | ch04 | information |  |
| Fake news | ch04 |  |  |
| General Data Protection Regulation (GDPR) | ch04 | data | ch10 |
| Green computing | ch04 |  |  |
| Intellectual property | ch04 |  |  |
| Log files | ch04 | server |  |
| Misinformation | ch04 | information |  |
| Social media networking ethics | ch04 |  |  |
| spam | ch04 |  |  |
| Access controls | ch05 | data, integrity |  |
| Adware | ch05 | information, spyware |  |
| Asymmetric encryption | ch05 |  |  |
| Authentication tokens | ch05 |  |  |
| Availability | ch05 | information |  |
| backdoor | ch05 |  |  |
| Baiting | ch05 | phishing |  |
| Biometric security measures | ch05 |  |  |
| Black hats | ch05 | data, information |  |
| blended threat | ch05 | computer |  |
| brain password | ch05 | database, password |  |
| business continuity planning | ch05 |  |  |
| callback modem | ch05 |  |  |
| Computer fraud | ch05 | data, computer |  |
| Confidentiality | ch05 | information |  |
| Cryptojacking | ch05 | cryptocurrency |  |
| denial-of-service (DoS) attack | ch05 | server |  |
| DNA identification | ch05 |  |  |
| fault-tolerant systems | ch05 | availability |  |
| firewall | ch05 | data |  |
| Gray hats | ch05 |  |  |
| Integrity | ch05 | information |  |
| intrusion detection system (IDS) | ch05 | firewall |  |
| Keystroke loggers | ch05 |  |  |
| logic bomb | ch05 | virus, worm |  |
| Macro viruses | ch05 | virus |  |
| nonrepudiation | ch05 |  |  |
| password | ch05 |  |  |
| Pharming | ch05 | information, phishing |  |
| Phishing | ch05 |  |  |
| Physical security measures | ch05 |  |  |
| PKI (public key infrastructure) | ch05 | data |  |
| quid pro quo | ch05 | data, information, baiting |  |
| rootkit | ch05 | computer |  |
| Script kiddies | ch05 | computer |  |
| Secure Sockets Layer (SSL) | ch05 |  |  |
| Sniffing | ch05 |  |  |
| social engineering | ch05 | information |  |
| Spoofing | ch05 | information |  |
| Spyware | ch05 | information |  |
| symmetric encryption | ch05 |  |  |
| Transport Layer Security (TLS) | ch05 | data, integrity |  |
| Trojan programs | ch05 | computer |  |
| virtual private network (VPN) | ch05 | data |  |
| virus | ch05 | operating_system_os |  |
| White hats | ch05 | information, computer |  |
| worm | ch05 | data, computer |  |
| Zero login | ch05 |  |  |
| Zero trust security | ch05 |  |  |
| global information system (GIS) | ch06 | data, information, geographic_information_system_gis |  |
| global structure | ch06 | information, process |  |
| Global supply chain management | ch06 | supply_chain, supply_chain_management_scm |  |
| international structure | ch06 | process |  |
| multinational corporations (MNCs) | ch06 |  |  |
| multinational structure | ch06 |  |  |
| Offshore outsourcing | ch06 |  |  |
| transborder data flow (TDF) | ch06 | data |  |
| transnational structure | ch06 |  |  |
| collaboration system or collaboration software | ch07 |  |  |
| Collaborative filtering (CF) | ch07 | data, information |  |
| Collaborative planning, forecasting, and replenishment (CPFR) | ch07 | data, supply_chain |  |
| Communication software | ch07 |  |  |
| Customer relationship management (CRM) | ch07 | information |  |
| Customization | ch07 |  |  |
| Document and content management software | ch07 | information |  |
| e-marketplace | ch07 |  |  |
| Electronic data interchange (EDI) | ch07 | data, information |  |
| Enterprise resource planning (ERP) | ch07 | data, information | ch10 |
| enterprise system | ch07 |  |  |
| Knowledge management (KM) | ch07 |  |  |
| online auction | ch07 |  |  |
| Personalization | ch07 | process |  |
| pull technology | ch07 | information |  |
| push technology | ch07 | information, server |  |
| radio frequency identification (RFID) | ch07 | object |  |
| reverse auctions | ch07 |  |  |
| supply chain | ch07 |  |  |
| Supply chain management (SCM) | ch07 | process, supply_chain |  |
| Task management software | ch07 |  |  |
| choice phase | ch08 |  |  |
| decision support system (DSS) | ch08 | data, information, database, model_base | ch09 |
| design phase | ch08 |  |  |
| digital dashboard | ch08 | information |  |
| Executive information systems (EISs) | ch08 | data, information, digital_dashboard |  |
| geographic information system (GIS) | ch08 | information, global_information_system_gis |  |
| implementation phase | ch08 | choice_phase |  |
| intelligence phase | ch08 | data, information |  |
| management support systems (MSSs) | ch08 | information |  |
| managerial designer | ch08 | decision_support_system_dss |  |
| model base | ch08 | information, database, decision_support_system_dss | ch09 |
| model builder | ch08 | data, information |  |
| Semistructured decisions | ch08 | information |  |
| Structured decisions | ch08 |  |  |
| technical designer | ch08 | data, decision_support_system_dss |  |
| Unstructured decisions | ch08 |  |  |
| Artificial intelligence (AI) | ch09 |  |  |
| Artificial neural networks (ANNs) | ch09 | spam |  |
| Augmented intelligence | ch09 |  |  |
| backward chaining | ch09 |  |  |
| case-based reasoning (CBR) | ch09 | information, database |  |
| Expert systems | ch09 |  |  |
| explanation facility | ch09 |  |  |
| forward chaining | ch09 |  |  |
| Fuzzy logic | ch09 | computer |  |
| Genetic algorithms (GAs) | ch09 | process |  |
| inference engine | ch09 | decision_support_system_dss, model_base, backward_chaining |  |
| Intelligent agents | ch09 |  |  |
| knowledge acquisition facility | ch09 |  |  |
| knowledge base | ch09 | database |  |
| knowledge base management system (KBMS) | ch09 | database_management_system_dbms, knowledge_base |  |
| Machine learning | ch09 | process |  |
| Monitoring and surveillance agents | ch09 | computer |  |
| natural-language processing (NLP) | ch09 |  |  |
| Personal agents | ch09 | information |  |
| Robots | ch09 | artificial_intelligence_ai |  |
| Shopping and information agents | ch09 | information |  |
| soft robot | ch09 | robots |  |
| 3D printing | ch10 | process, object |  |
| 4D printing | ch10 |  |  |
| application service providers (ASPs) | ch10 |  |  |
| Augmented reality (AR) | ch10 | object, virtual_reality_vr |  |
| avatar | ch10 | virtual_world |  |
| backup as a service (BaaS) | ch10 | data, blockchain_as_a_service_baas |  |
| blockchain | ch10 | data |  |
| Blockchain as a service (BaaS) | ch10 | backup_as_a_service_baas, blockchain |  |
| cave automatic virtual environment (CAVE) | ch10 |  |  |
| Cloud computing | ch10 | data, grid_computing, software_as_a_service_saas |  |
| Cloud storage | ch10 |  |  |
| community cloud | ch10 |  |  |
| contextual computing | ch10 |  |  |
| Cryptocurrency | ch10 | computer |  |
| data as a service (DaaS) | ch10 | data |  |
| Distributed cloud computing | ch10 | data, cloud_computing |  |
| Edge computing | ch10 | data |  |
| egocentric environment | ch10 | virtual_reality_vr |  |
| exocentric environment | ch10 | data, egocentric_environment, virtual_reality_vr |  |
| Fungible tokens | ch10 | blockchain |  |
| grid computing | ch10 | computer |  |
| hybrid cloud | ch10 | private_cloud, public_cloud |  |
| Implanted microchips | ch10 | information |  |
| Infrastructure as a service (IaaS) | ch10 | computer, cloud_computing |  |
| metaverse | ch10 | virtual_world |  |
| Mixed reality (MR) | ch10 |  |  |
| Multicloud | ch10 | public_cloud |  |
| Nanotechnology | ch10 |  |  |
| non-fungible token (NFT) | ch10 | blockchain |  |
| on-demand software | ch10 |  |  |
| Platform as a service (PaaS) | ch10 |  |  |
| private cloud | ch10 |  |  |
| public cloud | ch10 |  |  |
| QR (quick response) code | ch10 |  |  |
| Quantum computing | ch10 | computer |  |
| security as a service (SECaaS) | ch10 |  |  |
| Semi-fungible tokens (SFTs) | ch10 | fungible_tokens |  |
| Software as a Service | ch10 |  |  |
| Software as a service (SaaS) | ch10 | application_service_providers_asps, on_demand_software |  |
| Utility (on-demand) computing | ch10 |  |  |
| Virtual reality (VR) | ch10 | computer |  |
| virtual world | ch10 |  |  |
