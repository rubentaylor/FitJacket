<script lang="ts">
    import { auth } from "$lib/shared/auth.svelte";
</script>

<div class="flex flex-col gap-y-6">
    <h2>Hello, {auth.user.username} 👋</h2>
</div>