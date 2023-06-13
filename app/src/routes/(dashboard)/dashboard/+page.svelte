<script lang="ts">
    import DeleteIcon from '../../../components/icons/DeleteIcon.svelte'
    import PencilIcon from '../../../components/icons/PencilIcon.svelte'

    export let data

    console.log(data)
</script>

<section class="min-h-screen flex justify-center">
    <div class="bg-gradient-to-r from-sky-600 via-purple-500 to-pink-500 rounded-xl mb-[20px] mt-[200px] max-w-[1400px] min-w-[1400px] min-h-[720px]">
        <h1 class="text-center p-10 text-6xl text-white font-extrabold">Your Routines</h1>
        <div>
            {#each data.routines as routine, i}
                <article class="bg-white p-6 m-6 rounded-xl text-ellipsis flex justify-between">
                    <header >
                        <div class="flex items-center">
                            <h1 class="text-xl m-1 py-5">{routine.name}</h1>
                            <span class="bg-gray-700 px-6 m-3 py-2  rounded-lg text-white">{routine.label}</span>
                        </div>
                        <span>{routine.timestamps.replace('GMT', '')}</span>
                    </header>
                    <main class="flex items-center gap-4" >
                        <button class="h-16 w-16  bg-blue-600 rounded-lg flex justify-center items-center text-white text-xl">
                            <DeleteIcon />
                        </button>
                        <button class="h-16 w-16 rounded-lg bg-green-600 flex justify-center items-center text-center text-white text-xl">
                            <PencilIcon />
                        </button>
                    </main>
                    
                </article>
            {/each}
        </div>
    </div>
</section>