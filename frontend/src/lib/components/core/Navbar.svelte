<script lang="ts">
    import { auth } from "$lib/shared/auth.svelte";

    console.log(auth);
</script>

<nav class="w-full fixed h-[56px] bg-white z-50">
    <div class="h-full w-full flex items-center justify-between px-20 shadow">
        <a href="/" class="font-bold text-xl">
            FitJacket
        </a>
        <div class="flex items-center gap-x-4 h-full">
            <div class="flex items-center gap-x-3">
                <a href="/workout-groups" class="nav-link">Workout Groups</a>
                <a href="/fitness-events" class="nav-link">Fitness Events</a>
                <a href="/dashboard" class="nav-link">Dashboard</a>
                <a href="/chat" class="nav-link">Chat</a>
            </div>
            <div class="h-8 w-[1px] bg-neutral-300"></div>
            {#if auth.token === ''}
                <div class="flex items-center gap-x-3">
                    <a href="/login" class="btn-primary h-8">Login</a>
                    <a href="/sign-up" class="btn-secondary h-8">Sign Up</a>
                </div>
            {:else}
                <div>{auth.user.username}</div>
            {/if}
            
        </div>
    </div>
</nav>