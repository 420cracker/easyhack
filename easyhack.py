#!/bin/bash
clear
check=0
check=1
ok="ok"
ENTER="press ENTER for main menu"
#colors
w='\e[97m'
g='\033[1;92m'
r='\033[1;91m'
a='\033[1;94m'
b='\e[1;4m'
cyan='\033[1;36m'
green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'
reset='\033[0m'
G='\e[110m'
G1='\e[101m'
o='\033[0m'
#banner
sleep 0.5
echo -e $yellow
figlet -f big "EasYHaCk"

echo -e "                   $g"420"$r"Gang"$w""" 
echo -e "$a              # # # # # # # # # # # #"
echo -e "$a              #$G                     $o$a#"
echo -e "$a              #$G    $r"EasY_HaCk  V3.2"$a   $o$a#"
echo -e "$a              #$G                     $o$a#"
echo -e "$a              # # # # # # # # # # # #"
echo
echo -e "  $G1$w Welcome to This Tool For Penetration Testing $o" 
Author : Haris
Tool. : Easy Hack
Location : College Road Taunsa Sharif
echo -e $o"$green               Made by$yellow Haris Haroon "$o
echo -e " $g          Developers Team :  Taunsa Hackers "
echo " "
echo -e "              $red Press ENTER to Continue"
echo -e $yellow
echo -n -e "[EasY_HaCk]~#:"
sleep 2
read tmp
echo -e " "
echo -e "$blue THE MAIN MENU"
sleep 0.5
echo -e "$red --------------"
sleep 0.1
echo -e "$a      [$r"01"$a"]"$g PAYLOAD GENERATOR"
sleep 0.1
echo -e "$a      [$r"02"$a"]"$g ADVANCE NMAP SCAN"
sleep 0.1
echo -e "$a      [$r"03"$a"]"$g WEB-HACKS"
sleep 0.1
echo -e "$a      [$r"04"$a"]"$g PASSWORD CRACK"
sleep 0.1
echo -e "$a      [$r"05"$a"]"$g Termux Tools"
sleep 0.1
echo -e "$a      [$r"06"$a"]"$g MY SERVER"
sleep 0.1
echo -e "$a      [$r"07"$a"]"$g ABOUT"
sleep 0.1
echo -e "$a      [$r"08"$a"]"$g UPDATE ME"
sleep 0.1
echo -e "$a      [$r"09"$a"]"$g CONTACT ME"
sleep 0.1
echo -e "$a      [$w"XX"$a"]"$g EXIT $reset"
sleep 0.5
echo -e $yellow
echo -n $B "[EasY_HaCk]~#:"
read option
if [[ $option == "" ]];
then
	echo -e "$red Please enter correct number of choice"
	echo
	echo -e "$green Plz wait... You are redirecting to main menu"
	sleep 2
EasY_HaCk
fi

create_payload()
{
python2 $PREFIX/share/EasY_HaCk/.modules/.pay.py
EasY_HaCk
}

about()
{
echo -e "$green                    EasY_HaCk $yellow

This tool is to provide easy user interface 
My aim behind this tool is to make penetration testing easy 
like payload creation, metasploit installation, 
ngrok installation, network scanning and Websites Hacking 
& Wait for my updates of$r EasY_HaCk$yellow tool 
with some extra features and options and all 
CREDITS GOES TO$g SABRi$yellow"@"$green"ZAKI"$yellow from $g"Alpha"$r"Team"$w"DZ"$r (o_O)$reset"
echo
echo -e "$red                    press ENTER"
echo -n "[EasY_HaCk]~#:"
read tmpp
EasY_HaCk
}

update()
{
echo -e "\033[1;33m Updating ..."
echo
cd $PREFIX/share/EasY_HaCk/
git reset --hard > /dev/null
git pull
chmod +x *
cp -f $PREFIX/share/EasY_HaCk/EasY_HaCk $PREFIX/bin/
echo
echo
echo -e "\033[1;31m Updated Successfully \033[0m"
echo
echo -e "$red                    press ENTER"
echo -n "[EasY_HaCk]~#:"
read tmp
EasY_HaCk
}

password()
{
clear
$PREFIX/share/EasY_HaCk/.modules/.password
echo -e "$red                    press ENTER"
echo -n "[EasY_HaCk]~#:"
read tmp
EasY_HaCk
}

termux()
{
clear
$PREFIX/share/EasY_HaCk/.modules/.Termux_Tools
EasY_HaCk
}


contact()
{
echo -e "$green ********** Do You Want to Contact Me ? **********"
echo -e "$r                     press ENTER$reset"
echo -n "[EasY_HaCk]~#:"
read tmp4
echo -e "$w My Facebook ID> $yellow www.facebook.com/sabri.zaki.31"
echo -e "$red               $ENTER$reset"
echo -n "[EasY_HaCk]~#:"
read tmp5
EasY_HaCk
}

