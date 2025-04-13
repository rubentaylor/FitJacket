<script lang="ts">
	import '../app.css';
	import { Navbar, Footer } from '$lib/components/core/';
	let { children } = $props(); 
</script>

<Navbar/>
{@render children()}
<Footer/>
