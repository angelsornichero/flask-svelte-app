<script lang="ts">
    import CreateRoutineForm from '../../../components/CreateRoutineForm.svelte';

    export let data

    const cookie = data.userCookie as string
    

</script>

<section class="min-h-screen flex justify-center items-center">
    <CreateRoutineForm cookie={cookie} />
</section>