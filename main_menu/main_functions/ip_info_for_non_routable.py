from ipaddress import ip_network

non_routable_ip = {ip_network('0.0.0.0/8'): """
Диапазон  <code>0.0.0.0/8</code> описан в RFC1122 , RFC3330 и RFC1700 как \n"Этот хост в этой сети" 
(this host on this network), 
хотя, учитывая варианты применения, правильнее было бы назвать его как "любой адрес". В частности, 
IP-адрес <code>0.0.0.0</code> используется для:\n
<b>- обозначения в конфигурационных файлах серверов и выводе netstat информации о том, 
что определенный сервис "слушает" запросы на всех IP-адресах данного сервера;</b>\n
<b>- конфигурации маршрута по умолчанию на активном сетевом оборудовании;</b>\n
<b>- использования в качестве src address в запросах на получение IP-адреса (DHCPDISCOVER);</b>\n
<b>- обозначения IP-адреса в суммаризованных событиях безопасности IDS/IPS/WAF/etc 
(например, TCP Host Sweep - обозначение dst host в случае инициации коннектов к большому количеству IP-адресов).</b>""",
                   ip_network('10.0.0.0/8'): """
<code>10.0.0.0/8</code>
<code>172.16.0.0/12</code>
<code>192.168.0.0/16</code>
<b>Три вышеописанных диапазона 
не маршрутизируются в Интернет, 
поскольку зарезервированы под 
организацию локальных сетей ИТ-инфраструктуры компаний.
Описаны изначально в RFC1918 . 
При этом любая организация вправе использовать любой из вышеописанных диапазонов 
для IP-адресного плана либо все вместе на свое усмотрение. 
Для взаимодействия с внешними ресурсами и партнерами во избежание пересечения 
адресного пространства должен использоваться NAT.</b>""",

                   ip_network('172.16.0.0/12'): """
<code>10.0.0.0/8</code>
<code>172.16.0.0/12</code>
<code>192.168.0.0/16</code>
<b>Три вышеописанных диапазона 
не маршрутизируются в Интернет, 
поскольку зарезервированы под 
организацию локальных сетей ИТ-инфраструктуры компаний.
Описаны изначально в RFC1918 . 
При этом любая организация вправе использовать любой из вышеописанных диапазонов 
для IP-адресного плана либо все вместе на свое усмотрение. 
Для взаимодействия с внешними ресурсами и партнерами во избежание пересечения 
адресного пространства должен использоваться NAT.</b>""",

                   ip_network('192.168.0.0/16'): """
<code>10.0.0.0/8</code>
<code>172.16.0.0/12</code>
<code>192.168.0.0/16</code>
<b>Три вышеописанных диапазона 
не маршрутизируются в Интернет, 
поскольку зарезервированы под 
организацию локальных сетей ИТ-инфраструктуры компаний.
Описаны изначально в RFC1918 . 
При этом любая организация вправе использовать любой из вышеописанных диапазонов 
для IP-адресного плана либо все вместе на свое усмотрение. 
Для взаимодействия с внешними ресурсами и партнерами во избежание пересечения 
адресного пространства должен использоваться NAT.</b>""",

                   ip_network('100.64.0.0/10'): """
<b>В соответствии с RFC6598 , <code>100.64.0.0/10</code> используется 
как транслируемый блок адресов для межпровайдерских взаимодействий 
и Carrier Grade NAT. Особенно полезен как общее свободное адресное IPv4-пространство RFC1918, 
необходимое для интеграции ресурсов провайдеров, а также для выделения немаршрутизируемых адресов абонентам. 
Конечно, в последнем случае никто не мешает использовать RFC1918 - на откуп сетевым архитекторам.</b>""",
                   ip_network('127.0.0.0/8'):
                       """<b>В случае, если сервису необходим для работы функционирующий сетевой стек, который не будет 
давать сбоев при отключении от сети, используются loopback-адреса. Выделение <code>127.0.0.0/8</code> под 
внутренние loopback-адреса определено в RFC1122 . В отличие от адресов RFC1918 и RFC6598, 
адреса для loopback не должны присутствовать и обрабатываться ни в одной сети</b>, 
только во внутренней таблице маршрутизации хоста.""",
                   ip_network('169.254.0.0/16'):
                       """<b>В соответствии с RFC3927 , определен как Link-Local для автоматической конфигурации. Думаю, 
каждый человек хоть раз в жизни, но успел столкнуться с ситуацией, когда ПК, не получив 
IP-адрес от DHCP-сервера, присваивает сам себе непонятный и нигде не прописанный ранее IP, 
начинающийся на 169.254... Это и есть реализация рекомендаций из RFC3927.</b>""",
                   ip_network('192.0.0.0/24'):
                       """<b>Блок не встречается в повседневной жизни, 
поскольку зарезервирован под IANA для нужд IETF в 
соответствии с RFC6890 .</b>""",
                   ip_network('192.0.2.0/24'):
                       """
<code>192.0.2.0/24</code>
<code>198.51.100.0/24</code> 
<code>203.0.113.0/24</code> 
<b>Эти три подсети, в соответствии с RFC5737 , 
зарезервированы для описания в документах. Многие, думаю, сталкивались с ситуацией, 
когда для статьи в журнале либо презентации на конференции нужно показать некоторое адресное 
пространство, которое, с одной стороны, не должно ассоциироваться с локальными 
RFC1918-адресами и как бы показывать Интернет, но, в то же время, и не принадлежать никому, 
чтобы не было лишних вопросов со стороны владельца адресов. Для этого и были выделены три 
подсети /24 по принципу "дарю, пользуйтесь".</b>""",
                   ip_network('198.51.100.0/24'):
                       """
<code>192.0.2.0/24</code>
<code>198.51.100.0/24</code> 
<code>203.0.113.0/24</code> 
<b>Эти три подсети, в соответствии с RFC5737 , 
зарезервированы для описания в документах. Многие, думаю, сталкивались с ситуацией, 
когда для статьи в журнале либо презентации на конференции нужно показать некоторое адресное 
пространство, которое, с одной стороны, не должно ассоциироваться с локальными 
RFC1918-адресами и как бы показывать Интернет, но, в то же время, и не принадлежать никому, 
чтобы не было лишних вопросов со стороны владельца адресов. Для этого и были выделены три 
подсети /24 по принципу "дарю, пользуйтесь".</b>""",
                   ip_network('203.0.113.0/24'):
                       """
<code>192.0.2.0/24</code>
<code>198.51.100.0/24</code> 
<code>203.0.113.0/24</code> 
<b>Эти три подсети, в соответствии с RFC5737 , 
зарезервированы для описания в документах. Многие, думаю, сталкивались с ситуацией, 
когда для статьи в журнале либо презентации на конференции нужно показать некоторое адресное 
пространство, которое, с одной стороны, не должно ассоциироваться с локальными 
RFC1918-адресами и как бы показывать Интернет, но, в то же время, и не принадлежать никому, 
чтобы не было лишних вопросов со стороны владельца адресов. Для этого и были выделены три 
подсети /24 по принципу "дарю, пользуйтесь".</b>""",
                   ip_network('192.88.99.0/24'):
                       """
<b>Частный случай из подсети <code>192.0.0.0/24</code>, но заслуживает отдельного описания из технологического интереса. 
В связи с необходимостью взаимодействия новых IPv6-облаков между 
собой в преобладающем IPv4-транзите необходим NAT 6to4. При этом некоторые межконтинентальные 
сервисы, наиболее критичные из которых - корневые сервера DNS, используют технологию anycast. 
Наверное, это тема для отдельной заметки, но вкратце: подсеть, выделенная под any-cast, 
может терминироваться в любой автономной системе для обеспечения отказоустойчивости. В RFC3068 
был выделен пул адресов <code>192.88.99.0/24</code> для NAT 6to4 сервисов, использующих any-cast. Как видим, 
выделен был этот пул еще в 2001 году, после чего, нахлебавшись проблем на практике, 
в 2015 году издается RFC7526 , отменяющий RFC3068, но при этом подсеть <code>192.88.99.0/24</code> остается 
зарезервированной под нужды IETF.</b>""",
                   ip_network('198.18.0.0/15'):
                       """
<code>198.18.0.0/15</code>                       
<b>Диапазон выделен под лаборатории нагрузочного тестирования (Benchmarking) в соответствии с 
RFC2544 и уточнением в RFC6815 , что данный диапазон не должен быть доступен в Интернет во 
избежание конфликтов. Опять же, никто при этом не отменяет использование RFC1918, 
но для больших сетей с крупными лабораториями лишний блок /15 явно не помешает.</b>""",
                   ip_network('224.0.0.0/4'):
                       """
<code>224.0.0.0/4</code>                    
<b>Этот диапазон в исторической классификации еще называется как Class D. Выделен под 
Multicast, уточнение специфики работы которого тоже вроде как отдельная заметка. В RFC5771 
подробно расписано использование подсетей внутри блока, но суть остается той же: эти адреса не 
закреплены ни за каким провайдером, и, соответственно, через Интернет не должны светиться.</b>""",
                   ip_network('240.0.0.0/4'):
                       """
<b>В соответствии с RFC1122 , <code>240.0.0.0/4</code>, исторически также известный как 
Class E, зарезервирован под использование в будущем. Юмор ситуации в том, что RFC1122 
издавался еще в августе 1989 года, сейчас 2016 год, IPv4-адреса закончились, но для IETF 
будущее еще не наступило, потому что из всей большой подсети /4 до сих пор используется только 
один адрес. Но, наверное, если посчитать статистику по всем подсетям всех организаций мира, 
этот адрес окажется в лидерах, потому что сервисы, использующие broadcast, обращаются к адресу 
<code>255.255.255.255</code>, который и принадлежит описанному диапазону.</b>"""}
