

import server
import uvicorn
from config.config import Config
app = server.createApp()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=Config.PORT)