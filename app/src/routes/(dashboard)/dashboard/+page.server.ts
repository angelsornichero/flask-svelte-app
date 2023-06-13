import type { PageServerLoad } from './$types'
import { getRoutines } from '../../../services/RoutinesServices'

// eslint-disable-next-line
export const load: any = (async({ cookies }) => {
	const userCookie = cookies.get('sessionJWT')

	const { routines } = await getRoutines(userCookie as string)

	return {
		routines
	}

}) satisfies PageServerLoad
