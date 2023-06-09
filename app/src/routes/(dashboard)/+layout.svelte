<script>
    import "../../app.css"
    import AuthorizedHeader from "../../components/AuthorizedHeader.svelte";
    import Footer from "../../components/Footer.svelte"

    export let data
</script>

<AuthorizedHeader username={data.username} />
<main>
    <slot />
</main>
<Footer />