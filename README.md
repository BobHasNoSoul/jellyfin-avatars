# jellyfin-avatars
adds a html page and a button to jellyfin 10.8.x for users to get more avatars

this guide was thrown together as a more in depth way of getting avatars on jellyfin from my jellyfin-mods repo.. if you like this head there and maybe you will see some other things you like. 

![Screenshot 2024-02-19 215300](https://github.com/BobHasNoSoul/jellyfin-avatars/assets/23018412/e641792f-f408-4834-a5b1-c77d5e9a17d4)

![Screenshot 2024-02-19 215204](https://github.com/BobHasNoSoul/jellyfin-avatars/assets/23018412/339d0f5b-ca10-4a47-9fce-baf6345cf465)

![screencapture-blueboxofdoom-uk-web-avatars-pop-pop-html-2024-02-22-17_15_21](https://github.com/BobHasNoSoul/jellyfin-mods/assets/23018412/b62a4881-634c-4c42-9a47-ffe4eb0a69a7)

![screencapture-blueboxofdoom-uk-web-avatars-Steam-gallery-html-2024-02-22-17_16_00](https://github.com/BobHasNoSoul/jellyfin-mods/assets/23018412/703b7a00-7884-4c84-82c6-b9946ae71c11)

![screencapture-blueboxofdoom-uk-web-avatars-360-360-html-2024-02-22-17_18_58](https://github.com/BobHasNoSoul/jellyfin-mods/assets/23018412/7c483249-2d51-4eb9-9857-08a82a9df69b)

![screencapture-blueboxofdoom-uk-web-avatars-nf-nf-html-2024-02-22-17_20_00](https://github.com/BobHasNoSoul/jellyfin-mods/assets/23018412/49dca657-cf1b-4c67-8c9f-2ecce64985a6)

![screencapture-blueboxofdoom-uk-web-avatars-one-one-html-2024-02-22-17_20_40](https://github.com/BobHasNoSoul/jellyfin-mods/assets/23018412/2da96360-73f8-4774-8fd5-d14f5c3c1def)

![screencapture-blueboxofdoom-uk-web-avatars-playstation-playstation-html-2024-02-22-17_21_07](https://github.com/BobHasNoSoul/jellyfin-mods/assets/23018412/cc71e8ca-18c7-4fd0-b618-92ca2f261606)

![screencapture-blueboxofdoom-uk-web-avatars-playstation-playstation-html-2024-02-22-17_21_07](https://github.com/BobHasNoSoul/jellyfin-mods/assets/23018412/0510732b-debc-4c70-92ee-28ac498fc052)

![screencapture-blueboxofdoom-uk-web-avatars-ps2-index-html-2024-02-22-17_22_02](https://github.com/BobHasNoSoul/jellyfin-mods/assets/23018412/c0c3f357-1aa2-4b7f-b6d5-9d7089c8b4e0)

OH NO A MASSIVE UPDATE AND RECODE WAS MADE 19/2/24 

this works on 10.8.13 and all 10.8 variants

however this creates a bigger avatar library covering steam, playstation, xbox one, xbox 360, netflix, PS2 and a new good pop culture animated section. and yes the link is now to /web/avatars/index.html 

---

# installation
go to your web root (usually `/usr/share/jellyfin/web`) now run these commands

put the avatars dir into the web root 

and now we need to edit the profile tab to enable the button :D 

    `sudo nano UserProfilePage.*.chunk.js`

now find the following string:

    `"raised btnDeleteImage hide",title:"DeleteImage"})`

now after that string you add a `,` so it becomes `"raised btnDeleteImage hide",title:"DeleteImage"}),`

and hit enter to create a new line and enter again so you create a blank line 

then insert the following on the blank line

````
(0, n.jsx)("a", {
    href: "/web/avatars/index.html",
    target: "_blank",
    style: {
        display: "inline-block",
        padding: "0.9em 1em",
        backgroundColor: "#00a4dc",
        color: "#fff",
        border: "0",
        textDecoration: "none",
        borderRadius: "0.2em",
        boxSizing: "border-box", // Changed from box-sizing to boxSizing
        lineHeight: "1.35",      // Changed from line-height to lineHeight
        boxShadow: "0px 2px 5px rgba(0, 0, 0, 0.2)",
        transition: "background-color 0.3s ease",
        cursor: "pointer"
    },
    children: "More Avatars"
})
````
so the final section is bellow the segment above and that should be 

`]}))]})),(0,n.jsx)(f.Z,{userId:t})]}))}))}}}]);`

now you can just simply save this file and clear cache and reload in your client browser / app

all set :D reloaded and boom done for 2024
