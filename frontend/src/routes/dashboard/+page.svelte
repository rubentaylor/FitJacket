<script lang="ts">
    import { auth } from "$lib/shared/auth.svelte";
</script>

<div>
    <h2>Hello, {auth.user.username} 👋</h2>
</div>