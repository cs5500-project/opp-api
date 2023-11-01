# High-level design
## Application Architecture
### Diagram
[Link to Lucidchart](https://lucid.app/lucidspark/8d2d6e36-c118-40bd-a856-62f6cb26e4d2/edit?viewport_loc=-6369%2C-1157%2C1839%2C1572%2C0_0&invitationId=inv_7fe0188e-fcb1-4dcc-981c-2f0019bb9fdc)
### Step to deploy to the Cloud
  1. We choose render.com to host the web servers.
  2. Packaging our application in to docker containers.
  3. Setup dababase on MongoDB.
  4. Prepare for scalability. Use load balancers or other close services to handle large traffic.
### Deployment Pipeline
  1. Code is stored in the cloud repository(Github).
  2. The code is compiled or built, generating artifacts (e.g., binaries, libraries).
  3. Unit tests are run to ensure that individual code components work as expected.
  4. Build docker container images and run successfully in local environment
  5. Once all tests and checks pass, the changes are deployed to the production environment. 
### Frontend Wireframes
[Link to Figma](https://www.figma.com/file/x1LuRa2y4Wm83u2NRH9tiy/Untitled?type=design&node-id=0%3A1&mode=design&t=pX7MuVYy0nwR7qRI-1)
### Description of Backend Modules
