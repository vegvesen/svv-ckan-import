# svv-ckan-import
Filer for å importere data inn i Dataportalen.

Inneholder kode for å importere + datafiler med metadataene for datasettene vi vil ha i Dataportalen.

I første omgang legger vi inn datasettene som nå ligger på http://vegvesen.no/data

Hvis du vil se på informasjonen, bruk Excel-filene i mappa working-files-data, de er lettere å lese enn CSV-filene.
I tillegg ligger det noe data (stikkord for datasett + tilordning til grupper) i fila import.py

Når du skal oppdatere informasjon:
1. Rediger Excel-fila
2. Lagre den som csv-fil
3. Åpne CSV-fila i Notepad og velg Encoding --> Convert to UTF-8-BOM (hvis du dropper dette siste trinnet blir ÆØÅ til mystiske tegn)
