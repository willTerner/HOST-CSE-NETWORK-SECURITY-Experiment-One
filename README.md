### 根据机器更改脚本中的ip
### 然后sudo sh 脚本名，运行脚本即可
   + synflood攻击
     + start_1_c.sh，用c语言实现
     + start_1_python.sh，用scapy 实现
   + tcp rst攻击
     + start_2_python1.sh，对应scapy 自动攻击，注意要还要根据wireshark截包更改一些字段
     + start_2_python2.sh，对应scapy手动攻击
   + tcp劫持会话
     + start_2_python1.sh，对应scapy手动攻击，注意要wireshark截包更改一些字段
     + start_2_python2.sh，对应scapy自动攻击