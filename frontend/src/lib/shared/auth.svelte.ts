import { browser } from '$app/environment';

const defaultAuth = {
	user: {
		username: '',
		email: ''
	},
	token: ''
};

export let auth = $state({
	...(browser
		? JSON.parse(localStorage.getItem('auth') || JSON.stringify(defaultAuth))
		: defaultAuth),

	setToken(token: string) {
		this.token = token;
	},

	setUser(email: string, username: string) {
		this.user.email = email;
		this.user.username = username;
	},

	clearAuth() {
		this.token = '';
		this.user.username = '';
		this.user.email = '';
	}
});

$effect.root(() => {
	$effect(() => {
		if (browser) {
			localStorage.setItem('auth', JSON.stringify(auth));
		}
	});
});
