<script lang="ts">
    import { auth } from '$lib/shared/auth.svelte';
    
    let username = $state(auth.user?.username || '');
    let email = $state(auth.user?.email || '');
    let isProfilePrivate = $state(auth.user?.is_private || false);
    let loadingGeneral = $state(false);
    
    let currentPassword = $state('');
    let newPassword = $state('');
    let confirmPassword = $state('');
    let loadingPassword = $state(false);

    let passwordErrorMsg = $state('');
    
    async function updateGeneralSettings() {
        loadingGeneral = true;
        
        try {
            const response = await fetch('/dashboard/settings/', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username,
                    email,
                    is_private: isProfilePrivate
                })
            });
            
            if (!response.ok) {
                throw new Error('Failed to update general settings');
            }

            const { data } = await response.json();

            auth.setUser(data.email, username, data.id);
        } catch (err) {
            console.error(err);
        } finally {
            loadingGeneral = false;
        }
    }
    
    async function updatePassword() {
        loadingPassword = true;
        passwordErrorMsg = '';
        
        try {
            const response = await fetch('/dashboard/settings/', {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    current_password: currentPassword,
                    new_password: newPassword || null
                })
            });

            if (!response.ok) {
                throw new Error('Failed to update password');
            }
        } catch (err) {
            console.error(err);
            passwordErrorMsg = 'An error occurred while updating the password. Please try again.';
        } finally {
            currentPassword = '';
            newPassword = '';
            confirmPassword = '';

            loadingPassword = false;
        }
    }
</script>

<div class="flex flex-col gap-y-6 h-full">
    <h2>Settings</h2>
    <div class="flex justify-between gap-6 w-full h-full">
        <div class="w-1/2 flex flex-col gap-6">
            <h4 class="-my-2">Change Settings</h4>
            <div class="p-4 bg-white shadow rounded">
                <form onsubmit={updateGeneralSettings} class="flex flex-col gap-y-4">
                    <div class="flex flex-col gap-y-1">
                        <label for="username" class="text-sm">Username</label>
                        <input 
                            type="text" 
                            id="username" 
                            bind:value={username} 
                            required
                            disabled={loadingGeneral}
                            class="input h-9"
                        />
                    </div>
                    
                    <div class="flex flex-col gap-y-1">
                        <label for="email" class="text-sm">Email</label>
                        <input 
                            type="email" 
                            id="email" 
                            bind:value={email} 
                            required
                            disabled={loadingGeneral}
                            class="input h-9"
                        />
                    </div>
                    
                    <div class="flex items-center gap-x-2 mt-2">
                        <input 
                            type="checkbox" 
                            id="isPrivate"
                            bind:checked={isProfilePrivate}
                            disabled={loadingGeneral}
                            class="h-4 w-4"
                        />
                        <label for="isPrivate" class="text-sm">Private</label>
                    </div>
                    
                    <button 
                        type="submit" 
                        disabled={loadingGeneral || !username || !email}
                        class="btn-primary h-8"
                    >
                        Update Profile
                    </button>
                </form>
            </div>
            <h4 class="-my-2">Change Password</h4>
            <div class="p-4 bg-white shadow rounded">
                {#if passwordErrorMsg}
                    <div class="text-red-500 mb-2">{passwordErrorMsg}</div>
                {/if}
                <form onsubmit={updatePassword} class="flex flex-col gap-y-4">
                    <div class="flex flex-col gap-y-1">
                        <label for="currentPassword" class="text-sm">Current Password</label>
                        <input 
                            type="password" 
                            id="currentPassword" 
                            bind:value={currentPassword}
                            required
                            disabled={loadingPassword}
                            class="input h-9"
                        />
                    </div>
                    
                    <div class="flex flex-col gap-y-1">
                        <label for="newPassword" class="text-sm">New Password</label>
                        <input 
                            type="password" 
                            id="newPassword" 
                            bind:value={newPassword}
                            required
                            minlength="8"
                            disabled={loadingPassword}
                            class="input h-9"
                        />
                    </div>
                    
                    <div class="flex flex-col gap-y-1">
                        <label for="confirmPassword" class="text-sm">Confirm New Password</label>
                        <input 
                            type="password" 
                            id="confirmPassword" 
                            bind:value={confirmPassword}
                            required
                            minlength="8"
                            disabled={loadingPassword}
                            class="input h-9"
                        />
                    </div>
                    
                    <button 
                        type="submit" 
                        disabled={loadingPassword || !newPassword || !confirmPassword || !currentPassword || newPassword !== confirmPassword}
                        class="btn-primary h-8"
                    >
                        Change Password
                    </button>
                </form>
            </div>
        </div>
        
    </div>
</div>