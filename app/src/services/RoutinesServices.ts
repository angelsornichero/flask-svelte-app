import { env } from '$env/dynamic/public'

export async function getRoutines(token: string) {
	const res = await fetch(env.PUBLIC_BASE_URL.concat('/routines'), {
		headers: {
			authorization: token
		}
	})

	const data = await res.json()

	return data

}
