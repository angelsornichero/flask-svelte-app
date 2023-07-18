<script lang="ts">
    import RoutineCard from '../../../components/RoutineCard.svelte';


    export let data

</script>

<section class="min-h-screen flex justify-center">
    <div class="bg-gradient-to-r from-sky-600 via-purple-500 to-pink-500 rounded-xl mb-[20px] mt-[200px] max-w-[1400px] min-w-[1400px] min-h-[720px]">
        <h1 class="text-center p-10 text-6xl text-white font-extrabold">Your Routines</h1>
        <div>
            {#each data.routines as routine}
                <RoutineCard routine={routine} />
            {/each}
        </div>
    </div>
</section>