<script lang="ts">
    import { heroImage } from "$lib/assets";
</script>

<section>
    <div class="w-full h-[100vh]">
        <div class="h-full w-full items-center justify-between z-10 absolute flex px-40">
            <div class="flex flex-col gap-y-8 w-1/2 items-start">
                <div class="flex flex-col gap-y-4">
                    <h1>Be the Best You With <span class="text-cyan-300">FitJacket</span></h1>
                    <p class="text-[15px] pr-[20%]">Your personal fitness journey starts here and now. FitJacket is an all-in-one fitness solution aimed to keep you motivated with a wide range of features from ways to track and visualize your progress to a built-in social media platform for you to connect with like-minded fitness enthusiasts. </p>
                </div>
                <div class="flex items-center gap-x-4 justify-center z-50">
                    <a href="/signup" class="btn-primary h-10 text-base px-4">
                        Get Started Free
                    </a>
                    <a href="/features" class="btn-secondary h-10 text-base px-4">
                        Learn More
                    </a>
                </div>
            </div>
            <div class="w-1/2 h-2/3 -z-10 relative rounded-xl overflow-hidden">
                <div class="absolute inset-0 bg-black/50 -z-10"></div>
                <img class="-z-20 object-cover h-full w-full absolute" src={heroImage} alt="hero"/>
            </div>
            
        </div>
    </div>

</section>
