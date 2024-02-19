# jellyfin-avatars
adds a html page and a button to jellyfin 10.7.x for users to get more avatars

this guide was thrown together as a more in depth way of getting avatars on jellyfin from my jellyfin-mods repo.. if you like this head there and maybe you will see some other things you like. 

![](https://user-images.githubusercontent.com/23018412/115957171-d65a0300-a4f8-11eb-8a8a-698e4620ea6d.PNG)
![](https://user-images.githubusercontent.com/23018412/115976186-3eddca00-a563-11eb-8597-81341924c750.PNG)

---

# installation
go to your web root (usually /usr/share/jellyfin/web) now run these commands

    sudo wget https://github.com/BobHasNoSoul/jellyfin-avatars/archive/refs/heads/main.zip
    sudo unzip main.zip

and now we need to edit the profile tab to enable the button :D 

    sudo nano user-profile-index-html.*.bundle.js

now replace the following string:

    <span>${DeleteImage}</span> </button>

with the following:

    <span>${DeleteImage}</span> </button> <button is="emby-buttoon" type="button" class="raised" id="btnMoreImages">><STYLE>A {text-decoration: none; color: #def3fb} </STYLE><span>${<a href="/web/jellyfin-avatars-main/avatars.html" target="_blank">More Images</a>}</span></button>

now you can just simply save this file and clear cache and reload in your client browser / app

all set :D
