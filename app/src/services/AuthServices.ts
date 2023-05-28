import { env } from '$env/dynamic/public'

interface RegisterParams {
    username: string,
    password: string,
    repeat_password: string,
    email: string
}

export async function register(user: RegisterParams) {
	const res = await fetch(env.PUBLIC_BASE_URL.concat('/register'),
		{
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(user)
		}
	)

	const data = await res.json()

	return data
}
