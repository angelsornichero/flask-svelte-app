<script context="module" lang="ts">
    // GET COOKIE
    export function getCookie(name: string) {
        let cookieName = name + "=";
        let decodedCookie = decodeURIComponent(document.cookie);
        let ca = decodedCookie.split(';');
        for(let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(cookieName) == 0) {
                return c.substring(cookieName.length, c.length);
            }
        }
        return "";
    }

    // SET COOKIE
    export function setCookie(name: string, value: string) {
        document.cookie = name + "=" + value + ";" + ";path=/";
    }

    // DELETE COOKIE
    export function deleteCookie(name: string) {
        document.cookie = name + '=; Max-Age=-99999999;'; 
    }
</script>