nmap()
{
if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; 
then
clear
echo -e $g "welcom to EasY_ScaN"
echo -e "$yellow"[✔]:[ "$w"Internet"$yellow ]:$green connected !"
sleep 3
clear
echo "EasY_ScaN "
sleep 0.3
clear
echo "EasY_ScaN ./ "
sleep 0.3
clear
echo "EasY_ScaN ..\ "
sleep 0.3
clear
echo "EasY_ScaN .../ "
sleep 0.3
clear
echo "EasY_ScaN ....\ "
sleep 0.3
clear
echo "EasY_ScaN ...../ "
sleep 0.3
clear
echo "EasY_ScaN ......\ "
sleep 0.3
clear
echo "EasY_ScaN ......./ "
sleep 0.3
clear
echo "EasY_ScaN ........\ "
sleep 0.3
clear
echo "EasY_ScaN ........./ "
sleep 0.3
clear
echo "EasY_ScaN ...........\ "
$PREFIX/share/EasY_HaCk/.modules/.EasY_ScaN
else
echo -e "$red sorry ther is no internet im your mobile "
echo -e "$red you can't use EasY_ScaN"
echo -e "$yellow "["$red "x"$yellow ]:[$w "Internet"$yellow ]:$red Not connected !"
sleep 20
$PREFIX/share/EasY_HaCk/EasY_HaCk
fi

}

web_hacking()
{
if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; 
then
clear
echo -e $g "welcom to web_hacking"
echo -e "$yellow"[✔]:[ "$w"Internet"$yellow ]:$green connected !"
sleep 4 
clear
echo "WEB-HACK "
sleep 0.2
clear
echo "WEB-HACK ./ "
sleep 0.2
clear
echo "WEB-HACK ..\ "
sleep 0.2
clear
echo "WEB-HACK .../ "
sleep 0.2
clear
echo "WEB-HACK ....\ "
sleep 0.2
clear
echo "WEB-HACK ...../ "
sleep 0.2
clear
echo "WEB-HACK ......\ "
sleep 0.2
clear
echo "WEB-HACK ......./ "
sleep 0.2
clear
echo "WEB-HACK ........\ "
sleep 0.2
clear
echo "WEB-HACK ........./ "
sleep 0.2
clear
echo "WEB-HACK ...........\ "
$PREFIX/share/EasY_HaCk/.modules/.web
else
echo -e "$red sorry ther is no internet im your mobile "
echo -e "$red you can't use WEB-HACK"
echo -e "$yellow "["$red "x"$yellow ]:[$w "Internet"$yellow ]:$red Not connected !"
sleep 20
$PREFIX/share/EasY_HaCk/EasY_HaCk
fi

}

server()
{
$PREFIX/share/EasY_HaCk/.modules/.server

}


case "$option" in
	1) if [ $check = 0 ];
		then
			create_payload
			fi
			create_payload
		 ;;
	2) nmap
		;;
	3) web_hacking
		;;
	4) password
		;;
	5) termux
		;;
	6)  server
		;;
	7)  about
		 ;;
	8)  update
		 ;;
	9) contact
		;;
esac

if [ $zaki -eq x ] || [ $zaki -eq X ] || [ $zaki -eq XX ] || [ $zaki -eq xx ] ;
then
clear
echo " by by "
exit 
else
clear
echo "E.................................\ "
sleep 0.1
clear
echo "EX................................/ "
sleep 0.1
clear
echo "EXI...............................\ "
sleep 0.1
clear
echo "EXIT............................../ "
sleep 0.1
clear
echo "EXIT E............................\ "
sleep 0.1
clear
echo "EXIT EA.........................../ "
sleep 0.1
clear
echo "EXIT EAS..........................\ "
sleep 0.1
clear
echo "EXIT EASY........................./ "
sleep 0.1
clear
echo "EXIT EASY H.......................\ "
sleep 0.1
clear
echo "EXIT EASY HA....................../ "
sleep 0.1
clear
echo "EXIT EASY HAC.....................\ "
sleep 0.1
clear
echo "EXIT EASY HACK..................../ "
sleep 0.1
clear
echo "EXIT EASY HACK T..................\ "
sleep 0.1
clear
echo "EXIT EASY HACK TO................./ "
sleep 0.1
clear
echo "EXIT EASY HACK TOO................\ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL.............../ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL...............\ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL.............../ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL...............\ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL.............../ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL...............\ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL.............../ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL...............\ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL.............../ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL...............\ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL.............../ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL...............\ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL.............../ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL...............\ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL.............../ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL...............\ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL.............../ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL...............\ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL.............../ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL...............\ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL.............../ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL...............\ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL.............../ "
sleep 0.1
clear
echo "EXIT EASY HACK TOOL...............\ "
sleep 0.1
clear
echo -e "\033[1;91mzaki sabri  wish you all the best ♡ you all "
sleep 3
clear 
exit
fi
read zaki

