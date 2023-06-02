<script>
    import HomeIcon from "./icons/HomeIcons.svelte"
    import RegisterIcon from "./icons/RegisterIcon.svelte"
    import LoginIcon from "./icons/LoginIcon.svelte"
    import InfoIcon from "./icons/InfoIcon.svelte"
</script>

<header class="">
    <nav class=" text-xl fixed w-full flex justify-center">
        <ul class="shadow-2xl text-white w-8/12 bg-gradient-to-r from-sky-600 via-purple-500 to-pink-500 flex p-6 m-6 justify-around rounded-xl">
            <li>
                <a class="flex gap-1" href="/"><HomeIcon />Home</a>
            </li>
            <li>
                <a class="flex gap-1" href="/register"><RegisterIcon /> Register</a>
            </li>
            <li>
                <a class="flex gap-1" href="/login"><LoginIcon /> Login</a>
            </li>
            <li>
                <a class="flex gap-1" href="/#info"><InfoIcon /> Info</a>
            </li>
        </ul>
    </nav>
</header>

