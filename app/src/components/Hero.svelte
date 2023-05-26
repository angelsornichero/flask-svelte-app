<script>
    import DumbellIcon from "./icons/DumbellIcon.svelte"
    import RunningIcon from "./icons/RunningIcon.svelte"
</script>
 
<section class="min-h-screen bg-gradient-to-r from-sky-600 via-purple-500 to-pink-500 flex items-center justify-center">
    <DumbellIcon />
    <RunningIcon />
    <slot />
</section>