import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { BACKEND_URL } from '$env/static/private';

export const load: PageServerLoad = async ({ fetch, cookies }) => {
	const userId = cookies.get('user_id');

	const fitnessChallengeResponse = await fetch(
		`${BACKEND_URL}/api/fitness-challenges/user/${userId}`
	);

	if (!fitnessChallengeResponse.ok) {
		error(502, 'Fitness challenges not found');
	}

	const allChallenges = await fitnessChallengeResponse.json();

	const myChallenges = allChallenges.results.filter(
		(challenge: any) => challenge.user.toString() === userId
	);

	const participatingChallenges = allChallenges.results.filter(
		(challenge: any) =>
			challenge.user.toString() !== userId &&
			challenge.participants.some((participant: number) => participant.toString() === userId)
	);

	return {
		myChallenges: {
			count: myChallenges.length,
			results: myChallenges
		},
		participatingChallenges: {
			count: participatingChallenges.length,
			results: participatingChallenges
		}
	};
};
