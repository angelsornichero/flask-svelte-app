import { env } from '$env/dynamic/public'

interface CreateRoutine {
	name: string,
	label: string
}

export async function getRoutines(token: string) {
	const res = await fetch(env.PUBLIC_BASE_URL.concat('/routines'), {
		headers: {
			authorization: token
		}
	})

	const data = await res.json()

	return data

}


export async function createRoutine(token: string, routine: CreateRoutine) {
	const res = await fetch(env.PUBLIC_BASE_URL.concat('/new-routine'), {
		method: 'POST',
		body: JSON.stringify(routine),
		headers: {
			authorization: token,
			'Content-Type': 'application/json'
		}
	})

	const data = await res.json()
	console.log(routine)
	return data
}
