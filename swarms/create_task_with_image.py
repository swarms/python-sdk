import config
from sdk import services


campaigns, jobs, tasks, results = services.get(config)

tasks.create({
    "name": "Toomkirik",
    "components": [
        {
            "type": "Image",
            "url": "https://gallery.tasuki.org/gallery/2017/10-few-hours-in-tallinn/__18-toomkirik.jpg",
        }
    ]
})
