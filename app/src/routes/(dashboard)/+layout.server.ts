import type { LayoutServerLoad } from './$types'
import { decodeUsernameJWT } from '../../services/JWTService'
import { error } from '@sveltejs/kit'

// eslint-disable-next-line
export const load: any = (async({ cookies }) => {
	const userCookie = cookies.get('sessionJWT')

	const username = await decodeUsernameJWT(userCookie as string)

	if (!username) throw error(401, { message: 'Please login first' })

	return {
		username,
		userCookie
	}


}) satisfies LayoutServerLoad
