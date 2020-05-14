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
            <ns1:encData>
                4e06a8c06f189e54e0f22e7f645f172bc6ba2702618c445c2973848e004d4709d745cad80f1fc63654bae492019e771af038de6822b1123687d6598f0064cae237c4e1ac873f4d3aa267a6c27197878a0638cf29b571f049d50add1f4303b8d46c05020516d5ca8000d05a10371829da7a90aad4f4c68a62c0c6083ede28f247
                </ns1:encData>
            <ns1:title>
                {title}
                </ns1:title>
            <ns1:artist>
                {artist}
                </ns1:artist>
            <ns1:playtime>
                {ms_playtime}
                </ns1:playtime>
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
            <ns1:encData>
                4e06a8c06f189e54e0f22e7f645f172bc6ba2702618c445c2973848e004d4709d745cad80f1fc63654bae492019e771af038de6822b1123687d6598f0064cae237c4e1ac873f4d3aa267a6c27197878a0638cf29b571f049d50add1f4303b8d46c05020516d5ca8000d05a10371829da7a90aad4f4c68a62c0c6083ede28f247
                </ns1:encData>
            <ns1:md5>
                {hash}
                </ns1:md5>
        </ns1:GetMurekaInfo>>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""



XML_RESPONSE_TEMPLATE = """
eXtensible Markup Language
    <?xml
        version="1.0"
        encoding="utf-8"
        ?>
    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <soap:Body>
            <GetSyncLyricBySearchResponse
                xmlns="ALSongWebServer">
                <GetSyncLyricBySearchResult>
                    <strStatusID>
                        1
                        </strStatusID>
                    <strInfoID>
                        9644892
                        </strInfoID>
                    <strRegistDate/>
                    <strTitle>
                        GOTT (Feat. MOON, 우원재, Jvcki Wai)
                        </strTitle>
                    <strArtist>
                        사이먼 도미닉
                        </strArtist>
                    <strAlbum>
                        화기엄금
                        </strAlbum>
                    <strCountGood>
                        0
                        </strCountGood>
                    <strCountBad>
                        0
                        </strCountBad>
                    <strLyric>
                         [truncated][00:00.07]사이먼 도미닉&lt;br&gt;[00:03.54]GOTT (Feat. MOON, 우원재, Jvcki Wai)&lt;br&gt;[00:07.82][Intro. Simon Dominic] \uFEFFlisten up&lt;br&gt;[00:08.69]fake gangsters &lt;br&gt;[00:09.30]and my honeys&lt;br&gt;[0
                        </strLyric>
                    <strRegisterFirstName>
                        BipolarDiSorder0404
                        </strRegisterFirstName>
                    <strRegisterFirstEMail/>
                    <strRegisterFirstURL/>
                    <strRegisterFirstPhone/>
                    <strRegisterFirstComment/>
                    <strRegisterName>
                        BipolarDiSorder0404
                        </strRegisterName>
                    <strRegisterEMail/>
                    <strRegisterURL/>
                    <strRegisterPhone/>
                    <strRegisterComment/>
                    </GetSyncLyricBySearchResult>
                </GetSyncLyricBySearchResponse>
            </soap:Body>
        </soap:Envelope>
"""
