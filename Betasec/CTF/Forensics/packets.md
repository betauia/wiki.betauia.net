# Packets
`wireshark file.pcap`
`strings file.pcap | grep -i "key"`

convert .pcapng to .pcap (requires wireshark):  // or just try and rename
`editcap old_file.pcapng new_file.pcap`

scrape out images, files, credentials and other goods from PCAP and PCAPNG files:
>http://www.netresec.com/?page=NetworkMiner

visualize a Packet Capture offline as a Network Diagram:
>https://github.com/Srinivas11789/PcapXray

export objects in wireshark (files)
`tcpflow -r file.pcap` // extracts files

run foremost on .pcap