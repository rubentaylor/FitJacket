<script lang="ts">
    let { fitnessChallenge } = $props();
    
    function calcDuration(start: string, end: string): string {
        const startTime = new Date(start);
        const endTime = new Date(end);
        const durationMs = endTime.getTime() - startTime.getTime();
        const minutes = Math.floor(durationMs / 60000);
        
        if (minutes < 60) {
            return `${minutes} min`;
        } else {
            const hours = Math.floor(minutes / 60);
            const remainingMinutes = minutes % 60;
            return remainingMinutes > 0 ? 
                `${hours}h ${remainingMinutes}m` : 
                `${hours}h`;
        }
    }
</script>

<button class="w-full rounded-lg bg-white shadow py-4 px-5 hover:shadow-lg duration-300 flex flex-col items-start gap-y-2">
    <div class="flex flex-col">
        <div class="flex gap-x-2">
            <span class="text-cyan-500 font-bold text-sm">
                {fitnessChallenge.participants.length} 
                {#if fitnessChallenge.participants.length > 1}
                    Participants
                {:else}
                    Participant
                {/if}
            </span>
        </div>
        <h4>{fitnessChallenge.title}</h4>
    </div>
    <p>
        {fitnessChallenge.description}
    </p>
    {#if false}
        <hr class="my-2"/>
        <div class="flex flex-col gap-y-1">
            <h6>Workouts</h6>
            {#each fitnessChallenge.workouts as workout}
                <div class="text-sm text-gray-700 flex justify-between">
                    <span>• {workout.title}</span>
                    <span class="text-gray-500">{calcDuration(workout.start_time, workout.end_time)}</span>
                </div>
            {/each}
        </div>
    {/if}
    <hr class="my-2"/>
    <div class="flex items-center gap-x-1.5 text-sm">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mt-0.5 text-neutral-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span class="text-gray-600">
            {new Date(fitnessChallenge.start_time).toLocaleDateString('en-US', {weekday: 'short', month: 'short', day: 'numeric'})}
            •
            {new Date(fitnessChallenge.start_time).toLocaleTimeString('en-US', {hour: '2-digit', minute:'2-digit'})} - 
            {new Date(fitnessChallenge.end_time).toLocaleTimeString('en-US', {hour: '2-digit', minute:'2-digit'})}
        </span>
    </div>
</button>