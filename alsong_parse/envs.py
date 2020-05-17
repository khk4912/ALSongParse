XML_TEMPLATE = """
<?xml
    version="1.0"
    encoding="UTF-8"
    ?>
<SOAP-ENV:Envelope
    xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
    xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:ns2="ALSongWebServer/Service1Soap"
    xmlns:ns1="ALSongWebServer"
    xmlns:ns3="ALSongWebServer/Service1Soap12">
    <SOAP-ENV:Body>
        <ns1:GetSyncLyricBySearch>
            <ns1:encData>{enc_data}</ns1:encData>
            <ns1:title>{title}</ns1:title>
            <ns1:artist>{artist}</ns1:artist>
            <ns1:playtime>{ms_playtime}</ns1:playtime>
        </ns1:GetSyncLyricBySearch>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""


XML_WITH_MP3_TEMPLATE = """
<?xml
    version="1.0"
    encoding="UTF-8"
    ?>
<SOAP-ENV:Envelope
    xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
    xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:ns2="ALSongWebServer/Service1Soap"
    xmlns:ns1="ALSongWebServer"
    xmlns:ns3="ALSongWebServer/Service1Soap12">
    <SOAP-ENV:Body>
        <ns1:GetMurekaInfo>
            <ns1:encData>{enc_data}</ns1:encData>
            <ns1:md5>{hash}</ns1:md5>
        </ns1:GetMurekaInfo>>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""

XML_RESMBLE_TEMPLATE = """
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
    xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
    xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:ns2="ALSongWebServer/Service1Soap"
    xmlns:ns1="ALSongWebServer"
    xmlns:ns3="ALSongWebServer/Service1Soap12">
    <SOAP-ENV:Body>
        <ns1:GetResembleLyricList2>
            <ns1:encData>{enc_data}</ns1:encData>
            <ns1:title>{title}</ns1:title>
            <ns1:artist>{artist}</ns1:artist>
            <ns1:pageNo>1</ns1:pageNo>
        </ns1:GetResembleLyricList2>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""

XML_WITH_ID_TEMPLATE = """<?xml
    version="1.0"
    encoding="UTF-8"
    ?>
<SOAP-ENV:Envelope
    xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
    xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:ns2="ALSongWebServer/Service1Soap"
    xmlns:ns1="ALSongWebServer"
    xmlns:ns3="ALSongWebServer/Service1Soap12">
    <SOAP-ENV:Body>
        <ns1:GetLyricByID2>
            <ns1:encData>{enc_data}</ns1:encData>
            <ns1:lyricID>{lyric_id}</ns1:lyricID>
            </ns1:GetLyricByID2>
        </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>"""
