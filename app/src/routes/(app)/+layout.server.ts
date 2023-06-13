import type { LayoutServerLoad } from './$types'
import { decodeUsernameJWT } from '../../services/JWTService'
import { redirect } from '@sveltejs/kit'

// eslint-disable-next-line
export const load: any = (async({ cookies }) => {
	const userCookie = cookies.get('sessionJWT')

	const username = await decodeUsernameJWT(userCookie as string)

	if (username) throw redirect(301, '/dashboard')

	return

}) satisfies LayoutServerLoad
