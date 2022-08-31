read -p "Type your target OS [ window or linux ] ::: " os
echo "your OS is ${os}"

if [[ ${os} -eq 'window' ]]
then
	sed -i -e 's/\r$//' *.sh
	sed -i -e 's/\r$//' .env
elif [[ ${os} -eq 'linux' ]]
then
	sed -i -e 's/$/\r' *.sh
	sed -i -e 's/$/\r' .env
else
	echo "Invalid OS"
fi

echo done
