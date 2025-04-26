<script lang="ts">
	import '../app.css';
	import { Navbar, Footer } from '$lib/components/core/';
	import { modal } from '$lib/shared/modals.svelte';
	import { ModalType } from '$lib/shared/modals.svelte';
	import MessageModal from '$lib/components/modals/MessageModal.svelte';
	import CreateChallengeModal from '$lib/components/modals/CreateChallengeModal.svelte';
	import CreateEventModal from '$lib/components/modals/CreateEventModal.svelte';

	let { children } = $props(); 
</script>

{#if modal.type !== ModalType.NONE}
	<div class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-8">
		{#if modal.type === ModalType.MESSAGE}
			<MessageModal message={modal.payload}/>
		{:else if modal.type === ModalType.CREATE_CHALLENGE}
			<CreateChallengeModal/>
		{:else if modal.type === ModalType.CREATE_EVENT}
			<CreateEventModal/>
		{/if}
	</div>
{/if}

<Navbar/>
{@render children()}
<Footer/>
