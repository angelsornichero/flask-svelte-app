<script lang="ts">
    export let username: string;
    $: string = username;
    import HomeIcon from "./icons/HomeIcons.svelte"
    import LoginIcon from "./icons/LoginIcon.svelte"
    import RoutineIcon from "./icons/RoutineIcon.svelte"
    import UserIcon from "./icons/userIcon.svelte";
    import { deleteCookie } from "../modules/cookies.svelte"

    function deleteUserCookie () {
        deleteCookie('sessionJWT')
        window.location.href = '/';
    }
</script> 

<header class="">
    <nav class=" text-xl fixed w-full flex justify-center">
        <ul class="shadow-2xl text-white w-8/12 bg-gradient-to-r from-sky-600 via-purple-500 to-pink-500 flex p-6 m-6 justify-around rounded-xl">
            <li>
                <a class="flex gap-1" href="/dashboard"><HomeIcon />Dashboard</a>
            </li>
            <li>
                <a class="flex gap-1" href="/new-routine"><RoutineIcon />New routine</a>
            </li>
            <li>
                <button class="flex gap-1" on:click={deleteUserCookie}><LoginIcon /> Logout</button>
            </li>
            <li>
                <span class="flex gap-1"><UserIcon />{username}</span>
            </li>
        </ul>
    </nav>
</header>