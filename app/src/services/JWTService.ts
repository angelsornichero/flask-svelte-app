import jwt from 'jsonwebtoken'
import { env } from '$env/dynamic/private'

export async function decodeUsernameJWT(token: string) {
	try {
		const { username } = await jwt.verify(token as string, env.JWT_SECRET) as jwt.JwtPayload
		return username
	} catch {
		return false
	}

}
