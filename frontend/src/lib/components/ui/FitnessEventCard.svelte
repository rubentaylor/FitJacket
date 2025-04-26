<script lang="ts">
    let { fitnessEvent } = $props();
</script>

<button class="w-full rounded-lg bg-white shadow py-4 px-5 hover:shadow-lg duration-300 flex flex-col items-start gap-y-2">
    <div class="flex flex-col">
        <div class="flex gap-x-2">
            <span class="text-cyan-500 font-bold text-sm">
                {fitnessEvent.participants.length} 
                {#if fitnessEvent.participants.length > 1}
                    Participants
                {:else}
                    Participant
                {/if}
            </span>
        </div>
        <h4>{fitnessEvent.title}</h4>
    </div>
    <p>
        {fitnessEvent.description}
    </p>
    <hr class="my-2"/>
    <div class="flex flex-col gap-y-1">
        <div class="flex items-center gap-x-1.5 text-sm">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mt-0.5 text-neutral-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span class="text-gray-600">
                {new Date(fitnessEvent.start_time).toLocaleDateString('en-US', {weekday: 'short', month: 'short', day: 'numeric'})}
                •
                {new Date(fitnessEvent.start_time).toLocaleTimeString('en-US', {hour: '2-digit', minute:'2-digit'})} - 
                {new Date(fitnessEvent.end_time).toLocaleTimeString('en-US', {hour: '2-digit', minute:'2-digit'})}
            </span>
        </div>
        <div class="flex items-center gap-x-1.5 text-sm">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mt-0.5 text-neutral-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            <span class="text-gray-600">
                {fitnessEvent.location || 'Virtual'}
            </span>
        </div>
    </div>
</button>