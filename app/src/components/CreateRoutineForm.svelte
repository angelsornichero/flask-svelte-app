<script lang="ts">
    export let cookie: string
    $: string = cookie;

    import { createRoutine } from '../services/RoutinesServices.js'
    async function handleSubmit(evt: SubmitEvent) {
            const formData = new FormData(evt.target as HTMLFormElement)
            const routine = { 
                name: formData.get('name') as string,
                label: formData.get('label') as string,
            }
            const data = await createRoutine(cookie as string, routine)
            console.log(data)

            window.location.href = '/dashboard'

        }
</script>

<form on:submit|preventDefault={handleSubmit} class="opacity-90 flex flex-col h-[400px] w-[560px] rounded-xl bg-gradient-to-r from-sky-600 via-purple-500 to-pink-500">
    <h1 class="text-white text-6xl font-bold text-center p-6 border-b-2">New routine</h1>
    <div class="flex flex-col gap-10">
        <div class="flex flex-col items-center m-auto p-6">
            <label class="text-white text-lg absolute z-10 right-[53.4%] bottom-[55%] bg-[#546DDF]" for="username">Routine name</label>
            <input name="name" class="bg-transparent border-2 rounded-lg absolute w-96 h-12 p-2 text-white border-white" id="username" type="text">
        </div>
        <div class="flex flex-col items-center m-auto p-6">
            <label class="text-white text-lg absolute z-10 right-[57%] bottom-[46%] bg-[#546DDF]" for="email">Label</label>
            <input name="label" class="bg-transparent border-2 rounded-lg absolute w-96 h-12 p-2 text-white border-white" id="email" type="text">
        </div>
    </div>
    <button class="mt-14  text-2xl border-2 p-4 mx-44 rounded-xl bg-gradient-to-r from-sky-600 via-purple-500 to-pink-500 text-white">Create Routine</button>
</form>