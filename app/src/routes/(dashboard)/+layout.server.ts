import type { LayoutServerLoad } from './$types'
import jwt from 'jsonwebtoken'
import { env } from '$env/dynamic/private'

export const load = (async({ cookies }: any) => {
	const userCookie = cookies.get('sessionJWT')

	const { username } = jwt.verify(userCookie, env.JWT_SECRET) as jwt.JwtPayload

	return {
		username
	}
}) satisfies LayoutServerLoad
