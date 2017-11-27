import json
import config
from sdk import services


campaigns, jobs, tasks, results = services.get(config)

# Create a campaign
zenCampaign = campaigns.create({
    "name": "My zen campaign",
    "title": "Zen campaign",
    "estDuration": "30 seconds",
    "workerPayment": 0.1,
    "results": 100,
})

# Add jobs to the campaign
koanJob = jobs.create({"name": "Solve koans"})
meditationJob = jobs.create({"name": "Meditate"})
campaigns.add_jobs(zenCampaign, [koanJob, meditationJob])

# Add tasks to koan job
oneHandClappingTask = tasks.create({
    "name": "One hand clapping",
    "components": [
        {
            "type": "Text",
            "style": "Instruction",
            "text": "Record the sound of one hand clapping.",
        }, {
            "type": "AudioRecording",
            "minDurationInSeconds": 3,
            "maxDurationInSeconds": 9,
        }
    ]
})

buddhaNatureTask = tasks.create({
    "name": "Buddha nature",
    "components": [
        {
            "type": "Text",
            "style": "Question",
            "text": "Does a dog have Buddha nature or not?",
        }, {
            "type": "BinaryChoice",
            "option1": "Yes",
            "option2": "No",
        }
    ]
})

jobs.update_tasks(koanJob, [oneHandClappingTask, buddhaNatureTask])

# Add tasks to meditation job
breathingMeditationTask = tasks.create({
    "name": "Breathing meditation",
    "components": [
        {
            "type": "Text",
            "style": "Instruction",
            "text": "Look at a wall. Don't move.",
        }, {
            "type": "VideoRecording",
            "minDurationInSeconds": 60 * 60,
            "maxDurationInSeconds": 60 * 60 * 24,
            "landscape": False,
        }
    ]
})

jobs.update_tasks(meditationJob, [breathingMeditationTask])


# You need to top up your account to publish the campaign!
# campaigns.publish(campaign)

campaign_list = campaigns.get_page()
print(json.dumps(campaign_list))

job_list = jobs.get_page()
print(json.dumps(job_list))
