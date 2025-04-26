<script lang="ts">
    import { FitnessChallengeCard } from "$lib/components/ui/";
    import { modal } from "$lib/shared/modals.svelte";
    import { ModalType } from "$lib/shared/modals.svelte";

    let { data } = $props();
    
    let myChallenges = $derived(data.myChallenges.results);
    let participatingChallenges = $derived(data.participatingChallenges.results);

    function handleCreateFitnessChallenge() {
        modal.setModal(ModalType.CREATE_CHALLENGE);
    }
</script>

<div class="flex flex-col gap-y-6">
    <div class="flex justify-between w-full items-center">
        <h2>Fitness Challenges</h2>
        <button onclick={handleCreateFitnessChallenge} class="btn-primary h-8">
            Create a Challenge
        </button>
    </div>
    <div class="flex flex-col gap-y-3">
        <h4>My Challenges</h4>
        {#if myChallenges && myChallenges.length > 0}
            {#each myChallenges as challenge}
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <FitnessChallengeCard fitnessChallenge={challenge} />
                </div>
            {/each}
        {:else}
            <p>You haven't created any fitness challenges yet</p>
        {/if}
    </div>
    <div class="flex flex-col gap-y-3">
        <h4>Participating Challenges</h4>
        {#if myChallenges && myChallenges.length > 0}
            {#each myChallenges as challenge}
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <FitnessChallengeCard fitnessChallenge={challenge} />
                </div>
            {/each}
        {:else}
            <p>You aren't apart of any challenges. Browse fun challenges <a href="/fitness-challenges" class="link">here</a></p>
        {/if}
        
    </div>
</div>