# jellyfin-avatars

updated 19.6.2025 

simple click and it updates (for some slow internet connections it may take a second for the update to finish so wait for the successful notification)

## installation guide

firstly `download the files in this repo`

you will have to put `monitoruserid.js` into your webroot 

your webroot will be in a standard location here are docker and ubuntu if you have changed the webroot i will assume you already know what you changed it to.

ubuntu and other linux bare metal - `/usr/share/jellyfin/web` 
docker official jellyfin image - `/jellyfin/jellyfin-web`

now you need to `copy the avatars folder into the webroot` 

now in your webroot `edit index.html` find `</body>` and just add the following ```<script defer src="monitoruserid.js"></script>``` and save and close it 

now we edit `user-userprofile.9cdbcbd8b4ed7a184e73.chunk.js` your uuid could be different here but the process is the same 

find ```className:"raised hide",title:"DeleteImage"}),```

replace it with 

```
className:"raised hide",title:"DeleteImage"}), (0, n.jsx)("a", {    href: "/web/avatars/index.html",    className: "raised button-submit",    style: { marginTop:"1em", display: "inline-block", textDecoration: "none", padding: "0.5em 1em", backgroundColor: "#007BFF", color:"#fff", borderRadius: "5px", textAlign: "center" },    children: "More Avatars"})]})]}),
```

now save and close it

you should now be all set to run the avatars library and enjoy the back button and the userid detection for admins to change the profile picture of other users without having to actually login as them.

## Screenshots
![Screenshot 2025-06-19 224440](https://github.com/user-attachments/assets/556038b3-2e3a-478b-b47e-5e509b13b66c)
![Screenshot 2025-06-19 224425](https://github.com/user-attachments/assets/6a536093-38c9-48a5-82dc-7dfc4141569c)
![Screenshot 2025-06-19 224402](https://github.com/user-attachments/assets/d3df3e95-a822-43b8-aa47-9f684f9d8147)
![Screenshot 2025-06-19 224350](https://github.com/user-attachments/assets/8ac0a68f-8065-4073-b3f3-bab83da7e746)
![Screenshot 2025-06-19 224336](https://github.com/user-attachments/assets/8e084712-a2d0-40cc-a00e-70c32c6c2dc9)
![Screenshot 2025-06-19 224326](https://github.com/user-attachments/assets/f3f536f3-c097-4292-8166-d541fecd14b1)
![Screenshot 2025-06-19 224306](https://github.com/user-attachments/assets/f5f16889-c9db-42cf-a734-489b15a15c0f)
![Screenshot 2025-06-19 224255](https://github.com/user-attachments/assets/8f7d83fd-6059-421b-9177-e95dea277fdf)
![Screenshot 2025-06-19 224246](https://github.com/user-attachments/assets/1830bc7c-93d4-48fb-b0b2-fbc51ae80183)
![Screenshot 2025-06-19 224236](https://github.com/user-attachments/assets/b0ea968f-8c94-4a75-96dd-b8d99e5d159f)
![Screenshot 2025-06-19 224222](https://github.com/user-attachments/assets/c22f4509-c0f9-4ad9-b52e-ebd1fe936285)
![Screenshot 2025-06-19 224210](https://github.com/user-attachments/assets/2d25987a-6f53-4c02-a31d-8ac25a150cc7)

