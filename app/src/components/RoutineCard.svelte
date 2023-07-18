<script lang="ts">

    import DeleteIcon from './icons/DeleteIcon.svelte'
    import PencilIcon from './icons/PencilIcon.svelte'

    interface Routine {
        name: string,
        label: string,
        timestamps: string,
        user: string,
        id: number
    }
    export let routine: Routine
    $: Routine  = routine;
</script>

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
            <PencilIcon />
        </button>
        <button class="h-16 w-16 rounded-lg bg-red-600 flex justify-center items-center text-center text-white text-xl">
            <DeleteIcon />
        </button>
    </main>
    
</article>