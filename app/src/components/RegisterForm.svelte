<script lang="ts">
    import { register } from "../services/AuthServices"
    import { setCookie } from "../modules/cookies.svelte"

    async function handleSubmit(evt: SubmitEvent) {
        const formData = new FormData(evt.target as HTMLFormElement)
        const user = { 
            username: formData.get("username") as string, 
            email: formData.get("email") as string, 
            password: formData.get("username") as string, 
            repeat_password: formData.get("repeatPassword") as string 
        }
        const data = await register(user)
        console.log(data)
        setCookie('sessionJWT', data.token)
    }

</script>


<form on:submit|preventDefault={handleSubmit} class="opacity-90 flex flex-col h-[560px] w-[560px] rounded-xl bg-gradient-to-r from-sky-600 via-purple-500 to-pink-500">
    <h1 class="text-white text-6xl font-bold text-center p-6 border-b-2">Register</h1>
    <div class="flex flex-col gap-10">
        <div class="flex flex-col items-center m-auto p-6">
            <label class="text-white text-lg absolute z-10 right-[55%] bottom-[63.5%] bg-[#546DDF]" for="username">Username</label>
            <input name="username" class="bg-transparent border-2 rounded-lg absolute w-96 h-12 p-2 text-white border-white" id="username" type="text">
        </div>
        <div class="flex flex-col items-center m-auto p-6">
            <label class="text-white text-lg absolute z-10 right-[57%] bottom-[54%] bg-[#546DDF]" for="email">Email</label>
            <input name="email" class="bg-transparent border-2 rounded-lg absolute w-96 h-12 p-2 text-white border-white" id="email" type="text">
        </div>
        <div class="flex flex-col items-center m-auto p-6">
            <label class="text-white text-lg absolute z-10 right-[55%] bottom-[45%] bg-[#546DDF]" for="password">Password</label>
            <input name="password" class="bg-transparent border-2 rounded-lg absolute w-96 h-12 p-2 text-white border-white" id="password" type="password">
        </div>
        <div class="flex flex-col items-center m-auto p-6">
            <label class="text-white text-lg absolute z-10 right-[52%] bottom-[35.5%] bg-[#546DDF]" for="repeatPassword">Repeat password</label>
            <input name="repeatPassword" class="bg-transparent border-2 rounded-lg absolute w-96 h-12 p-2 text-white border-white" id="repeatPassword" type="password">
        </div>
    </div>
    <button class="mt-14  text-2xl border-2 p-4 mx-44 rounded-xl bg-gradient-to-r from-sky-600 via-purple-500 to-pink-500 text-white">Register</button>
</form>