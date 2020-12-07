ENDPOINT_URL = "http://lyrics.alsong.co.kr/alsongwebservice/service1.asmx"

GET_RESEMBLE_XML_LIST_HEADER = {
    "Host": "lyrics.alsong.co.kr",
    "User-Agent": "gSOAP/2.7",
    "Content-Type": "application/soap+xml",
    "SOAPAction": "ALSongWebServer/GetResembleLyricList2",
}

GET_RESEMBLE_XML_COUNT_HEADER = {
    "Host": "lyrics.alsong.co.kr",
    "User-Agent": "gSOAP/2.7",
    "Content-Type": "application/soap+xml",
    "SOAPAction": "ALSongWebServer/GetResembleLyric2Count",
}

GET_RESEMBLE_XML_LIST = """<?xml
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
            <ns1:GetResembleLyricList2>
                <ns1:encData>{enc_data}</ns1:encData>
                <ns1:title>{title}</ns1:title>
                <ns1:artist>{artist}</ns1:artist>
                <ns1:pageNo>1</ns1:pageNo>
            </ns1:GetResembleLyricList2>
        </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
"""


GET_RESEMBLE_XML_COUNT = """<?xml
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
            <ns1:GetResembleLyric2Count>
                <ns1:stQuery>
                    <ns1:strTitle>{title}</ns1:strTitle>
                    <ns1:strArtistName>{artist}</ns1:strArtistName>
                    </ns1:stQuery>
                </ns1:GetResembleLyric2Count>
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

#                 <ns1:encData>6186a8b3cc48e85479f7f82755374f2c42e9eeb9f52fe3636e53d3cbde1289cce6edf5084723928877a44bebaaad99bd83ebf56cae79745014720d1fbeee68b2986f2e2fff926a37feeee3c90545da49f1ffb9ed5b775dcf88362e026e152392480933aeb343789ecfbc9395d375fa593b</ns1:encData>
