# jellyfin-avatars

keyupdate: it no longer needs the user to download the image and manually add it, it just updates the current users image with a simple tap or click

adds a html page and a button to jellyfin 10.9.x and higher for users to get more avatars

this guide was thrown together as a more in depth way of getting avatars on jellyfin from my jellyfin-mods repo.. if you like this head there and maybe you will see some other things you like. 

![](https://user-images.githubusercontent.com/23018412/115957171-d65a0300-a4f8-11eb-8a8a-698e4620ea6d.PNG)
![](https://user-images.githubusercontent.com/23018412/115976186-3eddca00-a563-11eb-8597-81341924c750.PNG)

Thanks NetfreaksShadow for the extra packs of avatars

---

# installation
go to your web root (usually /usr/share/jellyfin/web) now run these commands

    sudo wget https://github.com/BobHasNoSoul/jellyfin-avatars/archive/refs/heads/main.zip
    sudo unzip main.zip
    sudo mv jellyfin-avatars-main/avatars ./avatars

and now we need to edit the profile tab to enable the button :D 

    sudo nano user-userprofile.5*.js

now replace the entire files content with the following

    "use strict";(self.webpackChunk=self.webpackChunk||[]).push([[16325,96084],{55858:function(e,r,t){t.r(r);var a=t(62540),i=t(64680),n=t(63696),o=t(9055),l=t(89100),s=t(9482),c=t(73233),d=t(22622),u=t(40532),g=t(76165),m=t(41600),f=t(56869),y=t(50764),p=t(7397),h=function(e,r){var t="function"==typeof Symbol&&e[Symbol.iterator];if(!t)return e;var a,i,n=t.call(e),o=[];try{for(;(void 0===r||r-- >0)&&!(a=n.next()).done;)o.push(a.value)}catch(e){i={error:e}}finally{try{a&&!a.done&&(t=n.return)&&t.call(n)}finally{if(i)throw i.error}}return o};r.default=function(){var e=h((0,o.ok)(),1)[0].get("userId"),r=h((0,n.useState)(""),2),t=r[0],v=r[1],A=(0,n.useRef)(null),b=(0,n.useCallback)((function(){var r=A.current;r?e?(f.Ay.show(),window.ApiClient.getUser(e).then((function(e){if(!e.Name||!e.Id)throw new Error("Unexpected null user name or id");v(e.Name),c.default.setTitle(e.Name);var t="assets/img/avatar.png";e.PrimaryImageTag&&(t=window.ApiClient.getUserImageUrl(e.Id,{tag:e.PrimaryImageTag,type:"Primary"})),r.querySelector("#image").style.backgroundImage="url("+t+")",l.default.getCurrentUser().then((function(t){var a;if(!e.Policy)throw new Error("Unexpected null user.Policy");e.PrimaryImageTag?(r.querySelector("#btnAddImage").classList.add("hide"),r.querySelector("#btnDeleteImage").classList.remove("hide")):d.g.supports("fileinput")&&((null===(a=null==t?void 0:t.Policy)||void 0===a?void 0:a.IsAdministrator)||e.Policy.EnableUserPreferenceAccess)&&(r.querySelector("#btnDeleteImage").classList.add("hide"),r.querySelector("#btnAddImage").classList.remove("hide"))})).catch((function(e){console.error("[userprofile] failed to get current user",e)})),f.Ay.hide()})).catch((function(e){console.error("[userprofile] failed to load data",e)}))):console.error("[userprofile] missing user id"):console.error("[userprofile] Unexpected null page reference")}),[e]);return(0,n.useEffect)((function(){var r=A.current;if(r){b();var t=function(e){var r,t;switch(f.Ay.hide(),null===(t=null===(r=e.target)||void 0===r?void 0:r.error)||void 0===t?void 0:t.code){case DOMException.NOT_FOUND_ERR:(0,y.A)(s.Ay.translate("FileNotFound"));break;case DOMException.ABORT_ERR:a();break;default:(0,y.A)(s.Ay.translate("FileReadError"))}},a=function(){f.Ay.hide(),(0,y.A)(s.Ay.translate("FileReadCancelled"))};r.querySelector("#btnDeleteImage").addEventListener("click",(function(){e?(0,u.A)(s.Ay.translate("DeleteImageConfirmation"),s.Ay.translate("DeleteImage")).then((function(){f.Ay.show(),window.ApiClient.deleteUserImage(e,i.y.Primary).then((function(){f.Ay.hide(),b()})).catch((function(e){console.error("[userprofile] failed to delete image",e)}))})).catch((function(){})):console.error("[userprofile] missing user id")})),r.querySelector("#btnAddImage").addEventListener("click",(function(){var e=r.querySelector("#uploadImage");e.value="",e.click()})),r.querySelector("#uploadImage").addEventListener("change",(function(n){!function(n){var o=r.querySelector("#image"),l=n.target.files[0];if(!l||!/image.*/.exec(l.type))return!1;var s=new FileReader;s.onerror=t,s.onabort=a,s.onload=function(){e?(o.style.backgroundImage="url("+s.result+")",window.ApiClient.uploadUserImage(e,i.y.Primary,l).then((function(){f.Ay.hide(),b()})).catch((function(e){console.error("[userprofile] failed to upload image",e)}))):console.error("[userprofile] missing user id")},s.readAsDataURL(l)}(n)}));
    
            var btnMoreAvatars = document.createElement("button");
            btnMoreAvatars.id = "btnMoreAvatars";
            btnMoreAvatars.className = "raised emby-button"; // Match the style of Delete Image button
            btnMoreAvatars.innerHTML = s.Ay.translate("More Avatars");
            btnMoreAvatars.addEventListener("click", function() {
                window.location.href = "/web/avatars/index.html";
            });

            var btnDeleteImage = r.querySelector("#btnDeleteImage");
            if (btnDeleteImage && btnDeleteImage.parentNode) {
                btnDeleteImage.parentNode.insertBefore(btnMoreAvatars, btnDeleteImage.nextSibling);
            }
        } else console.error("[userprofile] Unexpected null page reference")}),[b,e]),(0,a.jsx)(p.A,{id:"userProfilePage",title:s.Ay.translate("Profile"),className:"mainAnimatedPage libraryPage userPreferencesPage userPasswordPage noSecondaryNavPage",children:(0,a.jsxs)("div",{ref:A,className:"padded-left padded-right padded-bottom-page",children:[(0,a.jsxs)("div",{className:"readOnlyContent",style:{margin:"0 auto",marginBottom:"1.8em",padding:"0 1em",display:"flex",flexDirection:"row",alignItems:"center"},children:[(0,a.jsxs)("div",{className:"imagePlaceHolder",style:{position:"relative",display:"inline-block",maxWidth:200},children:[(0,a.jsx)("input",{id:"uploadImage",type:"file",accept:"image/*",style:{position:"absolute",right:0,width:"100%",height:"100%",opacity:0,cursor:"pointer"}}),(0,a.jsx)("div",{id:"image",style:{width:200,height:200,backgroundRepeat:"no-repeat",backgroundPosition:"center",borderRadius:"100%",backgroundSize:"cover"}})]}),(0,a.jsxs)("div",{style:{verticalAlign:"top",margin:"1em 2em",display:"flex",flexDirection:"column",alignItems:"center"},children:[(0,a.jsx)("h2",{className:"username",style:{margin:0,fontSize:"xx-large"},children:t}),(0,a.jsx)("br",{}),(0,a.jsx)(g.A,{type:"button",id:"btnAddImage",className:"raised emby-button hide",title:"ButtonAddImage"}),(0,a.jsx)(g.A,{type:"button",id:"btnDeleteImage",className:"raised emby-button hide",title:"DeleteImage"})]})]}),(0,a.jsx)(m.A,{userId:e})]})})}}}]);

now you can just simply save this file 

one extra edit is needed to make this work (or you will get an api error)

simply edit `index.html` and add find and replace `</body></html>` with 

```
<script>
// Function to save credentials to sessionStorage
function saveCredentialsToSessionStorage(credentials) {
  try {
    // Store the credentials in sessionStorage
    sessionStorage.setItem('json-credentials', JSON.stringify(credentials));
    console.log('Credentials saved to sessionStorage.');
  } catch (error) {
    console.error('Error saving credentials:', error);
  }
}

// Function to save the API key to sessionStorage
function saveApiKey(apiKey) {
  try {
    sessionStorage.setItem('api-key', apiKey);
    console.log('API key saved to sessionStorage.');
  } catch (error) {
    console.error('Error saving API key:', error);
  }
}

// Override the default console.log function
(function() {
  var originalConsoleLog = console.log;

  console.log = function(message) {
    // Call the original console.log method
    originalConsoleLog.apply(console, arguments);

    // Check if the message contains the JSON credentials
    if (typeof message === 'string' && message.startsWith('Stored JSON credentials:')) {
      try {
        // Extract the JSON credentials from the message
        var jsonString = message.substring('Stored JSON credentials: '.length);
        var credentials = JSON.parse(jsonString);

        // Save the credentials to sessionStorage
        saveCredentialsToSessionStorage(credentials);
      } catch (error) {
        console.error('Error parsing credentials:', error);
      }
    }

    // Check if the message contains the WebSocket URL with api_key
    if (typeof message === 'string' && message.startsWith('opening web socket with url:')) {
      try {
        // Extract the API key from the message
        var url = message.split('url:')[1].trim();
        var urlParams = new URL(url).searchParams;
        var apiKey = urlParams.get('api_key');

        if (apiKey) {
          saveApiKey(apiKey);
        }
      } catch (error) {
        console.error('Error extracting API key:', error);
      }
    }
  };
})();
</script>
</body></html>
```

now save the file and clear cache and reload in your client browser / app

all set :D
