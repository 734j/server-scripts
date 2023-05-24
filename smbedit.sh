mkdir -p ~/smb-backups
cp /etc/samba/smb.conf ~/smb-backups/smb_$(date +"%Y%m%d_%H%M").conf
sudo vim /etc/samba/smb.conf

read -r -p "Do you want to restart the smbd daemon? [y/N] " response
case "$response" in
    [yY][eE][sS]|[yY]) 
        sudo systemctl restart smbd
	echo "smbd will restart"
	echo "The old smb.conf file was copied to ~/smb-backups"
        ;;
    *)
        echo "smbd will not restart"
	echo "The old smb.conf file was copied to ~/smb-backups"
        ;;
esac
