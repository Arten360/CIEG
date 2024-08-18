# CIEG - Carbon Intensity in the Electrical Grid

Dieses Projekt zielt darauf ab, die orts- und zeitabhängige CO2-Intensität des Stromnetzes für weitere Berechnungen und Analysen zu nutzen. Die Inspiration stammt aus dem Coursera Kurs "Carbon Aware Computing".

**Was ist CO2-Intensität?**

Die CO2-Intensität misst, wie sauber der Stromverbrauch in einer bestimmten Region zu einem bestimmten Zeitpunkt ist. Sie gibt an, wie viele Gramm Kohlendioxid (CO2) bei der Erzeugung von einer Kilowattstunde (kWh) Strom freigesetzt werden. 

Mit anderen Worten: Die CO2-Intensität repräsentiert den Treibhausgas-Fußabdruck von 1 kWh, die in dieser Region verbraucht wird. Dieser Fußabdruck wird in gCO2-Äq (Gramm CO2-Äquivalent) gemessen. Das bedeutet, dass jede Art von Treibhausgas in sein CO2-Äquivalent umgerechnet werden kann, was das globale Erwärmungspotenzial über 100 Jahre betrifft (z. B. hat 1 Gramm Methan die gleiche globale Erwärmungswirkung während 100 Jahren wie ~34 Gramm CO2 im gleichen Zeitraum).

Die CO2-Intensität der Stromerzeugung einer Region wird durch den Mix der Kraftwerke und ihre zugehörigen CO2-Intensitätsfaktoren bestimmt. Es gibt zwei Arten von Emissionsfaktoren, die auf der Karte angezeigt werden: Standardfaktoren und regionale Faktoren.

**Wie wird die CO2-Intensität berechnet?**

Lebenszyklus-Emissionen für die Stromerzeugung
Die auf der Karte angezeigten CO2-Intensitätsfaktoren sind Emissionsfaktoren, die auf dem gesamten Lebenszyklus der eingesetzten Brennstoffe und Erzeugungstechnologien basieren. Diese Zahlen stammen hauptsächlich aus dem IPCC (2014) Fifth Assessment Report, der Emissionsfaktoren zusammenfasst, die von einer Vielzahl von begutachteten Studien geschätzt wurden. Der IPCC-Bericht 2014 gilt als globaler Standard für die Messung des globalen Erwärmungspotenzials verschiedener Stromquellen.

Emissionen aus der Extraktion der Ressourcen, die zur Errichtung der installierten Kapazitäten erforderlich sind, Emissionen aus den direkten Betriebsabläufen und mit dem Lebensende verbundene Emissionen werden alle berücksichtigt.

**Warum ist das wichtig?**


Die CO2-Intensität des Stroms variiert stark je nach Ort und Uhrzeit, abhängig von der Zusammensetzung der Stromerzeugung (z.B. Kohlekraftwerke vs. erneuerbare Energien).  Durch die Berücksichtigung dieser Schwankungen können wir:

* **Energieeffizienz steigern:** Anwendungen und Prozesse zu Zeiten mit niedriger CO2-Intensität ausführen.
* **Nachhaltige Entscheidungen treffen:** Den CO2-Fußabdruck von Rechenprozessen und anderen Aktivitäten minimieren.
* **Die Entwicklung von "Carbon Aware" Technologien fördern:**

**Datenquelle**

Wir nutzen die API von Electricity Maps ([https://www.electricitymaps.com/free-tier-api](https://www.electricitymaps.com/free-tier-api)) um auf aktuelle Daten zur CO2-Intensität zuzugreifen. Weitere Informationen zur Methodik finden Sie unter [https://www.electricitymaps.com/methodology#carbon-intensity-and-emission-factors](https://www.electricitymaps.com/methodology#carbon-intensity-and-emission-factors)

**Authentifizierung**
Der Authentifizierungsschlüssel (auth-token) für den Zugriff auf die API ist in der Datei `helper.py` für den Benutzer `martin.stolz@magenta.de` hinterlegt.

**Codebeispiele**

* **`readmecarbon4e.py`:** Zeigt, wie das CO2-Footprint an einem definierten Standort eingelesen werden kann.
* **`einsacarbon4e.py`:** Enthält einen vereinfachten Code für das Auslesen des CO2-Bedarfs am Standort des EinsA.

**Zukünftige Entwicklungen**


* Integration in weitere Anwendungen und Dienste.
* Automatische Anpassung von Prozessen an die aktuelle CO2-Intensität.
* Erweiterung der Datenquellen und Analysemethoden.

**Beiträge willkommen!**

Dieses Projekt ist Open Source und wir freuen uns über jede Form von Unterstützung:

* Codebeiträge
* Fehlerberichte
* Ideen für Verbesserungen




