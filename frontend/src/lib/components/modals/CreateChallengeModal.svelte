<script lang="ts">
    import { modal } from '$lib/shared/modals.svelte';

    let title = $state('');
    let description = $state('');
    let startTime = $state();
    let endTime = $state();
    let workouts = $state();
    let loading = $state(false);
</script>

<div class="bg-white rounded shadow w-[800px] p-4 h-2/3">
    <div class="flex flex-col gap-y-3">
        <div class="flex justify-between items-center">
            <h3>Create Fitness Challenge</h3>
            <!-- svelte-ignore a11y_consider_explicit_label -->
            <button 
                class="p-2 text-gray-500 hover:text-gray-700 rounded-full hover:bg-gray-100"
                onclick={() => modal.close()}
            >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
            </button>
        </div>
        <hr/>
        <form class="flex flex-col gap-y-3">
            <div class="flex flex-col gap-y-1">
                <label for="title" class="text-sm">Title</label>
                <input class="input h-9"
                    type="text" 
                    id="title" 
                    bind:value={title} 
                    required 
                    disabled={loading}
                    placeholder="Challenge title"
                />
            </div>

            <div class="flex flex-col gap-y-1">
                <label for="description" class="text-sm">Description</label>
                <textarea class="input h-24 resize-none"
                    id="description" 
                    bind:value={description} 
                    required 
                    disabled={loading}
                    placeholder="Describe your challenge"
                ></textarea>
            </div>
            
            <div class="grid grid-cols-2 gap-x-4">
                <div class="flex flex-col gap-y-1">
                    <label for="startTime" class="text-sm">Start Time</label>
                    <input class="input h-9"
                        type="datetime-local" 
                        id="startTime" 
                        bind:value={startTime} 
                        required 
                        disabled={loading}
                    />
                </div>
                
                <div class="flex flex-col gap-y-1">
                    <label for="endTime" class="text-sm">End Time</label>
                    <input class="input h-9"
                        type="datetime-local" 
                        id="endTime" 
                        bind:value={endTime} 
                        required 
                        disabled={loading}
                    />
                </div>
            </div>

            <div class="flex flex-col gap-y-1">
                <label for="workouts" class="text-sm">Workouts</label>
                <select class="input h-9"
                    id="workouts" 
                    bind:value={workouts} 
                    multiple
                    disabled={loading}
                >
                    <option value="" disabled>Select workouts</option>
                    <!-- We'll populate this with workout options from the backend -->
                </select>
                <p class="text-xs text-gray-500 mt-1">Hold Ctrl/Cmd to select multiple workouts</p>
            </div>
            
            <div class="flex justify-end gap-x-3 mt-2">
                <button 
                    type="button"
                    class="px-4 py-2 text-gray-700 hover:bg-gray-100 rounded"
                    onclick={() => modal.close()}
                    disabled={loading}
                >
                    Cancel
                </button>
                <button 
                    type="submit"
                    class="px-4 py-2 bg-cyan-500 text-white rounded hover:bg-cyan-600"
                    disabled={loading}
                >
                    Create Challenge
                </button>
            </div>
        </form>
    </div>   
</div>