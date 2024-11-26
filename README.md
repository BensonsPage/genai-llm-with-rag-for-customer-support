# llm-with-rag
- sample project for implementing RAG with LLM (gemini-1.5-flash-latest)

## Clone
- git clone https://github.com/BensonsPage/genai-llm-with-rag-for-customer-support

## Make App Changes.
- generate embeddings and index company specific knowledge using vector database (Chroma) as per the script createcromadatabase.py

## Checkout changes to a branch in your repository.
- git checkout -b branch-name
- git add * # To include changes in the commit.
- git commit -m "Update my app" # To Commit your changes.
- git push origin branch-name # push the branch to the remote repository.
- Merge your changes to your main branch.
- If you encounter issues refer to .

## build and run your docker container.
- navigate into the "genai-llm-with-rag-for-customer-support" and run below command
docker compose up 
- If you encounter error, make the changes and run below command to rebuild the image.
docker compose up -d --no-deps --build llmcustomersupportapp
- If you navigate to on your browser, you should see your app running on http://localhost:8000
- You can as well see your container "llmcustomersupportapp" running.

