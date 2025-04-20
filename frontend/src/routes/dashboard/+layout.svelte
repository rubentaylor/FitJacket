<script lang="ts">
    import { auth } from "$lib/shared/auth.svelte";
	import { Sidebar } from "$lib/components/ui/";
    
    let { children } = $props();
</script>

<section>
    <div class="h-[100vh] flex w-full">
        <Sidebar username={auth.user.username} email={auth.user.email}/>
        <div class="h-full pt-[calc(56px+24px)] pb-6 px-6 w-[calc(100%-256px)]">
            {@render children()}
        </div>
    </div>
</section>